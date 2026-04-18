use std::collections::HashMap;
use std::fs;
use std::path::PathBuf;

fn parse_line(line: &str) -> Result<Vec<i32>, String> {
    let values: Result<Vec<i32>, std::num::ParseIntError> =
        line.split_whitespace().map(|elem| elem.parse()).collect();
    values.map_err(|err| err.to_string())
}

fn parse_input(input: &str) -> Result<Vec<Vec<i32>>, String> {
    let mut res: Vec<Vec<i32>> = Vec::new();
    for (index, line) in input.lines().enumerate() {
        let intm_res = parse_line(line)?;
        res.push(intm_res);
    }
    Ok(res)
}
