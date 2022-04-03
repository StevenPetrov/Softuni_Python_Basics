start_interval = int(input())
end_interval = int(input())
magical_number = int(input())
found = False
combination = 0

for n1 in range(start_interval,end_interval+1):
    for n2 in range(start_interval, end_interval + 1):
        if n1 + n2 == magical_number:
            combination += 1
            print(f"Combination N:{combination} ({n1} + {n2} = {magical_number})")
            found = True
            break
        else:
            combination += 1
    if found:
        break

if not found:
    print(f"{combination} combinations - neither equals {magical_number}")