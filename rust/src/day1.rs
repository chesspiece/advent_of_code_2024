use std::collections::HashMap;
use std::fs;
use std::path::PathBuf;

type PuzzleResult<T> = Result<T, String>;

#[derive(Debug, PartialEq, Eq)]
struct LocationLists {
    left: Vec<i64>,
    right: Vec<i64>,
}

impl LocationLists {
    fn total_distance(&self) -> i64 {
        let mut left = self.left.clone();
        let mut right = self.right.clone();

        left.sort_unstable();
        right.sort_unstable();

        let mut res: i64 = 0;

        for idx in 0..left.len() {
            res += (left[idx] - right[idx]).abs();
        }
        res
    }

    fn similarity_score(&self) -> i64 {
        let mut counts: HashMap<i64, i64> = HashMap::new();

        for value in &self.right {
            *(counts.entry(*value).or_insert(0_i64)) += 1;
        }

        let mut res: i64 = 0;

        for left_val in &self.left {
            let intermediate_result = match counts.get(left_val) {
                None => 0,
                Some(value) => left_val * value,
            };
            res += intermediate_result;
        }
        res
    }
}

fn load_lists() -> PuzzleResult<LocationLists> {
    let path = PathBuf::from("./../inputs/day01.txt");
    let input = fs::read_to_string(&path)
        .map_err(|error| format!("Failed to read {}: {error}", path.display()))?;
    parse_input(&input)
}

fn parse_input(input: &str) -> PuzzleResult<LocationLists> {
    let mut left = Vec::new();
    let mut right = Vec::new();

    for (index, line) in input.lines().enumerate() {
        if line.trim().is_empty() {
            continue;
        }

        let (left_value, right_value) =
            parse_pair(line).map_err(|error| format!("Line {}: {error}", index + 1))?;

        left.push(left_value);
        right.push(right_value);
    }

    Ok(LocationLists { left, right })
}

fn parse_pair(line: &str) -> PuzzleResult<(i64, i64)> {
    let mut values = line.split_whitespace();

    let left = values
        .next()
        .ok_or_else(|| "Expected exactly two integers".to_string())?;
    let right = values
        .next()
        .ok_or_else(|| "Expected exactly two integers".to_string())?;

    if values.next().is_some() {
        return Err("Expected exactly two integers".to_string());
    }

    let left = left
        .parse::<i64>()
        .map_err(|error| format!("Invalid integer '{left}': {error}"))?;
    let right = right
        .parse::<i64>()
        .map_err(|error| format!("Invalid integer '{right}': {error}"))?;

    Ok((left, right))
}

pub fn day1_part1() -> PuzzleResult<()> {
    let lists = load_lists()?;
    println!("{}", lists.total_distance());
    Ok(())
}

pub fn day1_part2() -> PuzzleResult<()> {
    let lists = load_lists()?;
    println!("{}", lists.similarity_score());
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::{parse_input, parse_pair, LocationLists};

    const SAMPLE_INPUT: &str = "\
3   4
4   3
2   5
1   3
3   9
3   3
";

    #[test]
    fn parses_pair_with_multiple_spaces() {
        let pair = parse_pair("3   4").unwrap();
        assert_eq!(pair, (3, 4));
    }

    #[test]
    fn rejects_rows_with_extra_values() {
        let error = parse_pair("1 2 3").unwrap_err();
        assert!(error.contains("exactly two integers"));
    }

    #[test]
    fn parse_input_reports_line_numbers() {
        let error = parse_input("1 2\n3 a\n").unwrap_err();
        assert!(error.contains("Line 2"));
        assert!(error.contains("Invalid integer"));
    }

    #[test]
    fn computes_total_distance_from_sample() {
        let lists = parse_input(SAMPLE_INPUT).unwrap();
        assert_eq!(lists.total_distance(), 11);
    }

    #[test]
    fn computes_similarity_score_from_sample() {
        let lists = parse_input(SAMPLE_INPUT).unwrap();
        assert_eq!(lists.similarity_score(), 31);
    }

    #[test]
    fn parses_input_into_columns() {
        let lists = parse_input("1 3\n2 4\n").unwrap();
        assert_eq!(
            lists,
            LocationLists {
                left: vec![1, 2],
                right: vec![3, 4],
            }
        );
    }
}
