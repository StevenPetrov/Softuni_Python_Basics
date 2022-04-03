record = float(input())
distance = float(input())
seconds_per_meter = float(input())

delay = (distance // 15) * 12.5

total_time_ivancho = (distance * seconds_per_meter) + delay


if total_time_ivancho < record:
    print(f"Yes, he succeeded! The new world record is {abs(total_time_ivancho):.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record-total_time_ivancho):.2f} seconds slower.")