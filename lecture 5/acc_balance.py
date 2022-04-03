balance = 0
add = ''

while True:
    add = input()
    if add == 'NoMoreMoney':
        break
    if float(add) > 0:
        balance += float(add)
        print(f"Increase: {float(add):.2f}")
    else:
        print("Invalid operation!")
        break
print(f"Total: {balance:.2f}")