sum_prime = 0
sum_non_prime = 0
prime = True

while True:
    command = input()
    if command == 'stop':
        break
    command = int(command)
    if int(command) < 0:
        print('Number is negative.')
        command = 0
    for number in range(2, command):
        if command % number == 0:
            prime = False
            break

    if prime:
        sum_prime += int(command)
    else:
        sum_non_prime += int(command)
        prime = True

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
