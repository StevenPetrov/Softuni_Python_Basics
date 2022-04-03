budget = float(input())
statists = int(input())
clothes_per_statists = float(input())

total_price_clothes = statists * clothes_per_statists

decorate = budget * 0.1

if statists > 150:
    total_price_clothes -= total_price_clothes * 0.1

total_cost = decorate + total_price_clothes

if total_cost > budget:
    print("Not enough money!")
    needed_money = total_cost - budget
    print(f"Wingard needs {needed_money:.2f} leva more.")
elif total_cost <= budget:
    print("Action!")
    left_money = (budget - total_cost)
    print(f"Wingard starts filming with {left_money:.2f} leva left.")