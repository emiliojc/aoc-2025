with open("./inputs/aoc-03-1.txt") as f_:
    banks = [l.strip() for l in f_.readlines()]

# print(banks)

enabled_batteries = []

for bank in banks:
    bank = list(bank)
    battery = bank[-12:]

    start, end = 0, -12
    current_pos = 0
    while True:
        # print(start, end)
        bounded_bank = bank[start:end]
        if not bounded_bank:
            break
        # print(bounded_bank)
        # print(battery)
        biggest_rest = max(bounded_bank)
        if biggest_rest < battery[current_pos]:
            # no bigger battery left
            break

        idx = bounded_bank.index(biggest_rest)
        battery[current_pos] = biggest_rest
        start += idx + 1
        current_pos += 1
        end += 1

    # print("".join(battery), len(battery))
    enabled_batteries.append(int("".join(battery)))


print(sum(enabled_batteries))


# bank = list(bank[::-2])
# for n in range(8, 0, -1):
#     # doesn't work, we can find higher numbers too early
#     n = str(n)
#     while n in bank:
#         if len(battery) == 11:
#             # the battery is complete
#             break
#         try:
#             # look for the n batteries for highest output
#             idx = bank.index(n)
#             battery.append((idx, n))
#             bank[idx] = -1
#         except ValueError:
#             # no more n battery in the bank
#             break
# battery.sort(key=lambda n: -n[0])
