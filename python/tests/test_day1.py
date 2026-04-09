import numpy as np
import numpy.testing as npt
from pytest_mock import MockerFixture

from advent_of_code_2024.day1 import day1_part1, day1_part2, parse_part1, parse_part2

SAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_parse_part1_returns_expected_arrays(mocker: MockerFixture) -> None:
    mocker.patch("builtins.open", mocker.mock_open(read_data=SAMPLE_INPUT))
    first_list, second_list = parse_part1()

    npt.assert_array_equal(first_list, np.array([3, 4, 2, 1, 3, 3], dtype=np.int64))
    npt.assert_array_equal(second_list, np.array([4, 3, 5, 3, 9, 3], dtype=np.int64))


def test_parse_part2_returns_expected_counts(mocker: MockerFixture) -> None:
    mocker.patch("builtins.open", mocker.mock_open(read_data=SAMPLE_INPUT))
    first_list, second_dict = parse_part2()

    assert first_list == [3, 4, 2, 1, 3, 3]
    assert dict(second_dict) == {4: 1, 3: 3, 5: 1, 9: 1}


def test_day1_part1_prints_sample_answer(capsys, mocker: MockerFixture) -> None:
    mocker.patch("builtins.open", mocker.mock_open(read_data=SAMPLE_INPUT))
    result = day1_part1()

    captured = capsys.readouterr()
    assert result is None
    assert captured.out == "11\n"


def test_day1_part2_prints_sample_answer(capsys, mocker: MockerFixture) -> None:
    mocker.patch("builtins.open", mocker.mock_open(read_data=SAMPLE_INPUT))
    result = day1_part2()

    captured = capsys.readouterr()
    assert result is None
    assert captured.out == "31\n"
