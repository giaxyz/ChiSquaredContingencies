import DataReadWrite
import StatsHandler as sh
import csv
import DoChiSquare

from _overlapped import NULL

def getVariableName(columnIndex):      
    
    '''
    Procedure to check the name of the attribtue in a specified column in the data csv file
    Input: columnIndex, The index of the csv column of the original data
            
    Return : the variable name, as a string
    
    
    '''

    
    attributeRow = dataHandler.getRow(0)
    attributeName = (attributeRow[columnIndex])
    return attributeName

def getVariableType(columnIndex, varTypesIndex):      
    
    '''
    Procedure to check what type the variable is, based on the metadata in the metadata.csv
    Input: columnIndex, The index of the csv column of the original data
            varTypesIndex : the column where the variable types is listed in the metaadata.csv
    Return : the variable type, as a string
    
    
    '''

    metaDataHandler = DataReadWrite.DataReadWrite("worldDataMetaData.csv")
    variableTypes = metaDataHandler.getColumnValues(varTypesIndex) # where the varTypes lives in the metadata csvcsv
    variableType = (variableTypes[columnIndex])
    attributeRow = dataHandler.getRow(0)
    attributeName = (attributeRow[columnIndex])
    

    return variableType
       
def writeCSV(newCsvName, data):
        
        '''
        Writes out a csv file
        Input newCsvName : the name of the csv file to write
            data : a list of lists as the data points
        Output : writes out the csv
        Return : none
        '''
    
        with open(newCsvName, 'w', newline='') as fp:
      
            a = csv.writer(fp, delimiter=',')
            a.writerows(data)        
               
def fillMissingValues(csv_data, csvMetaData, varTypesIndex):
 
    '''
    Method to preprocess the data
    Input : CSV data file, (string) 
        csv Meta data file, (string)
        varTypesIndex (int - index of the column in the metadate file which states the variable types by column in the data file)  
    
    Output : writes out the file with computed averages in the missing values
    
    '''
    
    cleanedData = []
    
    # Read the data and the metadata
    dataHandler = DataReadWrite.DataReadWrite(csv_data)
    metaDataHandler = DataReadWrite.DataReadWrite(csvMetaData)
    
    # Read the variable types
    variableTypes = varTypesIndex
    variableTypesColumn = metaDataHandler.getColumnValues(variableTypes)
    
    # Get all the averages by row.  If its a string, "not applicable"
    averagesByRow = dataHandler.computeAveragesByRow(variableTypesColumn)
    numOfRows = dataHandler.num_rows_csv()
    numOfCols = dataHandler.num_columns_csv()
   
    # Clean each row by checking the averages and placing the respective column average in the row
    for i in range(0, numOfRows):
       
        filledRow = []
        currentRow = dataHandler.getRow(i)
       
        
        for j in range(0, numOfCols):
            
            currentValue = currentRow[j]
            
            if(currentValue == ""):
                
                averageString = str(averagesByRow[j])
                filledRow.append(averageString)
                
            else:
               
                filledRow.append(currentValue)
                
       
        cleanedData.append(filledRow)
    
    return cleanedData
          
    
   
    #testRow = dataHandler.getRow(5)

def convertToRows(listOfColumns):
    
    data = []
  
    numColumns = len(listOfColumns)
    numRows = len(listOfColumns[0])
    
    for i in range(0, numRows):
        
        row = []
        
        for j in range(0, numColumns):
            
            row.append(listOfColumns[j][i])
        
        data.append(row)
        
   
    return data

if __name__ == "__main__":
       
    # DO NOT TOUCH
    varTypesIndex = 5 #The column of the metadata.csv which lists each variable's type 
    cleanedDataName = "worldDataFilled.csv"
    discretizedDataName = "worldDataDiscretized.csv"
    metaDataName = "worldDataMetaData.csv"
    
    ## ------ Fill missing attributes by filling in all the floats and int attributes with the average
    ##     If the value is a string, put "not_applicable"
    
    
    cleanedData = fillMissingValues("worldData.csv", "worldDataMetaData.csv", varTypesIndex)
    writeCSV(cleanedDataName,cleanedData)
    dataHandler = DataReadWrite.DataReadWrite(cleanedDataName)
    metaDataHandler = DataReadWrite.DataReadWrite(metaDataName)
    
    
    ## ------ Discretize all float and integer attributes in the data values
    
    finalData = []
    isTesting = False ## Set this to discretize test columns only. See below, if(isTesting) 
    skewThreshold = 1.5
    numberOfPartitions = 3 ## number of parititions here can only be 2 or 3
    numColumns = len(dataHandler.getRow(0))
    start = 0
    
    if(isTesting): ## if testing, set these to the test columns
        start = 3
        numColumns = 5
    
    discretizedColumns = []
    
    for i in range(start, numColumns):
        
        currentColumn = dataHandler.getColumnValues(i)
        currentAttrName = getVariableName(i)
        currentAttributeType = getVariableType(i, varTypesIndex)
        
        if(currentAttributeType != "string"):
                        
            currentColumn = dataHandler.getColumnValuesAsFloat(i)
            isSkewed = sh.computeSkewRatio (currentColumn, skewThreshold)
            discretizedColumn = sh.discretize(currentColumn, isSkewed, numberOfPartitions, i, currentAttrName, metaDataHandler)
            discretizedColumns.append(discretizedColumn)
        
        else:
            
            currentColumn = dataHandler.getColumn(i)
            discretizedColumns.append(currentColumn)
   
    
    ## ---------- Convert Discretized columns to rows and write out the data 
    
    discretizedData = convertToRows(discretizedColumns)
    writeCSV(discretizedDataName, discretizedData)
    dataHandlerDiscreet = DataReadWrite.DataReadWrite(discretizedDataName)
    #dataHandlerDiscreet.printCSV()

    ## --------------  Perform Chi Square Test  and output p-Values --------------------
    
    # ----- Leave this code in for testing purposes only, but ignore
    #finalData = "herbs.csv"
    #chiSquareHandler = DoChiSquare.DoChiSquare(finalData)
    
    ## Set the input and output attributes, where attr1 is the input attribute, attr 2 is the output attribute
    #attr1 = 1 ## never put 0 in each of these when you're doing the world data
    #attr2 = 0
    #printConclusion = False
    #chiValueRank = chiSquareHandler.run(attr1, attr2, printConclusion)
    #print(chiValueRank)
    
    #  ----- Perform chi square specific to the worldData.csv provided
  
    ## List of attributes in the world.csv file which will be the input attributes.
    # where 27 and 28 are discreet attributes, the rest are floats
    worldDataAttributes = [1,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,20,21,22,25,26,27,28] 
    outputAttribute = 10 ## set to sugar
    outputAttrName = getVariableName(outputAttribute)
    printConclusion = True
    finalData = discretizedDataName
    chiSquareHandler = DoChiSquare.DoChiSquare(finalData)
    
    rankedNames = []
    rankedPValues = []
    
    # For every input attribute, caclulate the p-value
    for i in range(0, len(worldDataAttributes)):
        
        if(i != outputAttribute):
            name = getVariableName(worldDataAttributes[i])
            rankedNames.append(name)
            #name = getVariableName(26)
            attr1 = worldDataAttributes[i]
            attr2 = outputAttribute
            #print("Attribute index : " + str(attr1) + " Name : " + name + " Output Attr : " + outputAttrName)
            chiValueRank = chiSquareHandler.run(attr1, attr2, printConclusion)
            rankedPValues.append(chiValueRank)
            
    sortedRanks = sorted(rankedPValues)
    
    ## Sort each p-Value according to how highly they are ranked 
    
    j = len(sortedRanks) - 1
    for i in range(0, len(sortedRanks)):
        
        currentPValue = sortedRanks[j]
       
        
        
        for k in range(0, len(rankedPValues)):
            
            if(rankedPValues[k] == sortedRanks[j]):
                
                print("Attribute : " + str(rankedNames[k]) + "  Chi P-Value Rank : " + str(rankedPValues[k]))
        
        j = j - 1
  
    
 
    
    
    
  
    
   
    

    
    
    
    

    
   
    
    