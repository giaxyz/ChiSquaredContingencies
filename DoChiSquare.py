'''
Created on 24 Nov 2014

@author: Gia
'''
import csv
import DataReadWrite
import StatsHandler as sh
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
        self.significanceLevel = 0.05 # significance label, used for critical values from the chi squared table below
        self.criticalValues = [3.841, 5.991, 7.815, 9.488, 11.070, 12.592, 14.067, 15.507, 16.919, 18.31, 19.68,21.03]
        self.round = 3 # number of decimal places to compute general math

        
    def run(self, attr1, attr2, printConclusion):
        
        ## ------ Set all the variables necessary, and set up the chi squared table from the data -----------
        dataHandler = DataReadWrite.DataReadWrite(self.csv_file)
        self.column1 = dataHandler.getColumn(attr1)
        self.column2 = dataHandler.getColumn(attr2)
        self.attr1Input = self.column1[0]
        self.attr2Ooutput = self.column2[0]
        self.col1DiscreetLabels = self.getDiscreetLabels(self.column1)
        self.col2DiscreetLabels = self.getDiscreetLabels(self.column2)
        matrixInputSize = len(self.col1DiscreetLabels)
        matrixOutputSize = len(self.col2DiscreetLabels)
        degreesOfFreedom = self.getDegreesOfFreedom(matrixInputSize, matrixOutputSize)
        chiMatrix = self.chiMatrixInitialize(matrixInputSize, matrixOutputSize)
        chiMatrix = self.chiMatrixCalculate(chiMatrix, matrixInputSize, matrixOutputSize, dataHandler, attr1, attr2)
        inputRowTotals = self.getTotalsInputRow(chiMatrix)
        outputRowTotals = self.getTotalsOutputRow(chiMatrix)
        grandTotal = (dataHandler.num_rows_csv()) 
        outputObservedPercentages = self.getOutputPercentages(outputRowTotals, grandTotal)
        expectedValuesMatrix = self.getExpectedValuesMatrix(inputRowTotals, outputObservedPercentages, chiMatrix)
        
        ## Use the chiMatrix and the expected values matrix  to compute the p-values
        
        chiSquaredValue = self.getChiSquaredValue(chiMatrix, expectedValuesMatrix)
        
        ## Compare the p-value to the critical values
        criticalValue = self.criticalValues[degreesOfFreedom - 1]
        
        ## Print out the conclusion
        conclusion = self.concludePValue(chiSquaredValue, criticalValue)
        
        if(printConclusion):
            #print("Matrix of Observed Values as Output Rows, Input Columns, Array laid out as list of list of rows :") 
            #print(chiMatrix) 
            #print("Input Row Totals : ")
            #print(inputRowTotals)
            #print("OutputRow Totals :")
            #print(outputRowTotals)
            print("\n\n-------Calculating Chi Square Between : ")
            print("Input : " + str(self.col1DiscreetLabels)  + " and Output : " + str(self.col2DiscreetLabels))    
            print("   Total number of examples :  " + str(grandTotal))
            #print("Output Percentages :")
            #print(outputObservedPercentages)
            print("   Expected Matrix : " + str(expectedValuesMatrix))
            print("   Observed Matrix : " + str(chiMatrix))
            print("   Chi-Squared Critical p-value for " + str(self.significanceLevel) + " is : " + str(criticalValue))
            print("   Chi-Squared p-Value Calculated is :  " + str(chiSquaredValue))
            print("\n\n")
            print(conclusion)
        
        return(chiSquaredValue - criticalValue)
        
       
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
    
    def getOutputPercentages(self, outputRowTotals, grandTotal):
        
        '''
        
        Work out the observed percentages of the output row
        Input : the list of row totals (the output row) of obsevations of the input attribute
        Return : the list of row totals as a percentage of the total number of observations
        
        '''
        
        observedPercentages = []
        
        
        for i in range(0, len(outputRowTotals)):
            
            #percentage = round((outputRowTotals[i] / grandTotal), 2)
            percentage = (outputRowTotals[i] / grandTotal)
            observedPercentages.append(percentage)
            
        return observedPercentages
        
    def getExpectedValuesMatrix(self, inputRowTotals, outputObservedPercentages, chiMatrix):
        
        
        """
        Comput the expected values of a given chi squared contingency table, and return another matrix of 
            expected values
            
        Input: inputRowTotals - the totals of the input row
            outputObservedPercentages : the percentages of the outputs observed in the output attribute
            chiMatrix : the values between inputs and outputs in the matrix of values
        Return : the matrix of expected values
        
        Return:
        """
        expectedMatrix = []
          
        for i in range(0, len(inputRowTotals)):
            
            expectedRow = []
            
            for j in range(0, len(outputObservedPercentages)):
                
                expectedValue = round(inputRowTotals[i] * (outputObservedPercentages[j]), 2)
                
                expectedRow.append(expectedValue)
            
            expectedMatrix.append(expectedRow)
        
        
        return expectedMatrix
    
    def getChiSquaredValue(self,chiMatrix, expectedValuesMatrix):
        
        '''
        Procedure to compute the chi value from a matrix of expected values and observed values
        Chi value = ((observed - expected) ^ 2) / expected --> summed all
       
        Input : chiMatrix : Matrix of Observed Values
           expectedValuesMatrix : matrix of Expected Values (must be the same dimension)
           
        Return : Chi Value
        
        '''
        
        chiValues = []
        
        for i in range(0, len(chiMatrix)):
            
            for j in range(0, len(chiMatrix[i])):
                
                observed =  (chiMatrix[i][j])
                expected =  (expectedValuesMatrix[i][j])
                
                chiValueInterim = (observed-expected)
                chiValueInterim = chiValueInterim * chiValueInterim
                chiValueInterim = chiValueInterim / expected
                chiValues.append(chiValueInterim)
                
       
        chiValue = round(sh.addValues(chiValues), self.round)
        return chiValue
                
    def getDegreesOfFreedom(self, matrixInputSize, matrixOutputSize):
            
            """
            Caclulate the degrees of freedom between the input and output variables
            Input : matrixInputSize : the size of the inputs in the matrix table
                    matrixOutputSize : the size of the outputs in the matrix table
            Return : the degrees of freedom 
            
            """
            deg_of_freedom = (matrixInputSize - 1) * (matrixOutputSize - 1)
            return deg_of_freedom
    
    def concludePValue(self, chiSquaredCalculated, criticalValue):  
        
        """
        Write out a conclusion string, based on the chi squared value and the critical value
            ie, accept or reject the null hypothesis
        Input : chiSquaredCalculated the chi square pvalue which you calculated from the data
                critical value : the critical chi-squared value from the table
        Return : A string wiht the conclusion information
        
        """
        
        conclusion = ""
        
        if(chiSquaredCalculated > criticalValue):
            conclusion = ("Null Hypothesis : REJECT (there is likely a correlation)")
        else:
            conclusion = conclusion = ("Null Hypothesis : ACCEPT (there is litte or no chance of correlation)")
        ## if it's greater than the critical value, then reject the null hypothesis, ie there is a correlation
            
        conclusion = conclusion +("     between Input : " + str(self.col1DiscreetLabels)  + " and Output : " + str(self.col2DiscreetLabels))
        conclusion = conclusion + ("\n\n")
        
        return conclusion     
        