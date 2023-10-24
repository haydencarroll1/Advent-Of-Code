def letter_in_string(letter, string):
    for index in string:
        if index == letter:
            return index


with open("input.txt") as f:
    lst = [x for x in f.read().split('\n')]
final_value = []
number_value = 0

for i in range(0, len(lst), 3):
    value = []
    for j in lst[i]:
        if letter_in_string(j, lst[i + 1]):
            if letter_in_string(j, lst[i + 2]):
                if j.isupper():
                    number_value += ord(j) - 38
                else:
                    number_value += ord(j) - 96
                break


print(number_value)
