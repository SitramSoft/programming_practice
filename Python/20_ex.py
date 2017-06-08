def spam():
    eggs = 'spam local'
    print(eggs) #prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) #prints 'bacon local'
    spam()
    print(eggs) #prints 'bacon local'

def spam_global():
    global eggs
    print(eggs) #prints 'global'

eggs = 'global'
bacon()
spam_global()
print(eggs) #prints 'global'
