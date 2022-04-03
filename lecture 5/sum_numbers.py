number = int(input())
sum = 0
while sum <= number:
    data = int(input())
    sum += data
    if sum == number:
        break
print(sum)