from days.day1 import day1_part1, day1_part2

if __name__ == "__main__":
    days_dict = {1: [day1_part1, day1_part2]}
    choosen_day = int(input().strip())
    try:
        needed_funcs = days_dict[choosen_day]
        for fnc in needed_funcs:
            fnc()
    except Exception as e:
        print("Error occured. This day is either don't exists or unimplemented")
        print(f"Your input was parsed as {e}")
