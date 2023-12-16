if __name__ == "__main__":
    handler = open("14.in", "r")
    lines = handler.read().split("\n")
    columns = len(lines[0])
    lines_number = len(lines)

    cube_rocks = {
        i: [] for i in range(columns)
    }

    for idx, line in enumerate(lines):
        for jdx, c in enumerate(line):
            if c == "#":
                cube_rocks[jdx].append(idx)

    rock_movements = {}
    load = 0

    for idx, line in enumerate(lines):
        for jdx, c in enumerate(line):
            if c == "O":
                cube_rocks_on_column = cube_rocks[jdx]

                cubes_over_current_rock = [x for x in cube_rocks_on_column if x < idx]

                if len(cubes_over_current_rock) == 0:
                    print(f"{idx}, {jdx} could go to 0, {jdx}")
                    rock_movements[f"0,{jdx}"] = rock_movements.get(f"0,{jdx}", 0) + 1
                else:
                    first_cube_over_rock = cubes_over_current_rock[-1]
                    print(f"{idx}, {jdx} could go to {first_cube_over_rock + 1}, {jdx}")
                    rock_movements[f"{first_cube_over_rock + 1},{jdx}"] = rock_movements.get(f"{first_cube_over_rock + 1},{jdx}", 0) + 1
    print(rock_movements)

    load = 0
    for position, count in rock_movements.items():
        x, y = [int(x) for x in position.split(",")]

        for i in range(count):
            current_load = lines_number - (x + i)
            print(f"{x + i}, {y} with load {current_load}")
            load += current_load

    print(load)