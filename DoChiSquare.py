'''
Created on 24 Nov 2014

@author: Gia
'''
import csv
import DataReadWrite
from _overlapped import NULL

class DoChiSquare:
     
    def __init__(self, csv_file):
       
        self.csv_file = csv_file
        self.attr1Input = NULL
        self.attr2Output = NULL
        self.column1Input = NULL
        self.column2Output = NULL
        self.col1DiscreetLabels = []
        self.col2DiscreetLabels = []
        self.significanceLevel = 0.05

        
    def run(self, attr1, attr2):
        
        dataHandler = DataReadWrite.DataReadWrite(self.csv_file)
        self.column1 = dataHandler.getColumn(attr1)
        self.column2 = dataHandler.getColumn(attr2)
        self.attr1Input = self.column1[0]
        self.attr2Ooutput = self.column2[0]
        self.col1DiscreetLabels = self.getDiscreetLabels(self.column1)
        self.col2DiscreetLabels = self.getDiscreetLabels(self.column2)
        matrixInputSize = len(self.col1DiscreetLabels)
        matrixOutputSize = len(self.col2DiscreetLabels)
       
        chiMatrix = self.chiMatrixInitialize(matrixInputSize, matrixOutputSize)
        chiMatrix = self.chiMatrixCalculate(chiMatrix, matrixInputSize, matrixOutputSize, dataHandler, attr1, attr2)
    
                  
        print("Input Labels : " )
        print(self.col1DiscreetLabels)
        print("Output Labels : ")
        print(self.col2DiscreetLabels)
        print("Matrix of Input Rows, Output Columns, Array laid out as list of list of rows") 
        print(chiMatrix)      
        
        inputRowTotals = self.getTotalsInputRow(chiMatrix)
        outputRowTotals = self.getTotalsOutputRow(chiMatrix)
        grandTotal = (dataHandler.num_rows_csv()) 
        
        print("Input Row Totals : ")
        print(inputRowTotals)
        print("OutputRow Totals :")
        print(outputRowTotals)
        print("Total number of examples :")
        print(grandTotal)
        

       
    def getDiscreetLabels(self, columnData):
        
        """
        Iterate through the data given the column, and identify all the discreet labels
        Input : the column of data as a list
        Return : List of the discreet labels
        
        """
        labels = []
        
        for i in range(1, len(columnData)):
            currentLabel = str(columnData[i])
            
            if currentLabel not in labels:
                labels.append(currentLabel)
        
       
        return labels
        
    def chiMatrixInitialize(self, matrixInputSize, matrixOutputSize):
        
        """
        Create a matrix of inputs x outputs and initialize all values to zero
        Input : matrixInputSize (the number of input attributes)
                MatrixOutputSize (the number of output attributes)
        Output : Matrix as list : eg where input = 2 and output = 3, a list of [[0,0,0],[0,0,0]]
        
        """
        chiMatrix = []
        
        for i in range (0, matrixInputSize):      
            row = []
            for j in range(0, matrixOutputSize):
                
                row.append(0)   
            chiMatrix.append(row)
            
        return chiMatrix
          
    def chiMatrixCalculate(self, chiMatrix, matrixInputSize, matrixOutputSize, dataHandler, attr1, attr2):
        
        """
        Iterate through the data for the two attributes,(discretized), and output the chi matrix with the count
            table for all combinations
        Input : chi Matrix ( initialized to all values at 0
            matrix Input Size : the input dimenstion of the chi matri
            matrix Output Size : the output dimension of the chi matrix
            dataHandler : the DataHandler object class with the .csv of the data
            attr1 : the input attribute as integer column index from the csv
            attr2 : the output attribute as integer column index from the csv
        """
        
        for i in range(0, matrixInputSize):
          
            inputLabel = (self.col1DiscreetLabels[i]) # not sick, sick
            
          
            
            for j in range(0, matrixOutputSize):
                
                outputLabel = (self.col2DiscreetLabels[j]) # h1 h2, placebo
                numExamples = dataHandler.num_rows_csv()
                
                #print("Input label : " + inputLabel + " Output Label : " + outputLabel)
                
               
                for k in range (1,  numExamples + 1):  ## plus 1 here to account for the attribute row
                    currentExample =  dataHandler.getRow(k)
                    #print(currentExample)
                    currentExampleInput = currentExample[attr1] # what column did it come from???
                    currentExampleOutput = currentExample[attr2]
                    
                    if((currentExampleInput  == inputLabel) and (currentExampleOutput == outputLabel)):
                        chiMatrix[i][j] = chiMatrix[i][j] + 1 
                        
        return chiMatrix
    
    def getTotalsInputRow(self, chiMatrix):
        
        """
        Work out the contingency table row totals (input row totals)
        Input : the contingency table chiMatrix
        Return : list of totals for each input
        
        """
        
        inputTotals = []
        length = len(chiMatrix)
        
        for i in range (0, length):
            
            currentRowTotal = 0
            
            for j in range(0, len(chiMatrix[0])):
                           
                currentRowTotal = currentRowTotal + chiMatrix[i][j]
            
            inputTotals.append(currentRowTotal)
        
        return inputTotals
        
    def getTotalsOutputRow(self, chiMatrix):
        
        """
        Work out the contingency table row totals (output row totals)
        Input : the contingency table chiMatrix
        Return : list of totals for each output
        
        """
        
        outputTotals = []
        lengthRow = len(chiMatrix)
        lengthColumn = len(chiMatrix[0])
        
        for i in range(0, lengthColumn):
            
            currentTotal = 0

            for j in range (0,lengthRow):
                currentRow = chiMatrix[j]
                currentTotal = currentTotal + currentRow[i]
            
            outputTotals.append(currentTotal)
        
        return outputTotals
    
   
        
        