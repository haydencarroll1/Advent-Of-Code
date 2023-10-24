with open("input.txt") as f:
    lst = [x for x in f.read().split('\n')]

total_points = 0

for i in lst:
    if 'X' in i:
        if 'A' in i:
            total_points += 3
        elif 'B' in i:
            total_points += 1
        elif 'C' in i:
            total_points += 2
    if 'Y' in i:
        total_points += 3
        if 'A' in i:
            total_points += 1
        elif 'B' in i:
            total_points += 2
        elif 'C' in i:
            total_points += 3
    if 'Z' in i:
        total_points += 6
        if 'A' in i:
            total_points += 2
        elif 'B' in i:
            total_points += 3
        elif 'C' in i:
            total_points += 1

print(total_points)