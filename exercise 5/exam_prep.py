poor_grades_count = int(input())
failed = poor_grades_count
average_score = 0
task_number = 0
break_triggered = False
last_task = ''
task = input()
while task != 'Enough':
    task_score = int(input())
    task_number +=1
    average_score += task_score
    if task_score <= 4:
        poor_grades_count -= 1
        if poor_grades_count == 0:
            break_triggered = True
            break
    last_task = task
    task = input()


if break_triggered:
    print(f"You need a break, {failed} poor grades.")
else:
    print(f'Average score: {average_score/task_number:.2f}')
    print(f"Number of problems: {task_number}")
    print(f"Last problem: {last_task}")
