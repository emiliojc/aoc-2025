# with open("./inputs/aoc-01-1-t.txt") as f_:
with open("./inputs/aoc-01-1.txt") as f_:
    instructions = [(line[0], int(line[1:].strip())) for line in f_.readlines()]

# print(f"{instructions = }")


def cleanup_rotations(n: int) -> tuple[int, int]:
    full_rotations = n // 100
    n = n % 100

    return n, full_rotations


def turn_left(current_value: int, n: int) -> tuple[int, int]:
    n, full_rotations = cleanup_rotations(n)
    tmp = current_value - n

    if tmp <= 0 and current_value != 0:
        full_rotations += 1

    if tmp < 0:
        tmp += 100

    # print(f"{tmp, full_rotations = }")
    return tmp, full_rotations


def turn_right(current_value: int, n: int) -> int:
    n, full_rotations = cleanup_rotations(n)
    tmp = current_value + n

    if tmp > 99:
        full_rotations += 1
        tmp -= 100

    # print(f"{tmp, full_rotations = }")
    return tmp, full_rotations


current = 50
zero_counter = 0
for op, n in instructions:
    # print(f"{current, op, n = }")
    match op:
        case "L":
            current, tmp_zero = turn_left(current, n)
        case "R":
            current, tmp_zero = turn_right(current, n)
        case _:
            print("something went wrong")

    zero_counter += tmp_zero

print(f"{zero_counter = }")
