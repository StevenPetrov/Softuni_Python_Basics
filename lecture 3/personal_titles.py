age = float(input())
type = input()

if type == 'f':
    if age >= 16:
        print('Ms.')
    if age < 16:
        print('Miss')
elif type == 'm':
    if age >= 16:
        print('Mr.')
    if age < 16:
        print('Master')