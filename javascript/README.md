# Practice JavaScript programming language

## Documentation

- Introduction to JavaScript Programming language synthax can be from freeCodeCamp - [Learn JavaScript for beginners](https://www.freecodecamp.org/news/learn-javascript-for-beginners/)

- I left at [Final Exercise: Build a Cash Register Machine](https://www.freecodecamp.org/news/learn-javascript-for-beginners/#finalexercisebuildeacashregistermachine)

## Instalation

### Ubuntu

- Node.js binary distributions are available from [NodeSource](https://github.com/nodesource/distributions).

- Download and import the Nodesource GPG key

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```

- Create deb repository

```bash
NODE_MAJOR=20
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```

- Run Update and install

```bash
sudo apt-get update
sudo apt-get install nodejs -y
```

- Unsinstalling Node.js

```bash
apt-get purge nodejs &&\
rm -r /etc/apt/sources.list.d/nodesource.list &&\
rm -r /etc/apt/keyrings/nodesource.gpg
```

- Test installed node.js version by checking the output of the following command

```bash
node -v
```

### ArchLinux

```bash
pacman -S nodejs npm
```

- Test installed node.js version by checking the output of the following command

```bash
node -v
```

## JavaScript specific shyntax

### Fow control statements(for and while statements)

```javascript
for ( [initialization]; [condition]; [arithmetic expression]) {
  // As long as condition returns true,
  // This block will be executed repeatedly
}

while (condition) {
  statement;
}
```

### Rest parameter

- The rest parameter is a parameter that can accept any number of data as its arguments. The arguments will be stored as an array. A function can only have one rest parameter, and the rest parameter must be the last parameter in the function.

```javascript
function printArguments(...args){
    console.log(args);
}

printArguments("A", "B", "C"); 
// [ 'A', 'B', 'C' ]
printArguments(1, 2, 3, 4, 5);
// [ 1, 2, 3, 4, 5 ]
```

### Arrow function

- Arrow function syntax allows toi create a function expression similar to regular function declaration
- when using the arrow function syntax, the curly brackets are required only when there is a mitiline function body
- arrow function allows to omit the round brackets when there is exactly one parameter for the function.
- when function has no parameters, the round brackets are mandatory

```javascript
function greetings(name) {
  console.log(`Hello, ${name}!`);
}

greetings("John"); // Hello, John!

const greetings1 = (name) => {
  console.log(`Hello, ${name}!`);
};

//or

const greetings2 = (name) => console.log(`Hello, ${name}!`);

//or

const greetings3 = name  => console.log(`Hello, ${name}`);

greetings1("John"); // Hello, John!
```

### Objects

- an object is declared using the curly brackets and each item inside the brackets is written in the `key:value` format.
- sring or numbers can be assigned as the key of an item and any type of data as the value, including a function.
- `this` keyword refers to the context of the code

```javascript
let myBook = {
  title: "JavaScript Introduction",
  author: "Nathan Sebhastian",
  describe: function () {
    console.log(`Book title: ${this.title}`);
    console.log(`Book author: ${this.author}`);
  },
};
```

- accesing the value of an object can be done either with the dot or the square brackets notation
- proprieties can be deleted, added, changed their value or checked if they exist

```javascript
let myBook = {
  title: "JavaScript Introduction",
  author: "Nathan Sebhastian",
};

console.log(myBook.title);
console.log(myBook["author"]);

// add release year property
myBook.year = 2023;

// change the author property
myBook.author = "John Doe";

//delete proprerty
delete myBook.author;

// check if property exists
console.log('tags' in myBook); // false
```
