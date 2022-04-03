n = int(input())
salary = int(input())

for n in range(n):
    tabs = input()
    if tabs == 'Facebook':
        salary -= 150
    if tabs == 'Instagram':
        salary -= 100
    if tabs == 'Reddit':
        salary -= 50

if salary <= 0:
    print("You have lost your salary." )
else:
    print(f'{salary}')

