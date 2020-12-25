import math
# реализуем алгоритм рекурсивно
# на каждом шаге проверяем нашли ли мы нужный элемент
# если нет, то далее
# делаем выбор идти влево или вправо
# данная реализация проста и не обрабатывет частные случаи такие, как
# отсутствие искомого элемента в массиве
def binary_search(mass, index, left_border, right_border, search_elem):

    # нашли элемент выходим из рекурсии
    if mass[index] == search_elem:
        return index

    # движемся влево, т.к элемент на котором мы сейчас находимся больше искомого
    if mass[index] > search_elem:
      return  binary_search(mass, index - math.ceil((index - left_border) / 2), left_border, index, search_elem)

    if mass[index] < search_elem:
       return binary_search(mass, index + math.ceil((right_border - index) / 2), index, right_border, search_elem)

mass = [1, 3, 5, 6, 7, 33, 231, 543, 567]
print(binary_search(mass, len(mass) // 2, 0, len(mass) - 1, 6))



