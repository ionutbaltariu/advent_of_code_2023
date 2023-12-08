import re

parse_rgx = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")

if __name__ == "__main__":
    handler = open("8.in")
    moves = handler.readline()

    map_dictionary = {}

    for line in handler.read().split("\n")[1:]:
        node, left, right = re.findall(parse_rgx, line)[0]
        map_dictionary[node] = (left, right)

    node = "AAA"

    i = 0
    length = len(moves)
    total_steps = 0
    print("Part ONE")

    ending_in_a = []
    while True:
        print(f"[DBG] At node {node}")

        if node == "ZZZ":
            print(f"End reached in {total_steps} steps! ")
            break

        step = moves[i]
        i = (i + 1) % (length - 1)
        total_steps += 1

        idx = 0 if step == "L" else 1
        print(f"[DBG] Taking step {'L' if idx == 0 else 'R'}")
        node = map_dictionary[node][idx]