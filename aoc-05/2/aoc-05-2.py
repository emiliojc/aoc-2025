with open("./inputs/aoc-05-1.txt") as f_:
    fresh_id_ranges = []

    for line in f_.readlines():
        line = line.strip()

        if "-" in line:
            fresh_id_ranges.append(tuple(int(n) for n in line.split("-")))
        else:
            break

print(f"{len(fresh_id_ranges) = }")
fresh_id_ranges.sort()
final_ranges = []
while fresh_id_ranges:
    print(f"{len(final_ranges) = }")
    # print(f"{final_ranges = }")
    print(f"{len(fresh_id_ranges) = }")
    # print(f"{fresh_id_ranges = }")
    start, end = fresh_id_ranges.pop()
    if not final_ranges:
        final_ranges.append((start, end))
        continue

    tmp = []
    while final_ranges:
        start_, end_ = final_ranges.pop()

        if start_ <= start <= end_:
            # partial overlap or total overlap from new range
            new_start = start_
            if end <= end_:
                new_end = end_
            else:
                new_end = end

            # new range to reevaluate
            fresh_id_ranges.append((new_start, new_end))
            break
        elif start_ <= end <= end_:
            # partial overlap from below
            new_end = end_
            # for start we know already it must be lower than start_
            new_start = start

            # new range to reevaluate
            fresh_id_ranges.append((new_start, new_end))
            break
        elif start < start_ and end > end_:
            # the range is contained in the new one.
            new_start = start
            new_end = end

            # new range to reevaluate
            fresh_id_ranges.append((new_start, new_end))
            break
        elif end_ + 1 == start:
            # consecutive ids
            new_start = start_
            new_end = end

            # new range to reevaluate
            fresh_id_ranges.append((new_start, new_end))
            break
        else:
            # new range
            tmp.append((start_, end_))
            if not final_ranges:
                tmp.append((start, end))
    final_ranges = tmp + final_ranges

print("*" * 50)
print(f"{final_ranges = }")
print(f"{len(final_ranges) = }")
print(f"{sum(b - a for a, b in final_ranges) + len(final_ranges) = }")

# fresh_ingredients_ids = {
#     n for start, end in fresh_id_ranges for n in range(start, end + 1)
# }

# print(len(fresh_ingredients_ids))
