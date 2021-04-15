def collatz(number):
    if (number % 2) == 0:
        return number // 2
    else:
        return 3 * number + 1

number = 0
execute = True

print('Enter a number:')

try:
    number = int(input())
    
    if number == 0:
        execute = False
        
except ValueError:
    print('Invalid input value!')
    execute = False
    
while execute:
    number = collatz(number)
    print(str(number))
    if number == 1:
        break
