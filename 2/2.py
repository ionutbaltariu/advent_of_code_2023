import re

red_rgx = re.compile(r"(\d{1,}) red")
green_rgx = re.compile(r"(\d{1,}) green")
blue_rgx = re.compile(r"(\d{1,}) blue")

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_sum_of_possible_games_ids(text: str) -> int:
    ids_sum = 0
    for idx, line in enumerate(text.split("\n")):
        red_ok, green_ok, blue_ok = True, True, True
        print(line)
        for match in red_rgx.findall(line):
            if int(match) > MAX_RED:
                red_ok = False
                break

        for match in green_rgx.findall(line):
            if int(match) > MAX_GREEN:
                green_ok = False
                break

        for match in blue_rgx.findall(line):
            if int(match) > MAX_BLUE:
                blue_ok = False
                break

        if red_ok and green_ok and blue_ok:
            ids_sum += idx + 1
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")

    return ids_sum


def get_sum_of_fewest_cubes_needed_powers(text: str) -> int:
    power_sum = 0

    for line in text.split("\n"):
        max_red = max(int(x) for x in red_rgx.findall(line))
        max_green = max(int(x) for x in green_rgx.findall(line))
        max_blue = max(int(x) for x in blue_rgx.findall(line))

        print(line)
        print(f"product is {max_red * max_green * max_blue}")
        print(f"sum is {power_sum}")
        power_sum += max_red * max_green * max_blue

    return power_sum


if __name__ == "__main__":
    with open("2.in", "r") as f:
        print(get_sum_of_fewest_cubes_needed_powers(f.read()))
