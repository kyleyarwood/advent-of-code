use std::io::prelude::*;
use std::fs::File;

fn main() {
    let mut input_file = File::open("day1p1_input.txt")
        .expect("File can't be opened!");
    let mut input_file_contents = String::new();
    input_file.read_to_string(&mut input_file_contents)
        .expect("File can't be read!");

    let mut result = 0;
    let mut current_floor = 0;

    let input_bytes = input_file_contents.into_bytes();

    while current_floor != -1 {
        if input_bytes[result] == b'(' {
            current_floor += 1;
        } else if input_bytes[result] == b')' {
            current_floor -= 1;
        }
        result += 1;
    }

    println!("{}", result);
}
