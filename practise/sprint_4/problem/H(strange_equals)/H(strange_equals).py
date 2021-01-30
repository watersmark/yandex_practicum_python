# первая строка
first = input()

# вторая строка
second = input()

if len(first) > len(second):
    second += '*' * (len(first) - len(second))
if len(second) > len(first):
    first += '*' * (len(second) - len(first))

map_first = dict()
index = 0

# проходим по первой строке
for elem in first:
    if elem in map_first:
        pass
    else:
        map_first[elem] = second[index]
