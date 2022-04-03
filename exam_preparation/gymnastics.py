country = input()
type_exersice = input()
sum = 0
if country == 'Russia':
    if type_exersice == 'ribbon':
        sum += 9.1
        sum += 9.4
    elif type_exersice == 'hoop':
        sum += 9.3
        sum += 9.8
    else:
        sum += 9.6
        sum += 9.0
elif country == 'Bulgaria':
    if type_exersice == 'ribbon':
        sum += 9.6
        sum += 9.4
    elif type_exersice == 'hoop':
        sum += 9.55
        sum += 9.750
    else:
        sum += 9.5
        sum += 9.4
elif country == 'Italy':
    if type_exersice == 'ribbon':
        sum += 9.2
        sum += 9.5
    elif type_exersice == 'hoop':
        sum += 9.45
        sum += 9.35
    else:
        sum += 9.7
        sum += 9.15

diff = (20 - sum)
diff_persent = diff / 20 * 100

print(f"The team of {country} get {sum:.3f} on {type_exersice}.")
print(f"{diff_persent:.2f}%")