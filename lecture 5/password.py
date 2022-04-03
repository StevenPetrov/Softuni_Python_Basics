user = input()
password = input()

while True:
    attempt = input()
    if attempt == password:
        break
print(f'Welcome {user}!')