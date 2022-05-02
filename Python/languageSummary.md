# Data types and variables

* Strings

```python
name = "Test"
```

* Lists

```python
groceries =["Milk", "Eggs", "Ice cream"]
```

* Dictionaries

```python
person ={
        'key': 'value',
        'name': 'Kalob',
        'language': 'Python'
}

person['name']
```

* tuples -> Lists that cannot be changed

```python
kids = ('Nathan', 'Daniel')
```

* sets -> a unique list. In example below if we print `foods` it will show only `{'Ice Cream', 'Pizza', 'Tacos'}`

```python
foods = {'Pizza', 'Tacos', 'Ice Cream', 'Pizza', 'Pizza', 'Tacos'}
```

* boolean

```python
is _adult = True
```

* assign the same value to multiple variables `a = b = 100`
* assign multiple values to multiple variables `a, b = 100, 200`

# Indexing

* Strings -> Individual items can be accessed with `name[x]` or `name[start:end]`. `start` or `end` can be skipped, but the `:` must be kept.
* Listst -> Individual items can be accessed with `name[x]` or `name[start:end]`. `start` or `end` can be skipped, but the `:` must be kept.

# Comments

* Simple comments in code must be marked by `#`

```python
# This is a simple comment
```

* Docstrings

```python
def things():
        """
        Hello
        """
```

# String Formatting

* Format strings with `.format` starting with Python 3.5 and up

```python
name = "Python"
course = "{} for Everybody".format(name)
```

* F Strings starting with Python 3.6 and up

```python
name = "Python"
print(f"The crash course language is {name}")
```

* Older way of string formatting

```python
print("Hello %s" % "World")

name = "Python"
print("Hello %s" % name)
```

# Files

* Create new file

```python
with open("try_me.py", "w") as file_handler:
        file_handler.write("print('Hello World lolololololo')")
        file_handler.close()
```

* Open an existing file

```python
with open(try_me.py","r") as file_handler:
        content = file_handler.read()
        file_handler.close()

print(content)
```

* Append to an existing file

```python
with open(try_me.py","a") as file_handler:
        file_handler.write("\nTesting line #2")
        file_handler.close()
```

# Operators

* Overview of basic operators can be found [here](https://www.tutorialspoint.com/python3/python_basic_operators.htm)

* Conditional branches

```python
lang = "Python 3"

if lang == "Ruby":
        print("You are using Ruby")
elif lang == "Python 2":
        print("Zomg please upgrade k thx baiii")
else:
        print(f"Anything else the value was {lang}")
```

* Comparison operators
  * `==` - equals
  * `>=` - greater then or equal
  * `<=` - less then or equal
  * `>` - greater
  * `<` - less
  * `!=` - is not equal

* Assignment operators
  * `=` - c = a + b assigns value of a + b into c
  * `+=` - c += a is equivalent to c = c + a
  * `-=` - c -= a is equivalent to c = c - a
  * `*=` - c *= a is equivalent to c = c * a
  * `/=` - c /= a is equivalent to c = c / a
  * `%=` - Modulus of two operands and assign the result to left operand
  * `**=` - Exponential (power) on two operands and assign value to the left
  * `//=` - Floor division on operators and assign value to the left operand

* Bitwise operators
  * `&` - Binary AND
  * `|` - Binary OR
  * `^` - Binary XOR
  * `~` - Binary Ones Complement
  * `<<` - Binary Left Shift
  * `>>` - Binary Right shift

* Logical operators
  * `and`
  * `or`
  * `not`

* Membership operators
  * `in`
  * `not in`

* Identity operators
  * `is`
  * `is not`

```python
  total = None
  type(total)
  if total is None:
        print("Is None")
```

# For loops

* `in` operator goes to iterables like: set, tuple, string, list

```python
groceries = ["Milk", "Eggs", "Ice cream"]

for item in groceries:
        print(f"The item is {item}")
```

* `break`
* `continue`

```python
name = "Python 3 Crash Course"
for letter in name:
        l = letter.lower()
        if l in 'aeiouy':
                print(f"Vowel is: {l}")
                continue
        if l == "3":
                print("Breaking on 3")
                break
```

* Access the index with the element

```python
for index, item in enumerate(items, start=0):   # default is zero
    print(index, item)
```

# While loops

```python
num = 0
while num < 10:
        print(num)
        num = num + 1
```

# List Comprehensions

Examples of ist multiplication

```python
nums = [1, 2, 3, 4, 5, 7, 8, 9, 10]
times_ten = [num*10 for num in nums]
times_ten2 = [num*10 for num in nums if num % 2 == 0]
```

# Functions

* function without parameters

```python
def name():
        return "A thing"

name()
```

* function with parameter

```python
def greeting(name):
        print(f"{name}, Hello to you good sir!")
```

* function with parameters with default value

```python
def greeting(name, greeting="Hello):
        return(f"{name}, {greeting} to you good sir!")
```

* function that returns another function

```python
import math
def make_cylinder_volume_func(r):
    def volume(h):
        return math.pi * r * r * h
    return volume
```

* Function annotations(starting with Python 3.5) which are dictionaries. Detailed explanation can be found [here](https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions?noredirect=1&lq=1)

```python
def main () -> None:
```

```python
def kinetic_energy(m:'in KG', v:'in M/S')->'Joules': 
    return 1/2*m*v**2
 
>>> kinetic_energy.__annotations__
{'return': 'Joules', 'v': 'in M/S', 'm': 'in KG'}
```

# Classes

* simple class definition

```python
class Person:
        pass

adi = Person()

adi

type(adi)
```

* every method in the class receives as parameter self

```python
class Person:
        name = "Adi"
        def speak(self):
```

* class with constructor

```python
class Person:
        def __init__(self, name, age, food)
        self.name = name
        self.age = age
        self.food = food
        def speak(self):
                print(f"Feed me more {self.food}")
        def get_name(self):
                print("The name of this person is", self.name)
        def __str__(Self):
                return self.name

adi = Person('Adi', 30, 'Pizza')
adi.speak()
adi.get_name()
print(adi) -> results in Adi
```

# Packages

* version of pip

```bash
pip -V
```

* Install new package

```bash
pip install <package_name>
```

* Uninstall a package

```bash
pip uninstall <package_name>
```

* Show details of a package

```bash
pip show <package_name>
```

* List all packages installed in the system

```bash
pip freeze
```

* A much better interactive editor then the standard shell is `ipython` which cab be installed with

```bash
sudo pip install ipython
```

# Try and Except

```python
try:
        1/0
except Exception as e: # except ZeroDivisionError:
        print(e)
        print(type(e))

print("It still runs!")
```