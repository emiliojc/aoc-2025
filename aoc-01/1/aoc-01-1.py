with open("./inputs/aoc-01-1.txt") as f_:
    instructions = [(line[0], int(line[1:].strip())) for line in f_.readlines()]

# print(f"{instructions = }")


def turn_left(current_value: int, n: int) -> int:
    n = n % 100
    tmp = current_value - n
    return 100 + tmp if tmp < 0 else tmp


def turn_right(current_value: int, n: int) -> int:
    n = n % 100
    tmp = current_value + n
    # print(f"{current, n, tmp =}")
    return tmp - 100 if tmp > 99 else tmp


current = 50
zero_counter = 0
for op, n in instructions:
    # print(f"{current, op, n = }")
    match op:
        case "L":
            current = turn_left(current, n)
        case "R":
            current = turn_right(current, n)
        case _:
            print("something went wrong")

    if current == 0:
        zero_counter += 1

print(f"{zero_counter = }")
