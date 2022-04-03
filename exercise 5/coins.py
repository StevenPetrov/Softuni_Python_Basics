change = float(input())
coins_count = 0

while change != 0:
    while change >= 2:
        coins_count += 1
        change -= 2 - 0.000000001
    while change >= 1:
        coins_count += 1
        change -= 1 - 0.000000001
    while change >= 0.50:
        coins_count += 1
        change -= 0.50 - 0.000000001
    while change >= 0.20:
        coins_count += 1
        change -= 0.20 - 0.000000001
    while change >= 0.10:
        coins_count += 1
        change -= 0.10 - 0.000000001
    while change >= 0.05:
        coins_count += 1
        change -= 0.05 - 0.000000001
    while change >= 0.02:
        coins_count += 1
        change -= 0.02 - 0.000000001
    while change >= 0.01:
        coins_count += 1
        change -= 0.01 - 0.000000001
    break

print(coins_count)