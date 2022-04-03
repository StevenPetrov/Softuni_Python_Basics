n = int(input())
sum_1 = 0
sum_2 = 0

for x in range(0,n):
    num = int(input())
    sum_1 += num

for x in range(0,n):
    num = int(input())
    sum_2 += num

if sum_1 == sum_2:
    print(f'Yes, sum = {sum_1}')
else:
    print(f'No, diff = {abs(sum_1-sum_2)}')