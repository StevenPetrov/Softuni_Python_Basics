n1 = int(input())
n2 = int(input())
even = 0
odd = 0

for number in range(n1,n2+1):
    even = 0
    odd = 0
    for x, y in enumerate(str(number)):
        if x % 2 == 0:
            even += int(y)
        else:
            odd += int(y)
    if even == odd:
        print(number, end=' ')
