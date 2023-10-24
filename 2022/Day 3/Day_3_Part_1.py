with open("input.txt") as f:
    lst = [x for x in f.read().split('\n')]

value = 0

for i in lst:
    first_part, second_part = i[:len(i)//2], i[len(i)//2:]
    for j in first_part:
        for k in second_part:
            if j == k:
                if j.isupper():
                    value += ord(j) - 38
                    break
                else:
                    value += ord(j) - 96
                    break
        if j == k:
            break



print(value)
