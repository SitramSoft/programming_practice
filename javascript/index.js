{
  //Exercise 1 - Count heads and tails from 10 coin tosses
  let heads = 0;
  let tails = 0;

  for (let x = 1; x <= 10; x++) {
    if (Math.random() < 0.5) {
      tails++;
    } else {
      heads++;
    }
  }

  console.log(
    `10 toses:\ntotal numbe of heads: ${heads}\nTotal nunmber of tails: ${tails}`
  );
}

{
  //Exercise 2 - How many times to flip a coin to land heads
  let toss = 0;

  while (Math.random() < 0.5) {
    toss++;
  }

  console.log(`The coin had to flip ${toss} times to land on heads`);
}

{
  //Exercise 3 - Print a pyramid of *
  let level = 5;
  let asterix = "";
  for (let i = 1; i <= level; i++) {
    asterix += "*";
    console.log(asterix);
  }
}

{
  //Exercise 3 - Print a reverse pyramid of *
  let level = 5;
  let asterix = "";

  for (let i = 1; i <= level; i++) {
    asterix += "*";
  }

  let i = level;

  while (i >= 1) {
    console.log(asterix);
    asterix = asterix.slice(0, -1);
    i--;
  }
}

{
  //Exercise 4 - Functions
  function greet(name = "default value") {
    //function body
    console.log(`My name is ${name}`);
  }

  function sum(a, b) {
    return a + b;
  }

  greet("Adi");
  greet();

  console.log(`${sum(2, 2)}`);
}

{
  //Exercise 5 - Function to calculate the area and perimeter of a sqare shape
  const calculateSquare = (side) => {
    console.log(`The square side is ${side}`);
    console.log(`The area of the square is ${side * side}`);
    console.log(`The perimeter of the square is ${4 * side}`);
  };

  calculateSquare(8);
}
