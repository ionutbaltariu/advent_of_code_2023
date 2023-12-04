from collections import deque


def get_number_of_winning_numbers(line):
    _, after_two_points = line.split(":")
    before_vertical, after_vertical = after_two_points.split("|")
    before_vertical = set(int(x) for x in before_vertical.strip().split(" ") if x != '')
    after_vertical = set(int(x) for x in after_vertical.strip().split(" ") if x != '')
    intersection = before_vertical.intersection(after_vertical)
    return intersection


def part_one_solution(text: str) -> int:
    s = 0

    for line in text.split("\n"):
        intersection = get_number_of_winning_numbers(line)

        if (length := len(intersection)) > 0:
            s += pow(2, length - 1)

    return s


def part_two_solution(text: str) -> int:
    # I feel like this is a really dumb solution
    points = {}
    scratch_cards = 0
    main_q = deque()
    copy_q = deque()

    for idx, line in enumerate(text.split("\n")):
        intersection = get_number_of_winning_numbers(line)
        points[idx] = len(intersection)

    for card_idx, card_points in points.items():
        main_q.append((card_idx, card_points))

    while main_q:
        if not copy_q:
            card_idx, card_points = main_q.popleft()
            scratch_cards += 1

            for idx in range(card_idx + 1, card_idx + card_points + 1):
                copy_q.append((idx, points.get(idx)))
        else:
            card_idx, card_points = copy_q.popleft()
            scratch_cards += 1

            for idx in range(card_idx + 1, card_idx + card_points + 1):
                copy_q.append((idx, points.get(idx)))

    return scratch_cards


if __name__ == "__main__":
    with open("4.in") as f:
        file_content = f.read()
        print(part_one_solution(file_content))
        print(part_two_solution(file_content))
