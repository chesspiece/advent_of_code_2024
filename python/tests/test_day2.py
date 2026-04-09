import numpy as np
import numpy.testing as npt
from pytest_mock import MockerFixture

from advent_of_code_2024.day2 import day2_part1, parse_part1

SAMPLE_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_parse_part1_returns_expected_arrays(mocker: MockerFixture) -> None:
    mocker.patch("builtins.open", mocker.mock_open(read_data=SAMPLE_INPUT))
    message_list = parse_part1()

    expected_message_list = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert message_list == expected_message_list


def test_day2_part1_prints_sample_answer(capsys, mocker: MockerFixture) -> None:
    mocker.patch("builtins.open", mocker.mock_open(read_data=SAMPLE_INPUT))
    result = day2_part1()

    captured = capsys.readouterr()
    assert result is None
    assert captured.out == "2\n"
