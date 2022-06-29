import string

def print_rangoli(size):
    # your code goes here
    alphabet = "-".join(string.ascii_lowercase)
    reverse_alphabet = alphabet[::-1]
    joined_alphabet = reverse_alphabet + alphabet[1::1]
    for x in range(size):
        print(x)
        #print(alphabet[2*(size-x)-2:2*size:1])
        print(joined_alphabet[(len(alphabet) - 2*(size))+1::1])
    #    for y in range(size):
        
    print(alphabet)
    #print(len(alphabet))
    print(reverse_alphabet)  
    #print(len(reverse_alphabet))
    print(joined_alphabet)
    #print(len(joined_alphabet))

    print(joined_alphabet[(len(alphabet) - 2*5)+1::1])
        

if __name__ == '__main__':
    #n = int(input())
    n = 5
    print_rangoli(n)