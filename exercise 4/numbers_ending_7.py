n = int(input())
sum = 0
max_num = -99999999

for x in range(n):
    number = int(input())
    if number > max_num:
        max_num = number
    sum += number


if  max_num == sum-max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs((sum-max_num)-max_num)}')