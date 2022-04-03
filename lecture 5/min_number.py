min = 9999999

while True:
    number = input()
    if number == 'Stop':
                break
    else:
            if int(number) < min:
                min = int(number)
print(min)