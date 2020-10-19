#Find largest odd number out of 10 numbers introduced by user
i = 0
x = 0
largest_odd_nr = 0
while i < 10:
    i= i + 1
    x = int(input('Enter integer ' + str(i) + ': '))
    if ((x % 2) == 0) and (x > largest_odd_nr):
        largest_odd_nr = x

if largest_odd_nr == 0:
    print('No odd number found from the inputed values')
else:
    print('The largest odd number from the values entered: ' + str(largest_odd_nr))
    
