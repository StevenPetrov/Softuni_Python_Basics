n = int(input())
sum_even = 0
sum_odd = 0
for n in range(n):
    if n % 2 == 0:
        num = int(input())
        sum_even += num
    else:
        num = int(input())
        sum_odd += num

if sum_odd == sum_even:
    print('Yes')
    print(f'Sum = {sum_even}')
else:
    print('No')
    print(f'Diff = {abs(sum_even-sum_odd)}')