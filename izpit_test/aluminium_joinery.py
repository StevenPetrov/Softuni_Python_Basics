number_of_windows = int(input())
type = input()
delivery = input()
total = 0

if number_of_windows < 10:
    print("Invalid order")

else:
    if type == '90X130':
        total = number_of_windows * 110
        if 60 >= number_of_windows > 30:
            total *= 0.95
        elif number_of_windows > 60:
            total *= 0.92
    elif type == '100X150':
        total = number_of_windows * 140
        if 80 >= number_of_windows > 40:
            total *= 0.94
        elif number_of_windows > 80:
            total *= 0.9
    elif type == '130X180':
        total = number_of_windows * 190
        if 50 >= number_of_windows > 20:
            total *= 0.93
        elif number_of_windows > 50:
            total *= 0.88
    elif type == '200X300':
        total = number_of_windows * 250
        if 50 >= number_of_windows > 25:
            total *= 0.91
        elif number_of_windows > 50:
            total *= 0.86
    if delivery == "With delivery":
        total = total + 60
    if number_of_windows > 99:
        total *= 0.96
    print(f'{total:.2f} BGN')
