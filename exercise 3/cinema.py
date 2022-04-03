type_projection = input()
rows = int(input())
columns = int(input())
income = 0

if type_projection == 'Premiere':
    income = rows * columns * 12
    print(f'{income:.2f} leva')
elif type_projection == 'Normal':
    income = rows * columns * 7.50
    print(f'{income:.2f} leva')
else:
    income = rows * columns * 5
    print(f'{income:.2f} leva')
