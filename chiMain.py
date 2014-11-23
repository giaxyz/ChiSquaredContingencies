import DataReadWrite
import StatsHandler as sh

import csv

def main():

    print("")



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

if __name__ == "__main__":

    main()

    ## First clean up the missing attributes by filling in all the floats and int attributes with the average
    ##     If the value is a string, put "not_applicable"
    cleanedData = fillMissingValues("worldData.csv", "worldDataMetaData.csv", 5)
    cleanedDataName = "worldDataFilled.csv"
    writeCSV(cleanedDataName,cleanedData)
    dataHandler = DataReadWrite.DataReadWrite(cleanedDataName)


    index = 15
    currentColumn = dataHandler.getColumnValuesAsFloat(index)
    #dataHandler.printColumn(index)

    #currentColumn = [1,2,3,4,2,2,2,25,5,5,5,8,8,8,8,100]
    #currentColumn = [5,5,5,5,5,5,5,5,5,5]
    currentColumn =[8,8,2,2,2,2,2,2,2,2]
    #currentColumn = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    skewThreshold = 1.5
    isSkewed = sh.computeSkewRatio (currentColumn, skewThreshold)
    print("Data skew : " )
    print(isSkewed)






















