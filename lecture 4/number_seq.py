n = int(input())
list = []

for n in range(n):
    number = int(input())
    list.append(number)

print('Max number:', max(list))
print('Min number:', min(list))