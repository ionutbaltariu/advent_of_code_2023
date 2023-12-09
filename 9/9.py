if __name__ == "__main__":
    with open("9.in", "r") as f:
        back_sum = 0
        front_sum = 0

        for line in f.read().split("\n"):
            numbers = [int(x) for x in line.split()]
            triangle = [numbers]
            all_zeros = False
            current_back_sum = numbers[-1]

            # part 1 and triangle forming
            while not all_zeros:
                numbers = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
                triangle.append(numbers)
                all_zeros = all([x == 0 for x in numbers])
                current_back_sum += numbers[-1]

            back_sum += current_back_sum
            left_val = 0

            # part 2
            for value in triangle[-2::-1]:
                left_val = value[0] - left_val
            front_sum += left_val

        print(back_sum)
        print(front_sum)
