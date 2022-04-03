groups = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

total_ppl = 0

for each in range(groups):
    number_of_ppl = int(input())
    total_ppl += number_of_ppl
    if number_of_ppl < 6:
            g1 += number_of_ppl
    elif number_of_ppl < 13:
            g2 += number_of_ppl
    elif number_of_ppl < 26:
            g3 += number_of_ppl
    elif number_of_ppl < 41:
            g4 += number_of_ppl
    else:
            g5 += number_of_ppl

print(f'{g1/total_ppl*100:.2f}%')
print(f'{g2/total_ppl*100:.2f}%')
print(f'{g3/total_ppl*100:.2f}%')
print(f'{g4/total_ppl*100:.2f}%')
print(f'{g5/total_ppl*100:.2f}%')