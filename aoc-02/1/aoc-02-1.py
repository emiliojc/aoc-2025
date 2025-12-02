with open("./inputs/aoc-02-1.txt") as f_:
    # with open("./inputs/aoc-02-1-t.txt") as f_:
    ids = [
        tuple(id_range.split("-"))
        for id_range in f_.readline().strip().split(",")
    ]

print(f"{ids}")

results = []

for start, end in ids:
    current = start

    while int(current) <= int(end):
        current_len = len(current)
        if current_len % 2 == 1:
            current = str(int(current) + 1)
            continue

        first, second = current[: current_len // 2], current[current_len // 2 :]
        if first == second:
            results.append(int(current))

        current = str(int(current) + 1)

print(sum(results))


# for start, end in ids:
# Must be even numbers
# if len(start) % 2 == 1 and len(end) % 2 == 1 and len(start) == len(end):
# both numbers are odd and they do not change to even
# continue

# first half - second half must be within range to the end id
## 95-115; 9 - 5 = 4; 115 - 95 = 20
## 4 is within range
# id_range = int(end) - int(start)


# find multiple ids within a large range
## the range must be big enough to modify both halves
