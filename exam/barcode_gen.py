start = input()
stop = input()

for x1 in range(int(start[0]), int(stop[0])+1):
    for x2 in range(int(start[1]), int(stop[1]) + 1):
        for x3 in range(int(start[2]), int(stop[2]) + 1):
            for x4 in range(int(start[3]), int(stop[3]) + 1):
                if x1 % 2 != 0 and x2 % 2 != 0 and x3 % 2 != 0 and x4 % 2 != 0:
                    print(f'{x1}{x2}{x3}{x4}', end=' ')
