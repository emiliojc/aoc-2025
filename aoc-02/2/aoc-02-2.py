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
        # I need to check which divisors the whole number have to equally divide it
        current_len = len(current)
        if current_len < 2:
            # At least we need 2 digits
            current = str(int(current) + 1)
            continue
        divisors = [n for n in range(1, current_len) if current_len % n == 0]

        # now we need to split the number in the divisor chunks and make sure all of them are equal
        is_false_id = False
        for d in divisors:
            from itertools import batched

            buckets = list(batched(current, d))
            x = buckets[0]
            if all(x == a for a in buckets):
                is_false_id = True
                break

        if is_false_id:
            results.append(int(current))

        current = str(int(current) + 1)

print(sum(results))
