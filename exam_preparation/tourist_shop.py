budget = float(input())
spend_money = 0
products_name = input()
is_higher = False
products_count = 0

while products_name != 'Stop':
    product_price = float(input())
    products_count += 1
    if products_count % 3 ==0:
        product_price *= 0.5
    if product_price > budget:
        is_higher = True
        budget -= product_price
        products_count -= 1
        break
    budget -= product_price
    spend_money += product_price
    products_name = input()

if is_higher:
    print(f"You don't have enough money!")
    print(f"You need {abs(budget):.2f} leva!")
else:
    print(f"You bought {products_count} products for {spend_money:.2f} leva.")