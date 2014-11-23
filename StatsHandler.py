'''
Created on 22 Nov 2014

@author: Gia
'''
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
    
    if(value1 >= value2):
        return value1
    else:
        return value2

def getSmaller(value1, value2):
    
    if(value1 <= value2):
        return value1
    else:
        return value2

def discretize(currentColumn, isSkewed): 
    
    #currentColumn = [1,2,3,4,2,2,2,25,5,5,5,8,8,8,8,100]
    #currentColumn = [5,5,5,5,5,5,5,5,5,5]
    #currentColumn = [8,8,2,2,2,2,2,2,2,2]
    #currentColumn = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    if(isSkewed):
        
        print("Skewed")
        
    else:
        
        print("Not Skewed")
        
  
           
    