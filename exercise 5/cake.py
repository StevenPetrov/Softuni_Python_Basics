cake_side_a = int(input())
cake_side_b = int(input())

cake_pieces = cake_side_b * cake_side_a

while cake_pieces > 0:
    cake_pickup = input()
    if cake_pickup == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break
    else:
        cake_pieces -= int(cake_pickup)
        continue

if cake_pieces <= 0:
        print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')