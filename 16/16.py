from collections import deque

DIRS = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}


def traverse_grid(start, matrix):
    q = deque()
    q.append(start)
    visited = set()
    visited_nodes = set()
    energized = 0
    m, n = len(matrix), len(matrix[0])

    while q:
        # doesn't really matter if it's pop or popleft
        node = q.popleft()
        x, y, d_str = node
        # print("at", x, y)
        d = DIRS[d_str]
        next_node_x, next_node_y = x + d[0], y + d[1]

        if (x, y) not in visited_nodes:
            energized += 1
            visited_nodes.add((x, y))

        if next_node_x < 0 or next_node_x > m - 1:
            # print("will be of bounds x")
            continue

        if next_node_y < 0 or next_node_y > n - 1:
            # print("will be of bounds y")
            continue

        if (x, y, d_str) in visited:
            # print("already visited with same direction")
            continue

        visited.add((x, y, d_str))

        next_node_content = matrix[next_node_x][next_node_y]

        if next_node_content == ".":
            # keep direction
            q.append((next_node_x, next_node_y, d_str))
        # |
        elif next_node_content == "|" and d_str in {"L", "R"}:
            q.append((next_node_x, next_node_y, "U"))
            q.append((next_node_x, next_node_y, "D"))
        elif next_node_content == "|" and d_str in {"U", "D"}:
            q.append((next_node_x, next_node_y, d_str))
        # -
        elif next_node_content == "-" and d_str in {"U", "D"}:
            q.append((next_node_x, next_node_y, "L"))
            q.append((next_node_x, next_node_y, "R"))
        elif next_node_content == "-" and d_str in {"L", "R"}:
            q.append((next_node_x, next_node_y, d_str))
        # /
        elif next_node_content == "/" and d_str == "R":
            q.append((next_node_x, next_node_y, "U"))
        elif next_node_content == "/" and d_str == "L":
            q.append((next_node_x, next_node_y, "D"))
        elif next_node_content == "/" and d_str == "U":
            q.append((next_node_x, next_node_y, "R"))
        elif next_node_content == "/" and d_str == "D":
            q.append((next_node_x, next_node_y, "L"))
        # \
        elif next_node_content == "\\" and d_str == "R":
            q.append((next_node_x, next_node_y, "D"))
        elif next_node_content == "\\" and d_str == "L":
            q.append((next_node_x, next_node_y, "U"))
        elif next_node_content == "\\" and d_str == "U":
            q.append((next_node_x, next_node_y, "L"))
        elif next_node_content == "\\" and d_str == "D":
            q.append((next_node_x, next_node_y, "R"))

    # -1 (the start tile)
    return energized - 1


if __name__ == "__main__":
    file_handler = open("16.in", "r")
    matrix = file_handler.read().split("\n")
    file_handler.close()

    # part one
    energized_tiles = traverse_grid((0, -1, "R"), matrix)

    print("part one", energized_tiles)

    start_nodes = []
    m, n = len(matrix), len(matrix[0])

    # start from left
    for i in range(m):
        start_nodes.append((i, -1, "R"))

    # start from right
    for i in range(m):
        start_nodes.append((i, n, "L"))

    # start from above
    for j in range(n):
        start_nodes.append((-1, j, "D"))

    # start from below
    for j in range(n):
        start_nodes.append((m, j, "U"))

    # basically repeat the same algorithm for every possible start position
    energized_tiles = -1
    for node in start_nodes:
        energized_tiles = max(energized_tiles, traverse_grid(node, matrix))

    print("part two", energized_tiles)