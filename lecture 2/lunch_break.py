import math

series_name = input()
episode_minutes = int(input())
break_minutes = int(input())

lunch_time = break_minutes * 0.125
chill_time = break_minutes * 0.25

free_time = break_minutes - lunch_time - chill_time

if free_time >= episode_minutes:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(free_time-episode_minutes)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(episode_minutes-free_time)} more minutes.")