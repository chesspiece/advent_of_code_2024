mod day1;

use std::io;

type PartFn = fn() -> Result<(), String>;

struct Day {
    part1: PartFn,
    part2: PartFn,
}

const DAYS: &[Day] = &[Day {
    part1: day1::day1_part1,
    part2: day1::day1_part2,
}];

fn main() -> Result<(), String> {
    let day_number = read_selected_day()?;
    let day = &DAYS[(day_number - 1) as usize];

    (day.part1)()?;
    (day.part2)()?;

    Ok(())
}

fn read_selected_day() -> Result<u32, String> {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .map_err(|error| format!("Failed to read day number from stdin: {error}"))?;

    input
        .trim()
        .parse::<u32>()
        .map_err(|error| format!("Invalid day number '{}': {error}", input.trim()))
}
