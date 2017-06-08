import random, sys

while True:
    print('Type exit to exist.')
    response = raw_input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
