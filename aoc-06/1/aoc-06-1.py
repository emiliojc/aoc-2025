import math

with open("./inputs/aoc-06-1.txt") as f_:
    operations = [list(row.strip().split()) for row in f_.readlines()]

# print(operations)

max_numbers = len(operations)
max_ops = len(operations[0])

results = []
for x in range(max_ops):
    op = sum if operations[-1][x] == "+" else math.prod

    results.append(op(int(operations[y][x]) for y in range(max_numbers - 1)))

print(sum(results))
