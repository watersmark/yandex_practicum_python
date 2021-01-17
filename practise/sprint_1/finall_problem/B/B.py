# создадим map и пройдёмся по нему, чтобы узнать сколько очков
# будет получено

count_ever = int(input())
map_elem = {}

# создадим map, который будет показывать кол-во элементов каждой величины
for _ in range(4):
    for elem in input():
        if elem in map_elem:
            map_elem[elem] += 1
        elif elem == '.':
            continue
        else:
            map_elem[elem] = 1

# перейдём к обходу map и подсчёту баллов

result_count = 0
for key in map_elem.keys():
    if map_elem[key] <= count_ever * 2:
        result_count += 1

print(result_count)
