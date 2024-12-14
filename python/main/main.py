import sys

from days.day1 import day1_part1, day1_part2

if __name__ == "__main__":
    days_dict = {1: [day1_part1, day1_part2]}
    try:
        choosen_day = int(input().strip())
    except Exception as e:
        print("No such day is available!")
        print(e)
        sys.exit(0)
    try:
        needed_funcs = days_dict[choosen_day]
        for fnc in needed_funcs:
            fnc()
    except Exception as e:
        print("Error occured. This day is either don't exists or unimplemented")
        print(e)