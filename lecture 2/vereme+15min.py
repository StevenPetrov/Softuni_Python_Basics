hour = int(input())
minutes = int(input())

all_minutes = hour * 60 + minutes + 15

future_hour = all_minutes // 60       #hour +=minutes // 60
future_minutes = all_minutes % 60     #minutes %= 60

if future_hour >= 24:
    future_hour -= 24


if future_minutes < 10:
    print(f"{future_hour}:0{future_minutes}")  # print(f"{future_hour}:{future_minutes:0 2d}")
else:
    print(f"{future_hour}:{future_minutes}")
