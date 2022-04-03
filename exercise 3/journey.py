budget = float(input())
season = input()

destination = ''
type_of_vacation = ''
spend_money = 0

if budget <= 100:
    destination = 'Bulgaria'
elif 100 < budget <= 1000:
    destination = 'Balkans'
else:
    destination = 'Europe'

if destination == 'Europe':
    type_of_vacation = 'Hotel'
elif season == 'summer':
    type_of_vacation = 'Camp'
else:
    type_of_vacation = 'Hotel'

if budget <= 100 and season == 'summer':
    spend_money = budget * 0.3
elif budget <= 100 and season == 'winter':
    spend_money = budget * 0.7
elif 100 < budget <= 1000 and season == 'summer':
    spend_money = budget * 0.4
elif 100 < budget <= 1000 and season == 'winter':
    spend_money = budget * 0.8
else:
    spend_money = budget * 0.9

print(f"Somewhere in {destination}")
print(f'{type_of_vacation} - {spend_money:.2f}')
