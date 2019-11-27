use std::io::prelude::*;
use std::fs::File;

fn main() {
    let mut input_file = File::open("day1p1_input.txt")
        .expect("File can't be opened!");
    let mut input_file_contents = String::new();
    input_file.read_to_string(&mut input_file_contents)
        .expect("File can't be read!");

    let mut result = 0;

    for i in input_file_contents.chars() {
        if i == '(' {
            result += 1;
        } else if i == ')' {
            result -= 1;
        }
    }

    println!("{}", result);
}
