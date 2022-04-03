import math

balls_number = int(input())
sum = 0
red_pts = 0
orange_pts = 0
yellow_pts = 0
white_pts = 0
black_pts = 0
else_pts = 0

for x in range(balls_number):
    color = input()
    if color == 'red':
        red_pts += 1
        sum += 5
    elif color == 'orange':
        orange_pts += 1
        sum += 10
    elif color == 'yellow':
        yellow_pts += 1
        sum += 15
    elif color == 'white':
        white_pts += 1
        sum += 20
    elif color == 'black':
        black_pts += 1
        sum = math.floor(sum / 2)
    else:
        else_pts += 1
        continue

print(f'Total points: {sum}')
print(f'Points from red balls: {red_pts}')
print(f'Points from orange balls: {orange_pts}')
print(f'Points from yellow balls: {yellow_pts}')
print(f'Points from white balls: {white_pts}')
print(f'Other colors picked: {else_pts}')
print(f'Divides from black balls: {black_pts}')
