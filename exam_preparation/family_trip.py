budget = float(input())
nights = int(input())
price_per_night = float(input())
add_tax = int(input())


if nights > 7:
    price_per_night *= 0.95

expenses = nights * price_per_night

expenses += budget * (add_tax / 100)
left_money = abs(budget-expenses)

if budget >= expenses:
    print(f"Ivanovi will be left with {left_money:.2f} leva after vacation.")
else:
    print(f"{left_money:.2f} leva needed.")
