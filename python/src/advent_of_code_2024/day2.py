"""
Solutions to day1 of advent of code
"""

from enum import Enum


class MessageDirection(Enum):
    UNDEFINED = 1
    INC = 2
    DEC = 3


def parse_part1():
    with open("../inputs/day02.txt", "r") as f:
        for line in f:
            yield list(map(int, line.split()))


def check_report(report: list[int], curr_diff_dir=MessageDirection.UNDEFINED) -> bool:
    if len(report) <= 1:
        return True
    diff = curr_diff_dir

    if curr_diff_dir == MessageDirection.UNDEFINED:
        prev_val = report[0]
        curr_value = report[1]
        diff = prev_val - curr_value
        if diff > 0:
            diff_dir = MessageDirection.INC
        elif diff < 0:
            diff_dir = MessageDirection.DEC
        else:
            return False
        diff_abs = abs(diff)
        if (diff_abs < 1) or (diff_abs > 3):
            return False
        prev_val = curr_value

    prev_val = report[0]
    for curr_value in report[1::]:
        diff = prev_val - curr_value
        if diff > 0:
            curr_diff_dir = MessageDirection.INC
        else:
            curr_diff_dir = MessageDirection.DEC
        if curr_diff_dir != diff_dir:
            return False
        diff_abs = abs(diff)
        if (diff_abs < 1) or (diff_abs > 3):
            return False
        prev_val = curr_value
    return True


def day2_part1():
    messages_list = parse_part1()
    corrected_messages = 0
    for message in messages_list:
        if check_report(message):
            corrected_messages += 1
    print(corrected_messages)
