product = input()

fruit = ('banana, apple, kiwi, cherry, lemon, grapes')
veggie = ('tomato, cucumber, pepper, carrot')

if product in fruit:
    print('fruit')
elif product in veggie:
    print('vegetable')
else:
    print('unknown')