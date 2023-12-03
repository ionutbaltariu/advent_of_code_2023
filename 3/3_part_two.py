import re

number_rgx = re.compile(r"\d+")
adjacency_table = {}


def is_valid_symbol(s: str):
    return s == "*"


def alter_adj_table(matrix, line, number_span):
    """
    ABCDE ABCD ABC
    FxxxG ExxF DxE
    HIJKL GHIJ FGH

    x{1,3} is the number, the others are the adjacent elements
    """
    # encode x_y_s

    all_adj_elements = []
    column_number = len(matrix[0])
    line_number = len(matrix)
    number_start, number_end = number_span
    number = matrix[line][number_start:number_end]

    # F / E / D
    if number_start > 0:
        c = matrix[line][number_start - 1]
        encoding = f"{line}_{number_start - 1}_{c}"
        add_in_adj_table(c, encoding, number)

    # G / F / E
    if number_end < column_number:
        c = matrix[line][number_end]
        encoding = f"{line}_{number_end}_{c}"
        add_in_adj_table(c, encoding, number)

    # BCD / BC / B (top row adjacent elements
    if line > 0:
        for idx, element in enumerate(matrix[line - 1][number_start:number_end]):
            encoding = f"{line - 1}_{number_start + idx}_{element}"
            add_in_adj_table(element, encoding, number)

    # IJK / HI / J
    if line < line_number - 1:
        for idx, element in enumerate(matrix[line + 1][number_start:number_end]):
            encoding = f"{line + 1}_{number_start + idx}_{element}"
            add_in_adj_table(element, encoding, number)
    # A, E, H, L / A, D, G, J / A, C, F, H

    if line > 0 and number_start > 0:
        c = matrix[line - 1][number_start - 1]
        encoding = f"{line - 1}_{number_start - 1}_{c}"
        add_in_adj_table(c, encoding, number)

    if line > 0 and number_end < column_number:
        c = matrix[line - 1][number_end]
        encoding = f"{line - 1}_{number_end}_{c}"
        add_in_adj_table(c, encoding, number)

    if line < line_number - 1 and number_start > 0:
        c = matrix[line + 1][number_start - 1]
        encoding = f"{line + 1}_{number_start - 1}_{c}"
        add_in_adj_table(c, encoding, number)

    if line < line_number - 1 and number_end < column_number:
        c = matrix[line + 1][number_end]
        encoding = f"{line + 1}_{number_end}_{c}"
        add_in_adj_table(c, encoding, number)


def add_in_adj_table(c, encoding, number):
    if is_valid_symbol(c):
        if encoding in adjacency_table:
            adjacency_table[encoding].add(number)
        else:
            adjacency_table[encoding] = {number}


def find_part_number_sum(text: str) -> int:
    matrix = [line for line in text.split("\n")]
    s = 0
    for line_idx, line in enumerate(matrix):
        number_match = number_rgx.search(line)

        if number_match:
            alter_adj_table(matrix, line_idx, number_match.span())

        while number_match:
            number_match = number_rgx.search(line, number_match.end())
            if number_match:
                alter_adj_table(matrix, line_idx, number_match.span())

    for gears in adjacency_table.values():
        if len(gears) == 2:
            x, y = gears
            s += int(x) * int(y)

    return s


if __name__ == "__main__":
    with open("3.in") as f:
        print(find_part_number_sum(f.read()))
