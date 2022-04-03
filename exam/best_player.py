hat_trick = False
player_name = input()
best_player_name = ''
most_goals = 0
while player_name != 'END':
    goals = int(input())
    if goals > most_goals:
        most_goals = goals
        best_player_name = player_name
    if goals >= 3:
        hat_trick = True
        if goals >= 10:
            break
    player_name = input()

if hat_trick:
    print(f"{best_player_name} is the best player!")
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"{best_player_name} is the best player!")
    print(f"He has scored {most_goals} goals.")