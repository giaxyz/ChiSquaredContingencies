'''
Created on 22 Nov 2014

@author: Gia
'''
import csv
import StatsHandler as sh

class DataReadWrite:
    
    def __init__(self, csv_file):
       
        self.csv_file = csv_file
            
    def printCSV(self):
        
        '''
        
        Print the entire the csv file
        
        '''
           
        f = open(self.csv_file, 'rt')
    
        try:
        
            reader = csv.reader(f)
            for row in reader:
                print (row)
                print("\n")
               
        finally:
                    
            f.close()
                    
    def num_columns_csv(self):
        
        '''
        Return the number of columns in the csv file
        
        '''

        f = open(self.csv_file, 'rt')
    
        firstRow = []
        lengthRows = 0
        count = 0
    
        try:
            reader = csv.reader(f)
        
            for row in reader:
            
                if(count == 0):
                    firstRow = row
                    lengthRows = len(firstRow)
                    count = count+1
                else:
                    break
                  
        finally:
             
            return lengthRows  
            f.close()
    
    def num_rows_csv(self):

        '''
        Return the number of rows in the csv file
        
        '''
        f = open(self.csv_file, 'rt')
    
        count = 0
        try:
            reader = csv.reader(f)
            for row in reader:         
                count = count + 1
     
        finally:
             
            return count  
            f.close()
  
    def printRow(self, rowIndex):

        '''
        Print the current row at Index : rowIndex
        Input : an integer of the index of the row
        Output : Print only the column at the row index
        Return : none
        
        '''
        
        f = open(self.csv_file, 'rt')
    
        index = 0
        try:
            reader = csv.reader(f)
            for row in reader:
            
                if(rowIndex == index):
                    print(row)
                    break
                index = index+1
               
               
                  
        finally:
        
            f.close()             
    
    def printColumn(self,columnIndex):

        '''
        Print the current column at Index : columnIndex
        Input : an integer of the index of the column
        Output : Print only the column at the column index
        Return : none
        
        '''
        
        f = open(self.csv_file, 'rt')
    
        try:
            reader = csv.reader(f)
            for row in reader:
            
                print(row[columnIndex])
                  
        finally:
        
            f.close() 
                
    def getRow(self, rowIndex):
        
        '''
        Get the current row at Index : rowIndex
        Input : an integer of the index of the row
        Output : the column at the row index
        
        '''
        
        f = open(self.csv_file, 'rt')
    
        index = 0
        rowList = []
        try:
            reader = csv.reader(f)
            for row in reader:
            
                if(rowIndex == index):
                    rowList = row
                    break
                index = index+1
               
               
                  
        finally:
        
            f.close()
            return rowList  

    def getColumn(self, columnIndex):
        
        '''
        Get the current column at Index : columnIndex
        Input : an integer of the index of the column
        Output : the column at the column index
        
        '''
        
        columnList = []
        
        f = open(self.csv_file, 'rt')
    
        try:
            reader = csv.reader(f)
            
            for row in reader:
            
                #print(row[columnIndex])
                columnList.append(row[columnIndex]) 
                
             
         
        finally:
        
            f.close()
            return columnList

    def getColumnValues(self, columnIndex):
        
        '''
        Input : the current column from the csv
        Output : The current column minus the first (top) element, to remove the column name (title)
        '''
        
        fullColumn = self.getColumn(columnIndex)
        lengthFullColumn = len(fullColumn)
        columnValues = fullColumn[1:lengthFullColumn]  
        return columnValues

    def computeAveragesByRow(self, listOfVariableTypes):
              
        '''
        
        Output a list of averages for the whole dataset, by each row. 
        If the data type is a string, put "not applicable" as the value
        This method iterates through each row by row, computing the average by column, 
            appending the averages through to the final averages list
            
        Missing values are first stripped, then the total of the values computed as an average of 
            the length of the list, minus the missing values
            
        Input : list of Variable types.  This is a String list of elements containing "string", "float", "int",
            indicating the data type of the attribute variable
            
        
        '''
      
        averagesByRow = []
        numColumns = self.num_columns_csv()
      
        for i in range (0, numColumns):
            
            currentColumn = self.getColumnValues(i)  
            currentColVariableType = listOfVariableTypes[i]
           
            if(currentColVariableType == "string"):
                averagesByRow.append("not_applicable")
            else:
                average = sh.computeAverage(currentColumn)
                averagesByRow.append(average)
                
        
        return averagesByRow
                      
    def getColumnValuesAsFloat(self, columnIndex):
        
        column = self.getColumnValues(columnIndex)
        columnAsFloat = []
        
        for i in range(0, len(column)):
            value = float(column[i])
            columnAsFloat.append(value)
        
        return columnAsFloat
            
        
        
               