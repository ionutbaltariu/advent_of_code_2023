import numpy as np

# each line transforms into a million lines therefore the multiplier (the number of lines to add to the coordinates
# is 1 mil - 1 (that line, because it already exists))
PART_TWO_MULTIPLIER = 999999


def get_sum_of_shortest_paths(matrix, lines_without_sharp, columns_without_sharp, multiplier=1):
    galaxies = []
    # instead of manipulating the matrix, count how many lines and columns should be added
    # that's basically the number of lines and columns that are before the current one
    # multiplied by the expansion factor
    for idx, line in enumerate(matrix):
        for jdx, element in enumerate(line):
            if element == "#":
                empty_lines_before = len([x for x in lines_without_sharp if idx > x])
                empty_columns_before = len([x for x in columns_without_sharp if jdx > x])
                galaxies.append(
                    (
                        idx + empty_lines_before * multiplier,
                        jdx + empty_columns_before * multiplier
                    )
                )
    s = 0
    # shortest distance is basically the manhattan distance between the two
    for i in range(len(galaxies)):
        for j in range(i, len(galaxies)):
            p1 = galaxies[i]
            p2 = galaxies[j]
            manhattan_distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            s += manhattan_distance

    return s


def get_matrix_and_lines_and_columns_without_sharp(file):
    matrix = []
    lines_without_sharp, columns_without_sharp = [], []

    for idx, line in enumerate(file.read().split("\n")):
        sharp_found = False
        line_arr = []

        for element in line:
            if element == "#":
                sharp_found = True
            line_arr.append(element)

        matrix.append(line_arr)

        if not sharp_found:
            lines_without_sharp.append(idx)

    m = len(matrix)
    n = len(matrix[0])

    for i in range(n):
        found_sharp = False
        for j in range(m):
            if matrix[j][i] == "#":
                found_sharp = True
                break
        if not found_sharp:
            columns_without_sharp.append(i)

    return matrix, lines_without_sharp, columns_without_sharp


def solve():
    f = open("10.in", "r")
    matrix, lines_without_sharp, columns_without_sharp = get_matrix_and_lines_and_columns_without_sharp(f)
    print(f"Part one: {get_sum_of_shortest_paths(matrix, lines_without_sharp, columns_without_sharp)}")
    print(f"Part two: {get_sum_of_shortest_paths(matrix, lines_without_sharp, columns_without_sharp, PART_TWO_MULTIPLIER)}")
    f.close()


if __name__ == "__main__":
    solve()