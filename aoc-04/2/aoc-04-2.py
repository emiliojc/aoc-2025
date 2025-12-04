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


def roll_paper_mover(roll_paper_map: list[list[str]]) -> list[tuple[int, int]]:
    max_rows = len(roll_paper_map)
    max_cols = len(roll_paper_map[0])

    result = []
    for i in range(max_rows):
        for j in range(max_cols):
            if roll_paper_map[i][j] != "@":
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

                if roll_paper_map[ti][tj] == "@":
                    neighbour_rolls += 1

            if neighbour_rolls < 4:
                result.append((i, j))

    return result


total_paper_moved = 0
while True:
    paper_to_remove = roll_paper_mover(p)
    if len(paper_to_remove) == 0:
        break

    total_paper_moved += len(paper_to_remove)

    for i, j in paper_to_remove:
        p[i][j] = "x"

print(total_paper_moved)
