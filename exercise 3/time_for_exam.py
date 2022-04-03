exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_minutes = exam_hour * 60 + exam_minute
arrival_minutes = arrival_hour * 60 + arrival_minute
difference = abs(exam_minutes - arrival_minutes)
minutes = 0
hours = 0
early_check = exam_minutes - arrival_minutes

if arrival_minutes > exam_minutes:
    print('Late')
    if difference >= 60:
        hours = difference // 60
        minutes = difference % 60
        if minutes < 10:
            print(f'{hours}:0{minutes} hours after the start')
        else:
            print(f'{hours}:{minutes} hours after the start')
    elif difference < 60:
        minutes = difference % 60
        print(f'{minutes} minutes after the start')

elif arrival_minutes == exam_minutes:
    print('On time')

elif early_check <= 30:
    print('On time')
    if difference < 60:
        minutes = difference % 60
        print(f'{minutes} minutes before the start')

else:
    print('Early')
    if difference >= 60:
        hours = difference // 60
        minutes = difference % 60
        if minutes < 10:
            print(f'{hours}:0{minutes} hours before the start')
        else:
            print(f'{hours}:{minutes} hours before the start')
    elif difference < 60:
        minutes = difference % 60
        print(f'{minutes} minutes before the start')
