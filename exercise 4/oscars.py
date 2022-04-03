actors_name = input()
academy_points = float(input())
number_of_voters = int(input())

actor_points = 0
actor_points += academy_points
addition_points = 0
final_points = 0

for each in range(1, number_of_voters + 1):
    name = input()
    voters_points = float(input())
    for x in (name):
        addition_points += 1
    final_points = (voters_points * addition_points) /2
    actor_points += final_points
    addition_points = 0
    if actor_points >= 1250.5:
        break
if actor_points >= 1250.5:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {actor_points:.1f}!")
else:
    print(f"Sorry, {actors_name} you need {1250.5-actor_points:.1f} more!")

