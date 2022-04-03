flowers = input()
number_of_flowers = int(input())
budget = int(input())

total_price = 0

if flowers == "Roses":
    total_price = number_of_flowers * 5
elif flowers == "Dahlias":
    total_price = number_of_flowers * 3.80
elif flowers == "Tulips":
    total_price = number_of_flowers * 2.80
elif flowers == "Narcissus":
    total_price = number_of_flowers * 3
elif flowers == "Gladiolus":
    total_price = number_of_flowers * 2.50

discount = 0

if number_of_flowers > 80 and flowers == 'Roses':
    discount = total_price * 0.1
elif number_of_flowers > 90 and flowers == 'Dahlias':
    discount = total_price * 0.15
elif number_of_flowers > 80 and flowers == 'Tulips':
    discount = total_price * 0.15
elif number_of_flowers < 120 and flowers == 'Narcissus':
    discount = (-total_price * 0.15)
elif number_of_flowers < 80 and flowers == 'Gladiolus':
    discount = (-total_price * 0.20)

left_amount = (budget + discount) - total_price

if left_amount >= 0:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers} and {left_amount:.2f} leva left.")
if left_amount < 0:
    left_amount = abs(left_amount)
    print(f"Not enough money, you need {left_amount:.2f} leva more.")
