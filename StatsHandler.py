'''
Created on 22 Nov 2014

@author: Gia
'''

def computeAverage(listOfValues):


    '''
    Compute the average of a given list of float or int values

    Input : A list of values.  If there are empty elements, they will be removed and total divided
        by the new number with the empty elements removed
    Output : a float of the average, rounded to 2 decimal places

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


