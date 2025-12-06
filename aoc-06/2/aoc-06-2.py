import math

with open("./inputs/aoc-06-1.txt") as f_:
    operations = [list(row.strip("\n")) for row in f_.readlines()]

ops = list(zip(*operations))
# print(ops)

full_operations = []
acc = []
for op in ops:
    if all(" " == x for x in op):
        f = sum if acc[0][-1] == "+" else math.prod
        temp = {f: [int("".join(o[:-1])) for o in acc]}
        full_operations.append(temp)
        acc = []
    else:
        acc.append(op)

f = sum if acc[0][-1] == "+" else math.prod
temp = {f: [int("".join(o[:-1])) for o in acc]}
full_operations.append(temp)

# print(full_operations)

print(sum(k(v) for d in full_operations for k, v in d.items()))
