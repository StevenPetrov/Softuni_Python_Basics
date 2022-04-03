days = int(input())
hours = int(input())
park_tax_per_day = 0
total = 0

for x in range(1,days+1):
    for y in range(1,hours+1):
        if x % 2 == 0 and y % 2 != 0:
            park_tax_per_day += 2.50
        elif x % 2 != 0 and y % 2 == 0:
            park_tax_per_day += 1.25
        else:
            park_tax_per_day += 1
    print(f"Day: {x} - {park_tax_per_day:.2f} leva")
    total += park_tax_per_day
    park_tax_per_day = 0
print(f"Total: {total:.2f} leva")
