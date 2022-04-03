travel_price = float(input())
order_puzzle = int(input())
order_doll = int(input())
order_bear = int(input())
order_minion = int(input())
order_truck = int(input())

puzzle = 2.60 * order_puzzle
doll = 3 * order_doll
bear = 4.10 * order_bear
minion = 8.20 * order_minion
truck = 2 * order_truck
#left_amount = 0

order_sum = puzzle + doll + bear + minion + truck
order_count = order_puzzle + order_doll + order_bear + order_minion + order_truck

if order_count >= 50:
    discount = order_sum * 0.25
else:
    discount = 0

rent = (order_sum - discount) * 0.1

gain_money = order_sum - rent - discount

if gain_money >= travel_price:
    print(f"Yes! {abs(gain_money-travel_price):.2f} lv left.")
else:
    print(f"Not enough money! {abs(gain_money-travel_price):.2f} lv needed.")


















#total_number_orders = order_truck + order_bear + order_doll + order_minion + order_puzzle
#
#total_sum = puzzle + doll + bear + minion + truck
#
#if total_number_orders >= 50:
#    discount = total_sum * 0.25
#else:
#    discount = 0
#
#left_amount_before_rent_and_travel_price = total_sum - discount
#rent = left_amount_before_rent_and_travel_price * 0.1
#
#left_amount_before_travel_price = left_amount_before_rent_and_travel_price - rent
#
#left_amount = left_amount_before_travel_price - travel_price
#
#
#if left_amount >= travel_price:
#   print(f"Yes! {left_amount:.2f} lv left.")
#elif left_amount < travel_price:
#    not_enough_money = travel_price - left_amount_before_travel_price
#    print(f"Not enough money! {not_enough_money:.2f} lv needed.")


