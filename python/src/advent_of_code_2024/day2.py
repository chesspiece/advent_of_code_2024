"""
Solutions to day2 of advent of code
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
    report: list[int], diff_dir=MessageDirection.UNDEFINED, was_error=False
) -> tuple[bool, bool]:
    if len(report) <= 1:
        return (True, True)

    if diff_dir == MessageDirection.UNDEFINED:
        d1_inc, _ = check_report(report, MessageDirection.INC, True)
        d1_dec, _ = check_report(report, MessageDirection.DEC, True)
        day1_solution = d1_inc or d1_dec

        _, d2_inc = check_report(report, MessageDirection.INC, False)
        _, d2_dec = check_report(report, MessageDirection.DEC, False)
        day2_solution = d2_inc or d2_dec

        return (day1_solution, day2_solution)

    prev_val = report[0]
    for i in range(1, len(report)):
        curr_value = report[i]
        diff = prev_val - curr_value

        if diff > 0:
            curr_diff_dir = MessageDirection.INC
        elif diff < 0:
            curr_diff_dir = MessageDirection.DEC
        else:
            curr_diff_dir = MessageDirection.UNDEFINED

        if curr_diff_dir != diff_dir or not (1 <= abs(diff) <= 3):
            if was_error:
                return (False, False)
            else:
                _, solday2_opt1 = check_report(
                    report[i - 1 : i] + report[i + 1 :], diff_dir, True
                )
                _, solday2_opt2 = check_report(
                    report[i - 2 : i - 1]
                    + report[i:],  # Have not tested if it works when i==1
                    diff_dir,
                    True,
                )
                return (False, solday2_opt1 or solday2_opt2)

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
