luggage_plus20_price = float(input())
luggage_kgs = int(input())
days = int(input())
number_of_luggages = int(input())

total = 0

if luggage_kgs < 10:
    total = luggage_plus20_price * 0.2
elif 10 <= luggage_kgs <= 20:
    total = luggage_plus20_price * 0.5
else:
    total = luggage_plus20_price

if days < 7:
    total += total * 0.4
elif 7 <= days <= 30:
    total += total * 0.15
else:
    total += total * 0.1

print(f"The total price of bags is: {total * number_of_luggages:.2f} lv. ")