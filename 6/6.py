import re
from functools import reduce
from typing import List


def part_one_solution(numbers: List[int]) -> int:
    length = len(numbers)
    times = numbers[:length // 2]
    distances = numbers[length // 2:]
    p = 1

    for i in range(length // 2):
        to_reach = distances[i]
        time = times[i]
        ways_of_reaching = 0

        for j in range(time):
            covered_distance_per_second = j
            remaining_seconds = time - j
            total_covered_distance = covered_distance_per_second * remaining_seconds
            if total_covered_distance > to_reach:
                ways_of_reaching += 1

        # print('final', ways_of_reaching)
        p *= ways_of_reaching

    return p


def part_two_solution(numbers: List[int]) -> int:
    ways_of_reaching = 0
    length = len(numbers)
    times = numbers[:length // 2]
    distances = numbers[length // 2:]

    time = int(reduce(lambda x, y: f"{x}{y}", times))
    distance = int(reduce(lambda x, y: f"{x}{y}", distances))

    for j in range(time):
        covered_distance_per_second = j
        remaining_seconds = time - j

        if covered_distance_per_second * remaining_seconds > distance:
            ways_of_reaching += 1

    return ways_of_reaching


if __name__ == "__main__":
    number_regex = re.compile(r"\d+")
    file_handler = open("6.in", "r")
    # file_handler = open("6_example.in", "r")
    text = file_handler.read()
    file_handler.close()

    numbers = [int(x) for x in number_regex.findall(text)]

    print(part_one_solution(numbers))
    print(part_two_solution(numbers))
