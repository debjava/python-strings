'''
Created on Apr 13, 2019

@author: PIKU
'''

def splitterString(stringToSplit):
    ''' Split by string '''
    splittedValue = stringToSplit.split(",")
    print("First Value : ", splittedValue[0])
    print("Second Value : ", splittedValue[1])

def splitter1(stringToSplit):
    if (stringToSplit is not None and len(stringToSplit) != 0):
        print("It is not null , ", stringToSplit)
        splittedValues = stringToSplit.split(",")
        return splittedValues[0], splittedValues[1]
    else:
        return "default value 1", "default value 2"


if __name__ == '__main__':
    splitterString("Hello,World")
    firstValue, secondValue = splitter1("Hello,World")
    print(firstValue, "---------", secondValue)
