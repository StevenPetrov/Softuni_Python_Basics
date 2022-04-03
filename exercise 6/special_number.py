n = input()

for current_number in range(1111,9999+1):
    for current_digit in str(current_number):
        special = True
        if int(current_digit) == 0 or int(n) % int(current_digit) != 0:
            special = False
            break
    if special:
        print(current_number, end=' ')
