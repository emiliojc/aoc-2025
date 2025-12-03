with open("./inputs/aoc-03-1.txt") as f_:
    banks = [l.strip() for l in f_.readlines()]

# print(banks)

enabled_batteries = []
for bank in banks:
    first_digit, first_idx = "0", "0"
    for idx, n in enumerate(bank[:-1]):
        if n > first_digit:
            first_digit, first_idx = n, idx

    second_digit = "0"
    for n in bank[first_idx + 1 :]:
        if n > second_digit:
            second_digit = n

    enabled_batteries.append(int(f"{first_digit}{second_digit}"))

print(sum(enabled_batteries))
