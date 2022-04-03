h = int(input())
a = int(input())
b = int(input())

all_square_meters = a * b * h
No_more_space = False

while all_square_meters > 0:
    insert_boxes= input()
    if insert_boxes == 'Done':
        print(f"{all_square_meters} Cubic meters left.")
        break
    elif int(insert_boxes) > all_square_meters:
        needed_space = int(insert_boxes) - all_square_meters
        No_more_space = True
        break
    else:
        all_square_meters -= int(insert_boxes)

if No_more_space:
    print(f"No more free space! You need {needed_space} Cubic meters more.")



