# File containing exercises for chapter 8 of the Automate The Borring Stuff book - https://automatetheboringstuff.com/2e/chapter8/
# Uses library PyInputPlus -> pip install pyinputplus
import pyinputplus as pyip

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers) # Return an int form of numbers.

#response = pyip.inputNum(prompt="Enter a number: ")

# Display help page for a certain method from PyInputPlus library
# help(pyinputplus.inputNum)

#response = pyip.inputNum(prompt="Enter a number: ",min=3)

#response = pyip.inputNum(prompt="Enter a number: ",blank=True)

response = pyip.inputNum(prompt="Enter a number: ",limit=2, default=3)

response = pyip.inputCustom(addsUpToTen)

print(type(response))
print(response)