age = int(input())
washing = float(input())
toy_price = int(input())

toy_numbers = 0
money_rising = -1
total_money_gain = 0

for age in range(1,age+1):
    if age % 2 != 0:
        toy_numbers += 1
    if age % 2 == 0:
        money_rising += 10
        total_money_gain += money_rising

total_toy_money_gain = toy_price * toy_numbers
sum = total_toy_money_gain + total_money_gain

if sum >= washing:
    print(f"Yes! {sum-washing:.2f}" )
else:
    print(f"No! {abs(sum-washing):.2f}")
