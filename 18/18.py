from math import ceil

DIRS = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}


def get_total_area(points):
    # using shoelace theorem
    # it returns the value of the area in a polygon described by any given number of points
    # https://artofproblemsolving.com/wiki/index.php/Shoelace_Theorem
    num_of_points = len(points)
    member1_sum = 0
    for i in range(num_of_points - 1):
        x = points[i % num_of_points][0]
        y = points[(i + 1) % num_of_points][1]
        member1_sum += x * y

    member2_sum = 0
    for i in range(num_of_points - 1):
        y = points[i % num_of_points][1]
        x = points[(i + 1) % num_of_points][0]
        member2_sum += x * y

    # abs(member1_sum - member2_sum) / 2 is the shoelace formula
    # while ceil(num_of_points / 2) is ???, just figured that if you add it to the result you get the correct answer
    # TODO: research why it needs to be added
    return abs(member1_sum - member2_sum) / 2 + ceil(num_of_points / 2)


def get_part_two_color(number: int) -> str:
    match number:
        case 0:
            return "R"
        case 1:
            return "D"
        case 2:
            return "L"
        case 3:
            return "U"


if __name__ == "__main__":
    file_handler = open("18.in", "r")
    lines = file_handler.read().split("\n")

    moves = []
    for line in lines:
        moves.append(line.split(" "))

    points_part_one = [(0, 0)]
    points_part_two = [(0, 0)]
    for move in moves:
        direction, steps, color = move
        dir_coords_part_1 = DIRS[direction]

        steps_from_color = int(color[2:-2], 16)
        part_two_dir = get_part_two_color(int(color[-2]))
        dir_coords_part_2 = DIRS[part_two_dir]
        # print(part_two_dir, steps_from_color)

        for _ in range(int(steps)):
            last_point = points_part_one[-1]
            points_part_one.append(
                (last_point[0] + dir_coords_part_1[0], last_point[1] + dir_coords_part_1[1]))

        for _ in range(int(steps_from_color)):
            last_point = points_part_two[-1]
            points_part_two.append((last_point[0] + dir_coords_part_2[0], last_point[1] + dir_coords_part_2[1]))

    # part one
    print("Part one", get_total_area(points_part_one))
    print("Part two", get_total_area(points_part_two))
