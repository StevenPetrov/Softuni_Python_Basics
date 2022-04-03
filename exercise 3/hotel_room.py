month = input()
nights = int(input())

studio_total = 0
apartment_total = 0

if month == 'May' or month == 'October':
    studio_total = nights * 50
    if 7 < nights <= 14:
        studio_total *= 0.95
    elif nights > 14:
        studio_total *= 0.70
    apartment_total = nights * 65
    if nights > 14:
        apartment_total *= 0.90
elif month == 'June' or month == 'September':
    studio_total = nights * 75.20
    if nights > 14:
        studio_total *= 0.80
    apartment_total = nights * 68.70
    if nights > 14:
        apartment_total *= 0.90
elif month == 'July' or month == 'August':
    studio_total = nights * 76
    apartment_total = nights * 77
    if nights > 14:
        apartment_total *= 0.90

print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")