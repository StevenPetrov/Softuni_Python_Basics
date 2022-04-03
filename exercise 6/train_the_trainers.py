people = int(input())

presentation_name = input()
current_degree = 0
presentations_count = 0
total_average = 0

while presentation_name != 'Finish':
    presentations_count +=1
    for count in range(people):
        degree = float(input())
        current_degree += degree
    current_degree /= people
    print(f'{presentation_name} - {current_degree:.2f}.')
    total_average += current_degree
    current_degree = 0
    presentation_name = input()

print(f"Student's final assessment is {total_average/presentations_count:.2f}.")

