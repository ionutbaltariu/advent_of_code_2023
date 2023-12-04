def part_one_solution(text: str) -> int:
    s = 0
    for line in text.split("\n"):
        _, after_two_points = line.split(":")
        before_vertical, after_vertical = after_two_points.split("|")
        before_vertical = set(int(x) for x in before_vertical.strip().split(" ") if x != '')
        after_vertical = set(int(x) for x in after_vertical.strip().split(" ") if x != '')
        intersection = before_vertical.intersection(after_vertical)

        if (length := len(intersection)) > 0:
            s += pow(2, length - 1)

    return s


if __name__ == "__main__":
    with open("4.in") as f:
        print(part_one_solution(f.read()))
