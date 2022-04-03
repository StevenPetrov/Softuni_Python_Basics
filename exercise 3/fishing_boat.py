budget = float(input())
season = input()
fishermans = float(input())

rent_of_ship = 0
discount = 0
additional_discount = 0

if season == 'Spring':
    rent_of_ship = 3000
elif season == 'Winter':
    rent_of_ship = 2600
elif season == 'Summer' or 'Autumn':
    rent_of_ship = 4200

if fishermans <= 6:
    discount = rent_of_ship * 0.1
elif fishermans <= 11:
    discount = rent_of_ship * 0.15
elif 12 <= fishermans:
    discount = rent_of_ship * 0.25

total_amount = rent_of_ship - discount

if fishermans % 2 == 0 and season != 'Autumn':
    additional_discount = total_amount * 0.05
else:
    pass

total_amount_with_all_discounts = total_amount - additional_discount
left_money = budget - total_amount_with_all_discounts

if left_money >= 0:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    left_money = abs(left_money)
    print(f"Not enough money! You need {left_money:.2f} leva.")
