# https://adventofcode.com/2023/day/1

def solution_part_one(text: str) -> int:
    s = 0
    for line in text.split('\n'):
        line_digits = [c for c in line if c.isdigit()]
        s += int(line_digits[0] + line_digits[-1])
    return s


DIGITS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one', 'two',
    'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]


def get_first_and_last(text: str) -> (str, str):
    find_indexes = {}
    length = len(text)

    for d in DIGITS:
        start = 0
        while True:
            searched = text.find(d, start)
            if searched == -1:
                break

            if d not in find_indexes:
                find_indexes[d] = [searched]
            else:
                find_indexes[d].append(searched)

            if searched + 1 < length:
                start = searched + 1
            else:
                break

    translation = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    first_digit = min(find_indexes.items(), key=lambda x: x[1][0])[0]
    last_digit = max(find_indexes.items(), key=lambda x: x[1][-1])[0]

    return translation.get(first_digit, first_digit), translation.get(last_digit, last_digit)


def solution_part_two(text: str) -> int:
    s = 0
    for line in text.split('\n'):
        first_digit, last_digit = get_first_and_last(line)
        # print(line, first_digit, last_digit)
        s += int(first_digit + last_digit)
    return s


if __name__ == "__main__":
    # print(get_first_and_last('sixhdnslspbrcsdvxnnk7kjlzxrrlk7bbrjxbxlq'))
    with open("1.in") as f:
        # print(solution_part_one(f.read()))
        print(solution_part_two(f.read()))
