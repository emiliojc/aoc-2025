coords = [
    # (0, 0),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]

with open("./inputs/aoc-04-1.txt") as f_:
    p = [list(l.strip()) for l in f_.readlines()]

# print(p)

max_rows = len(p)
max_cols = len(p[0])

result = 0
for i in range(max_rows):
    for j in range(max_cols):
        if p[i][j] != "@":
            # not a paperoll
            continue

        neighbour_rolls = 0
        for coord_i, coord_j in coords:
            ti, tj = i + coord_i, j + coord_j

            if ti < 0 or ti >= max_rows:
                # out of bounds
                continue

            if tj < 0 or tj >= max_cols:
                # out of bounds
                continue

            if p[ti][tj] == "@":
                neighbour_rolls += 1

        if neighbour_rolls < 4:
            result += 1

print(result)
