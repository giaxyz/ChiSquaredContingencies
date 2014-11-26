'''
Created on 22 Nov 2014

@author: Gia
'''
import DataReadWrite

from _overlapped import NULL

def computeAverage(listOfValues):
    
    
    '''
    Compute the average of a given list of float or int values
    
    Keyword Input : A list of values.  If there are empty elements, they will be removed and total divided 
        by the new number with the empty elements removed
        
    Returns : a float of the average, rounded to 2 decimal places
    
    '''  
    strippedList = stripMissingValues(listOfValues)
    total = addValues(strippedList)
    lengthStrippedList = len(strippedList)
    average = float(total/lengthStrippedList)
    average = round(average, 2)
    return average

def addValues(listOfValues):
    
    """ Ouptut the total by summing all the numbers in a list.

    Keyword arguments:
    listOFValues : a list of float or integer values
    
    Returns : float
    
    """
    
    total = 0
    
    for v in listOfValues:
        
        total = total + float(v)
      
    return total
        
def stripMissingValues(listOfValues):
    
    '''
    
    Output a list with all missing values removed from any given list.
    If the list contains an empty string, "", it will remove the element and return a cleaned list
    
    Input : a list of values.  
    Output : a list of values with "" empty elements removed

    ''' 
    
    cleanedList = []
    
    
    for v in listOfValues:
        
        if (v != ""):
            cleanedList.append(v)
    
   
    return cleanedList
    
def isEven(value):
    
    '''
    
    Return true if a value is even, and false otherwise
    
    '''
   
    divValue = value % 2
    if (divValue == 0):
        return True
    else:
        return False

def computeMedian(listOfValues):
    
    '''
    Output the median value from an Input list of values
    
    '''
   
    sortedColumn = sorted(listOfValues)
    columnSize = len(listOfValues)
    columnSizeIsEven = isEven(columnSize)
    
    if(columnSizeIsEven):
        
       
        lowerMiddleIndex = medianIndex(listOfValues)
        upperMiddleIndex = (int)(columnSize/2)
        lowerMiddleValue = (float)(sortedColumn[lowerMiddleIndex])
        upperMiddleValue = (float)(sortedColumn[upperMiddleIndex])
             
        
        difference = upperMiddleValue - lowerMiddleValue
        splitDifference = difference / 2
        median = lowerMiddleValue + splitDifference
        
        
        
        
    else:
        
        middleIndex = medianIndex(listOfValues)
        median = (float)(sortedColumn[middleIndex])
        
    return median

def medianIndex(listOfValues):
    
    
    '''
    
    Input : list of Values
    Output : the position index of the middle value if the list of values is odd
            the position index of the lower middle value if the list of values is even
    
    '''
    
    columnSize = len(listOfValues)
    columnSizeIsEven = isEven(columnSize)
    
    if(columnSizeIsEven):
        middleIndex = (int)((columnSize/2) - 1)
    else:
        middleIndex = (int)((columnSize/2 + 0.5) - 1)
        
    return middleIndex
    
def maxValue(listOfValues):

    '''
        
        Output the max Value from an input list of values
    
    '''

   
    sortedColumn = sorted(listOfValues)
    columnSize = len(listOfValues)
    maxValue = (sortedColumn[columnSize - 1])
    return maxValue(listOfValues)

def minValue(listOfValues):
    
    '''
        
        Output the min Value from an input list of values
    
    '''
    
    sortedColumn = sorted(listOfValues)
    minValue = (sortedColumn[0])
    return minValue
    
def computeLowerQuartile(listOfValues):
    
    '''
    
    Compute the value of the Lower Quartile from a given list of values
    Keyword Input: a list of values
    
    Return : the lowerquartile value (float)
    
    '''
    lowerHalfList = []
    sortedColumn = sorted(listOfValues)
    medIndex = medianIndex(listOfValues)
    
    for i in range(0, medIndex + 1):
        lowerHalfList.append(sortedColumn[i])
 
    lowerQuartileValue = computeMedian(lowerHalfList)
    return lowerQuartileValue

def computeUpperQuartile(listOfValues):
    
    '''
    
    Compute the value of the Upper Quartile from a given list of values
    Keyword Input: a list of values
    
    Return : the Upper Quartile value (float)
    
    '''
    
    upperHalfList = []
    sortedColumn = sorted(listOfValues)
    
   
    
    lengthList = len(listOfValues)
    
    medIndex = medianIndex(listOfValues)
    listIsEven = isEven(lengthList)
    if(listIsEven):
        medIndex = medIndex + 1
    
    
    
    for i in range(medIndex, lengthList):
        upperHalfList.append(sortedColumn[i])
        
    upperQuartileValue = computeMedian(upperHalfList)
   
    return upperQuartileValue   
    
def getLowerQuartileFrequency(listOfValues):
    
    '''
    Return the frequency of the values that fall in the lower quartile range
    
    Input : list of values
    Return : the number of values in the lower quartile range of the given list of values
    
    '''
    valuesInLowerQuartile = []
    lowerHalf = []
    listOfValues = sorted(listOfValues)
    median = computeMedian(listOfValues)
    medIndex = medianIndex(listOfValues)
    lowerQuartile = computeLowerQuartile(listOfValues)
    
    for i in range(0, medIndex + 1):
        
        lowerHalf.append(listOfValues[i])
        
  
    for i in range(0, len(lowerHalf)):
        
        currentValue = (float)(lowerHalf[i])
       
        if((currentValue >= lowerQuartile) and (currentValue <= median)):
           
            valuesInLowerQuartile.append(lowerHalf[i])
         
    print("Values in lower quartile : " + str(valuesInLowerQuartile))
    lowerQuartileFrequency = len(valuesInLowerQuartile)
    return lowerQuartileFrequency

def getUpperQuartileFrequency(listOfValues):
    
    
    '''
    Return the frequency of the values that fall in the upper quartile range
    
    Input : list of values
    Return : the number of values in the upper quartile range of the given list of values
    
    '''
    
  
    valuesInUpperQuartile = []
    upperHalf = []
    listOfValues = sorted(listOfValues)
    median = computeMedian(listOfValues)
    
    medIndex = medianIndex(listOfValues)
    upperQuartile = computeUpperQuartile(listOfValues)
   
   
   
    listIsEven = isEven(len(listOfValues))
    if(listIsEven):
        medIndex = medIndex + 1
    
    for i in range(medIndex, len(listOfValues)):
        upperHalf.append(listOfValues[i])
    
   
      
    for i in range(0, len(upperHalf)):
        
        currentValue = float(upperHalf[i])
        
        if((currentValue >= median) and (currentValue <= upperQuartile)):
            valuesInUpperQuartile.append(upperHalf[i])
            
    upperQuartileFrequency = len(valuesInUpperQuartile)
    print("Values in upper quartile : " + str(valuesInUpperQuartile))
    return upperQuartileFrequency

def computeSkewRatio(listOfValues, threshold):
    
    '''
    Compute how skewed a distribution of  list of values is by dividing the frequency of the larger
    quartile to the smaller quartile.  
    
    Input: List of values
    Returns : skewed index.  Larger the value, the more the skewness of the distribution. 1.0 indicates no skew
    
    '''
    
    median = computeMedian(listOfValues);
    mean = computeAverage(listOfValues);
    #upperQuartile = computeUpperQuartile(listOfValues)
    #lowerQuartile = computeLowerQuartile(listOfValues)
    #upperQuartileFrequency = getUpperQuartileFrequency(listOfValues)
    #lowerQuartileFrequency = getLowerQuartileFrequency(listOfValues)
    larger = getLarger(mean, median)
    smaller = getSmaller(mean, median)
    skewRatio = larger/smaller
    #print("skewed ratio is : " + str(skewRatio))
    
    if(skewRatio < threshold) :
        return False
    else:
        return True
    
    return skewRatio

def getLarger(value1, value2):
    
    """
    Output the larger of two values
    Input : value1, value2  as float or ints
    Return : the greater value
    
    """
    if(value1 >= value2):
        return value1
    else:
        return value2

def getSmaller(value1, value2):
    
    
    """
    Output the smaller of two values
    Input : value1, value2  as float or ints
    Return : the smaller value
    
    """
    
    if(value1 <= value2):
        return value1
    else:
        return value2

def discretize(currentColumn, isSkewed, n, columnIndex, attrName, metaDataHandler): 
    
   
    '''
    Perform binning discretization - if skewed data, perform equal width.  If not skewed, perform equal depth partitioning 
    Input : column of values
        isSkewed : boolean True or False to indicate if the data is skewed or not
        n : the number of discretization intervals to perform binning
        
    Output : the new list of discretized values
    
    '''
     
    
    discreetLabels = getDiscreetLabelsFromMetadata(metaDataHandler, n, columnIndex)
    
    if(isSkewed):
        partitions = equalWidthPartition(currentColumn, n, columnIndex)
        
    else:
        partitions = equalDepthPartition(currentColumn, n, columnIndex)
    
    
    row = discretizeColumn(attrName, currentColumn, partitions, discreetLabels)
    
      
    return row

def equalWidthPartition(listOfValues, n, columnIndex):
    
    '''
    
    Create a list of partition values (of number n ) to divides the range in the list of values into n intervals of equal size
    Widths = (highest - lowest)/n
    Input : the list of values, n : number of partitions, columnIndex for which column of values
    Return : a list of n values for partitioning
    
    '''
    binValues = []
    sortedValues = sorted(listOfValues)
    highest = sortedValues[len(sortedValues) - 1]
    lowest = sortedValues[0]
    widths = ((highest - lowest) / n)
    
    #print("Discretizing Equal Width: " + "Column Index : " + str(columnIndex))
    #print(listOfValues)
   
    
    upperBound = lowest + widths
    
    for i in range (0, n):
        #print ("Bin : " + str(i) + " " + str(upperBound))
        binValues.append(upperBound)
        upperBound = upperBound + widths
    
    #print("Final Bin Values : ")
    #print(binValues)
    return binValues

def equalDepthPartition(listOfValues, n, columnIndex):
    
    '''
    Return a list of partition values for n bins
    to later divide the range into N intervals, each containing approximately same
        number of samples
        
    Input : the list of values, n : number of partitions, columnIndex for which column of values
    Return : a list of n values for partitioning
    
    '''
    
    binValues = []
    sortedValues = sorted(listOfValues)
    #print("Discretizing Equal Depth: " + "  Column Index : " + str(columnIndex))
    #print(listOfValues)
    binListSize = round(len(listOfValues) / n)
    currentBin = binListSize - 1
    #print("ListSize  is  " + str(binListSize))
    
    for i in range(0, n):
        
        if(i < (n-1)):
           
            #print("Bin : " + str(i) + " " + str(sortedValues[currentBin]))
            binValues.append(sortedValues[currentBin])
            currentBin = currentBin + binListSize
        
        else:
            
            #print("Bin : " + str(i) + " " + str(sortedValues[len(listOfValues) - 1]))
            binValues.append(sortedValues[len(listOfValues) - 1])
  
    #print("Final Bin Values : ")
    #print(binValues)
    return binValues

def getDiscreetLabelsFromMetadata(metaDataHandler, n, columnIndex): 
    
    """
    Output the discreet labels used for discretization of the current column attribute
    Input: the metadataHandler class with the metadata.csv, where columns 8,9,10 and 11 have discretization labels 
        column index : the index of the column to discretize
        n : the number of discretization binds
    Return : a list of discretization labels
    
    """
    
    #These inputs are hardcoded into the metadata file, refer to the "worldDataMetaData.csv"
    descriptors = metaDataHandler.getColumn(8)
    levelHighDescriptors = metaDataHandler.getColumn(9)
    levelMediumDescriptors = metaDataHandler.getColumn(10)
    levelLowDescriptors = metaDataHandler.getColumn(11)
  
    
    descriptor = descriptors[columnIndex + 1]
    levelHighDescriptor = ((levelHighDescriptors[columnIndex + 1]) + " " + descriptor) 
    levelMediumDescriptor = ((levelMediumDescriptors[columnIndex + 1]) + " " + descriptor) 
    levelLowDescriptor = ((levelLowDescriptors[columnIndex + 1]) + " " + descriptor)
    
    
    discreetLabels = []
    
    if(n == 3):

        discreetLabels.append(levelLowDescriptor)
        discreetLabels.append(levelMediumDescriptor)
        discreetLabels.append(levelHighDescriptor)
        
        
            
    elif(n == 2):
       
        discreetLabels.append(levelLowDescriptor)
        discreetLabels.append(levelHighDescriptor)
         
        
    else:
        
        raise ValueError ("Oops - n has to be either 2 or 3 in this case")
        

    return discreetLabels

def discretizeColumn(attributeName, listOfValues, partitions, discreetLabels): 
    
    
    """
    Perform discretiztion on a given column of data.  
    Input: 
        attributeName : the name of the attribute to add to the top of the column
        listOfValues : the discretization margins
        partitions : the number of partitions
        discreetLabels : the labels used to discretize within the listOfValues ie. partition values
    
    Return : the discretized column as a list, with the variable attribute name on the top
    
    """
    
    column = [attributeName]
   
  
    for i in range(0, len(listOfValues)):
        
        column.append(discreetLabels[0])
        
    for i in range(0, (len(partitions))-1):
        
        
        discreetLabelsIndex = i + 1
        nextLabel = discreetLabels[discreetLabelsIndex]
        nextPartition = partitions[i]
       
        
        for j in range(0, len(listOfValues)):
            
            currentValue = listOfValues[j]
            
            if(currentValue > nextPartition):
                
              
                column[j + 1] = nextLabel
                
    return column
    
    
    
    
     