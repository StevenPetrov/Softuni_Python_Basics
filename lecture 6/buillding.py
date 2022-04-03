floors = int(input())
rooms = int(input())
room_numbers = ''
for f in range(floors,0, -1):
    for a in range(0,rooms):
        if f == floors:
            print(f'L{f}{a} ', end='')
        elif f != floors:
            if f % 2 == 0:
                room_numbers += (f'O{f}{a} ')
            else:
                room_numbers += (f'A{f}{a} ')
    print(room_numbers)
    room_numbers = ''