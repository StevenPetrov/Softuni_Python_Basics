rounds = int(input())
starting_points = int(input())

wins = 0
finals = 0
semi_finals = 0

for each in range(rounds):
    result = input()
    if result == 'W':
        starting_points += 2000
        wins += 1
    elif result == 'F':
        starting_points += 1200
        finals += 1
    elif result == 'SF':
        starting_points += 720
        semi_finals += 1

average_points = int(((wins * 2000) + (finals * 1200) + (semi_finals * 720))/rounds)
average_wins = ((wins/rounds)*100)
print(f"Final points: {starting_points:.0f}")
print(f'Average points: {average_points:.0f}')
print(f'{average_wins:.2f}%')

