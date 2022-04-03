aircompany = input()
tickets_adults = int(input())
tickets_kids = int(input())
price_adult = float(input())
tax = float(input())

total_adult_tickets = tickets_adults * price_adult
total_kids_tickets = (price_adult * 0.3) * tickets_kids
total_tax = (tickets_kids + tickets_adults) * tax

profit = (total_tax+total_kids_tickets+total_adult_tickets) * 0.2

print(f"The profit of your agency from {aircompany} tickets is {profit:.2f} lv.")