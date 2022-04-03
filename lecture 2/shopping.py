budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())


video_cards_sum = video_cards * 250
processors_sum = processors * (video_cards_sum * 0.35)
ram_memory_sum = ram_memory * (video_cards_sum * 0.1)

total_sum = video_cards_sum + processors_sum + ram_memory_sum

if video_cards > processors:
    discount = total_sum * 0.15
else:
    discount = 0

total_sum = total_sum - discount

if budget >= total_sum:
    print(f"You have {budget-total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum-budget:.2f} leva more!")

