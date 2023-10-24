with open("input.txt") as f:
    input_list = [int(i) if i else 0 for i in f.read().split('\n')]

total = 0
max_n = [0]*3

for i in input_list:
    if i == 0:
        if total > min(max_n):
            max_n[max_n.index(min(max_n))] = total
        total = 0
    else:
        total += i

print(max_n)
print(sum(max_n))
