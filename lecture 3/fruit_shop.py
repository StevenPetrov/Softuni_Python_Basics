product = input()
weekday = input()
quantity = float(input())

fruit = ('banana / apple / orange / grapefruit / kiwi / pineapple / grapes')
monfri = ('Monday / Tuesday / Wednesday / Thursday / Friday ')
weekend = ('Saturday / Sunday')

if weekday in monfri:
    if product in fruit:
        if product == 'banana':
            print(f'{quantity * 2.50:.2f}')
        elif product == 'apple':
            print(f'{quantity * 1.20:.2f}')
        elif product == 'orange':
            print(f'{quantity * 0.85:.2f}')
        elif product == 'grapefruit':
            print(f'{quantity * 1.45:.2f}')
        elif product == 'kiwi':
            print(f'{quantity * 2.70:.2f}')
        elif product == 'pineapple':
            print(f'{quantity * 5.50:.2f}')
        elif product == 'grapes':
            print(f'{quantity * 3.85:.2f}')
    else:
        print('error')
elif weekday in weekend:
    if product in fruit:
        if product == 'banana':
            print(f'{quantity * 2.70:.2f}')
        elif product == 'apple':
            print(f'{quantity * 1.25:.2f}')
        elif product == 'orange':
            print(f'{quantity * 0.90:.2f}')
        elif product == 'grapefruit':
            print(f'{quantity * 1.60:.2f}')
        elif product == 'kiwi':
            print(f'{quantity * 3.00:.2f}')
        elif product == 'pineapple':
            print(f'{quantity * 5.60:.2f}')
        elif product == 'grapes':
            print(f'{quantity * 4.20:.2f}')
    else:
        print('error')
else:
    print('error')