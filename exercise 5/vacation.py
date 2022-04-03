needed_money_for_vacation = float(input())
money_have = float(input())
day_count = 0
spend_days_count = 0
have_enough_money = False
spend_too_much = False

while have_enough_money != True or spend_too_much != True:
    action = input()
    money_count = float(input())
    day_count += 1
    if action == 'spend':
        spend_days_count += 1
        money_have -= money_count
        if money_have < 0:
            money_have = 0
        if spend_days_count == 5:
            spend_too_much = True
            break
    elif action == 'save':
        spend_days_count = 0
        money_have += money_count
        if money_have >= needed_money_for_vacation:
            have_enough_money = True
            break
        else:
            continue

if have_enough_money == True:
    print(f"You saved the money for {day_count} days.")
elif spend_too_much == True:
    print("You can't save the money.")
    print(f"{day_count}")

