import re

number_rgx = re.compile(r"\d+")


def get_adjacent(matrix, line, number_span):
    """
    ABCDE ABCD ABC
    FxxxG ExxF DxE
    HIJKL GHIJ FGH

    x{1,3} is the number, the others are the adjacent elements
    """
    all_adj_elements = []
    column_number = len(matrix[0])
    line_number = len(matrix)
    number_start, number_end = number_span

    # F / E / D
    if number_start > 0:
        all_adj_elements.append(matrix[line][number_start - 1])

    # G / F / E
    if number_end < column_number:
        all_adj_elements.append(matrix[line][number_end])

    # BCD / BC / B (top row adjacent elements
    if line > 0:
        for element in matrix[line - 1][number_start:number_end]:
            all_adj_elements.append(element)

    # IJK / HI / J
    if line < line_number - 1:
        for element in matrix[line + 1][number_start:number_end]:
            all_adj_elements.append(element)

    # A, E, H, L / A, D, G, J / A, C, F, H

    if line > 0 and number_start > 0:
        all_adj_elements.append(matrix[line - 1][number_start - 1])

    if line > 0 and number_end < column_number:
        all_adj_elements.append(matrix[line - 1][number_end])

    if line < line_number - 1 and number_start > 0:
        all_adj_elements.append(matrix[line + 1][number_start - 1])

    if line < line_number - 1 and number_end < column_number:
        all_adj_elements.append(matrix[line + 1][number_end])

    return all_adj_elements


def are_there_valid_symbols_in_adjacent_elements(elements):
    return len([x for x in elements if not x.isdigit() and x != '.']) > 0


def find_part_number_sum(text: str) -> int:
    matrix = [line for line in text.split("\n")]
    s = 0
    for line_idx, line in enumerate(matrix):
        number_match = number_rgx.search(line)

        if number_match:
            adjacent = get_adjacent(matrix, line_idx, number_match.span())
            if are_there_valid_symbols_in_adjacent_elements(adjacent):
                s += int(line[number_match.start():number_match.end()])
            # print(number_match)
            # print(adjacent)
            # print(are_there_valid_symbols_in_adjacent_elements(adjacent))

        while number_match:
            number_match = number_rgx.search(line, number_match.end())
            if number_match:
                adjacent = get_adjacent(matrix, line_idx, number_match.span())
                if are_there_valid_symbols_in_adjacent_elements(adjacent):
                    s += int(line[number_match.start():number_match.end()])
                # print(number_match)
                # print(adjacent)
                # print(are_there_valid_symbols_in_adjacent_elements(adjacent))

    return s


if __name__ == "__main__":
    with open("3.in") as f:
        print(find_part_number_sum(f.read()))
