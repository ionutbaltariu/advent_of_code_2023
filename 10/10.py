from collections import deque
from copy import deepcopy

directions = {
    "|": {(-1, 0), (1, 0)},
    "-": {(0, -1), (0, 1)},
    "L": {(-1, 0), (0, 1)},
    "J": {(-1, 0), (0, -1)},
    "7": {(1, 0), (0, -1)},
    "F": {(1, 0), (0, 1)}
}


def manhattan_norm(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def get_next_moves(matrix, i, j, m, n):
    if matrix[i][j] == "S":
        possible_next_moves = set()
        if i != 0:
            if matrix[i-1][j] in {"|", "7", "F"}:
                possible_next_moves.add((-1, 0))
        if i != m - 1:
            if matrix[i+1][j] in {"|", "L", "J"}:
                possible_next_moves.add((1, 0))
        if j != 0:
            if matrix[i][j-1] in {"-", "L", "F"}:
                possible_next_moves.add((0, -1))
        if j != n - 1:
            if matrix[i][j+1] in {"-", "J", "7"}:
                possible_next_moves.add((0, 1))
        print("start", possible_next_moves)
    elif matrix[i][j] not in directions:
        return []
    else:
        possible_next_moves = directions[matrix[i][j]]
        if i == 0:
            possible_next_moves.discard((-1, 0))

        if j == 0:
            possible_next_moves.discard((0, -1))

        if i == m - 1:
            possible_next_moves.discard((1, 0))

        if j == n - 1:
            possible_next_moves.discard((0, 1))

    return [
        (i + x, j + y) for x, y in possible_next_moves
    ]


if __name__ == "__main__":
    matrix = []
    start_pos = None

    with open("10.in", "r") as f:
        for i, raw_line in enumerate(f.read().split("\n")):
            line = []
            for j, el in enumerate(raw_line):
                line.append(el)
                if el == "S":
                    start_pos = (i, j)
            matrix.append(line)

    # copy = deepcopy(matrix)
    visited = set()
    queue = deque()
    m, n = len(matrix), len(matrix[0])

    queue.append((start_pos, 0))
    max_dist = -1

    while queue:
        node, dist = queue.popleft()

        if node in visited:
            continue

        max_dist = max(dist, max_dist)
        visited.add(node)
        # copy[node[0]][node[1]] = "#"
        next_moves = get_next_moves(matrix, node[0], node[1], m, n)
        queue.extend([
            (move, dist + 1) for move in next_moves
        ])

    print(max_dist)
    # for line in copy:
    #     print(''.join(line))
