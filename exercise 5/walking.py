goal_steps = 10000
steps_for_the_day = 0

while steps_for_the_day <= goal_steps:
    steps_count = input()
    if steps_count == 'Going home':
        last_steps = int(input())
        steps_for_the_day += last_steps
        break
    else:
        steps_for_the_day += int(steps_count)

difference = abs(goal_steps - steps_for_the_day)
if steps_for_the_day < goal_steps:
    print(f"{difference} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")

