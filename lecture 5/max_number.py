max = - 99999999999999999

while True:
    number = input()
    if number == 'Stop':
            break
    else:
            if max <= int(number):
                max = int(number)
print(max)