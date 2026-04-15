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


def check_report(
    report: list[int], diff_dir=MessageDirection.UNDEFINED, was_error = False
) -> tuple[bool, bool]:
    if len(report) <= 1:
        return True
    #diff = curr_diff_dir
    day1_solution = False
    day2_solution = False

    if diff_dir == MessageDirection.UNDEFINED:
        prev_val = report[0]
        curr_value = report[1]
        diff = prev_val - curr_value
        if diff > 0:
            diff_dir = MessageDirection.INC
        elif diff < 0:
            diff_dir = MessageDirection.DEC
        else:
            raise Exception("I think task description makes this branch impossible")

    prev_val = report[0]
    for (idx, curr_value) in enumerate(report[1::]):
        diff = prev_val - curr_value
        if diff > 0:
            curr_diff_dir = MessageDirection.INC
        else:
            curr_diff_dir = MessageDirection.DEC

        if curr_diff_dir != diff_dir:
            if was_error:
                return (False, False)
            else:
                _, solday2 = check_report([report[idx-1]] + report[idx+1::], diff_dir, True)
                _, solday2_v2 = check_report([report[idx-2]] + report[idx::], diff_dir, True)
                return (False, solday2 or solday2_v2)
        
        diff_abs = abs(diff)
        if (diff_abs < 1) or (diff_abs > 3):
            if was_error:
                return (False, False)
            else:
                _, solday2 = check_report([report[idx-1]] + report[idx+1::], diff_dir, True)
                _, solday2_v2 = check_report([report[idx-2]] + report[idx::], diff_dir, True)
                return (False, solday2 or solday2_v2)
        prev_val = curr_value
    return (True, True)


def day2():
    messages_list = parse_part1()
    corrected_messages = 0
    corrected_messages_day2 = 0
    for message in messages_list:
        day1_flag, day2_flag = check_report(message)
        if day1_flag:
            corrected_messages += 1
        if day2_flag:
            corrected_messages_day2 += 1
    print(corrected_messages)
    print(corrected_messages_day2)
