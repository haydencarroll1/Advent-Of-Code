with open("input.txt") as f:
    lst = [x for x in f.read().split('\n')]

input_list = [int(i) if i else 0 for i in lst]
total = 0
max_n = 0

for i in input_list:
    if i == 0:
        if total > max_n:
            max_n = total
        total = 0
    else:
        total += i

print(max_n)
