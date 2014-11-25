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
       
    varTypesIndex = 5 #The column of the metadata.csv which lists each variable's type
    
    ## ------ Fill missing attributes by filling in all the floats and int attributes with the average
    ##     If the value is a string, put "not_applicable"
    
    
    cleanedData = fillMissingValues("worldData.csv", "worldDataMetaData.csv", varTypesIndex)
    cleanedDataName = "worldDataFilled.csv"
    metaDataName = "worldDataMetaData.csv"
    writeCSV(cleanedDataName,cleanedData)
    dataHandler = DataReadWrite.DataReadWrite(cleanedDataName)
    metaDataHandler = DataReadWrite.DataReadWrite(metaDataName)
    
    
    ## ------ Discretize all float and integer attributes in the data values
    
    finalData = []
    isTesting = False
    skewThreshold = 1.5
    numberOfPartitions = 3 ## number of parititions here can only be 2 or 3
    numColumns = len(dataHandler.getRow(0))
    start = 0
    
    if(isTesting):
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
    
    discretizedDataName = "worldDataDiscretized.csv"
    
    writeCSV(discretizedDataName, discretizedData)
    

    ## -------- Perform Chi Square
    
    dataHandlerDiscreet = DataReadWrite.DataReadWrite(discretizedDataName)
    #dataHandlerDiscreet.printCSV()
    
    testData = "herbs.csv"
    #testData = "worldDataDiscretized.csv"
    chiSquareHandler = DoChiSquare.DoChiSquare(testData)
    attr1 = 0 ## never put 0 in each of these when you're doing the world data
    attr2 = 1
    chiSquareHandler.run(attr1, attr2)
    
     
    
 
    
    
    
  
    
   
    

    
    
    
    

    
   
    
    