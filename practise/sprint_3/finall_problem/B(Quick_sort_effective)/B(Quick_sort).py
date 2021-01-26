
# посылка: 47270805

# реализуем алгоритм быстрого поиска с заданным компаратором\
# сделаем рекурсивно, на каждом шаге дробя по pivot

# __________O(1)_________(пространственная)
# __________O(n^2)____________(временная худший случай) в лучшем O(n * log(n))


def effective_quick_sort(left, right):

    # условие выхода, остался один элемент или пустой массив
    if right - left <= 1:
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]

        return

    # на каждом шаге ищем новый pivot, как среднее промежутка
    pivot_index = (left + right) // 2
    pivot = data[pivot_index]

    # левая и правая граница каждого промежутка
    left_internal, right_internal = left, right

    # идём пока не упрёмся
    while right_internal > left_internal:

        if data[left_internal] < pivot:
            left_internal += 1
            continue

        if pivot < data[right_internal]:
            right_internal -= 1
            continue

        # поменяли элементы по pivot
        data[left_internal], data[right_internal] = data[right_internal], data[left_internal]
        left_internal += 1
        right_internal -= 1

    # сортируем рекурсивно остальные элементы
    effective_quick_sort(left, left_internal)
    effective_quick_sort(right_internal, right)


# кол-во участников
player_count = int(input())

# массив с параметрами участников,создадим сразу определённого размера, чтобы ускорить программу
data = [[]] * player_count

# заполняем массив участников
for index in range(player_count):
    player_one = input().split()
    data[index] = [-int(player_one[1]), int(player_one[2]), player_one[0]]

# сортируем in-place
effective_quick_sort(0, player_count - 1)

# выводим резудьтаты
for index in range(player_count):
    print(data[index][2])

