with open("./inputs/aoc-05-1.txt") as f_:
    fresh_id_ranges = []
    available_ids = []

    current_populating = fresh_id_ranges
    for line in f_.readlines():
        line = line.strip()

        if "-" in line:
            fresh_id_ranges.append(tuple(int(n) for n in line.split("-")))
        elif line:
            available_ids.append(int(line))


print(f"{fresh_id_ranges =}")
print(f"{available_ids =}")

total_fresh = 0
for id in available_ids:
    for start, end in fresh_id_ranges:
        if start <= id <= end:
            total_fresh += 1
            break

print(total_fresh)
