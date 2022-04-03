student_name = input()
grade = 0
failed = 0
average_grade  = 0
while grade < 12:
    grade_input = float(input())
    if grade_input < 4:
        failed +=1
        if failed > 1:
            print(f'{student_name} has been excluded at {grade+1} grade')
            break
    else:
        grade += 1
        average_grade += grade_input
        continue
if grade == 12:
    average_grade /= grade
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")