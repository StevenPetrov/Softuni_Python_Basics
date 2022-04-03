days = int(input())
type_of_room = input()
rate = input()

total = 0

if type_of_room == 'room for one person':
    total = (days - 1) * 18
elif type_of_room == 'apartment':
    total = (days - 1) * 25
elif type_of_room == 'president apartment':
    total = (days - 1) * 35

discount = 0

if type_of_room == 'apartment':
    if days < 10:
        discount = total * 0.3
    elif 10 <= days <= 15:
        discount = total * 0.35
    else:
        discount = total * 0.5
elif type_of_room == 'president apartment':
    if days < 10:
        discount = total * 0.1
    elif 10 <= days <= 15:
        discount = total * 0.15
    else:
        discount = total * 0.2

total_with_discount = float(total - discount)

if rate == 'positive':
    total_with_discount = total_with_discount + (total_with_discount * 0.25)
elif rate == 'negative':
    total_with_discount = total_with_discount - (total_with_discount * 0.10)

print(f'{total_with_discount:.2f}')
