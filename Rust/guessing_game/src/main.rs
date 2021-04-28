use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new(); //creates a mutable variable. By default in Rust variables are immutable

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
 
    println!("You guessed: {}", guess);
}