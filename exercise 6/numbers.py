number = int(input())
count = 1
all_printed = False

for row in range(1,number+1):
    for collumn in range(1,row + 1):
        print(count, end=' ')
        count += 1
        if count >  number:
            all_printed = True
            break
    if all_printed:
        break
    print()

