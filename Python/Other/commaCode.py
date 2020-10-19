def commaCode(inputList):
    myString = ''
    
    for i in inputList:   
        if (inputList.index(i) == (len(inputList) - 1)):
            myString = myString + 'and ' + str(i)
        else:
            myString = myString + str(i) + ', '
    return myString

inputValue = ''
spam = []

print('Insert next list member. Finish by an empty line!')
inputValue = input()

while (inputValue != ''):
    spam.append(inputValue);
    print('Insert next list member. Finish by an empty line!')
    inputValue = input()

print(commaCode(spam))
