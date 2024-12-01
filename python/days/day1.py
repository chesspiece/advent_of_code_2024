"""
Solutions to day1 of advent of code
"""

import re
from collections import defaultdict

import numpy as np
import numpy.typing as npt


def parse_part1() -> tuple[npt.NDArray[np.int64], npt.NDArray[np.int64]]:
    first_list: list[int] = []
    second_list: list[int] = []
    spaces = re.compile(" +")
    with open("../day1.txt", "r") as f:
        for line in f:
            ar1, ar2 = map(int, spaces.sub(" ", line.strip()).split(" "))
            first_list.append(ar1)
            second_list.append(ar2)
    return np.array(first_list), np.array(second_list)


def parse_part2() -> tuple[list[int], dict[int, int]]:
    first_list: list[int] = []
    second_list_dict: dict[int, int] = defaultdict(lambda: 0)
    spaces = re.compile(" +")
    with open("../day1.txt", "r") as f:
        for line in f:
            ar1, ar2 = map(int, spaces.sub(" ", line.strip()).split(" "))
            first_list.append(ar1)
            second_list_dict[ar2] += 1
    return first_list, second_list_dict


def day1_part1():
    first_list, second_list = parse_part1()
    first_list.sort()
    second_list.sort()
    diff = np.abs(first_list - second_list).sum()
    print(diff)
    return


def day1_part2():
    first_list, second_dict = parse_part2()
    diff = 0
    for id in first_list:
        diff += id * second_dict[id]
    print(diff)
    return
