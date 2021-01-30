# номер посылки: 47401290

# напишем метод для поиска элемента
# используем реализацию бинарного поиска на цикле
# left_border левая граница
# right_border правая граница
# в классический алгоритм добавим код, чтобы он не выходил
# в другую часть массива при шаге деления на 2
# рассмотрим два случая старта нашего бинарного поиска
# рабивая его на левую и правую половину


# ______________сложность временная____________
# O(log(n)) --> бинарный поиск

# ______________сложность пространственная________
# O(1) --> помимо входного массива мы используем только набор констант


def search_elem_position():

    # считали длину массива
    mass_len = int(input())

    # считали искомый элемент
    search_elem = int(input())

    # считали исходный массив
    mass = [int(elem) for elem in input().split(" ")]

    left_border = 0
    right_border = len(mass) - 1

    is_more = mass[0] <= search_elem

    while True:

        # на каждом шаге ищем центральный элемент
        mid = (left_border + right_border) // 2

        if mass[mid] == search_elem:
            return mid

        # условие выхода
        if left_border >= right_border:
            return -1

        # обработка случая перелёта в другой конец списка
        if is_more:

            # движение вправо
            if search_elem > mass[mid] > mass[0]:
                left_border = mid + 1
            # движение влево
            else:
                # mass[mid] > search_elem:
                right_border = mid - 1
        else:
            # движение влево
            if search_elem < mass[mid] < mass[0]:
                right_border = mid - 1

            # движение вправо
            else:
                # mass[mid] < search_elem:
                left_border = mid + 1


if __name__ == "__main__":
    print(search_elem_position())
