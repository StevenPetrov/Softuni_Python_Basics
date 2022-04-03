movie_title = input()
days = int(input())
number_tickets = int(input())
tickets_price = float(input())
persent = int(input())

sum_price_tickets = days * tickets_price * number_tickets
persent_tax = sum_price_tickets * (persent / 100)
profit = sum_price_tickets - persent_tax


print(f"The profit from the movie {movie_title} is {profit:.2f} lv.")