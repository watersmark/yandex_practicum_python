
# начало работы программы
def calc_hash_map():
    # кол-во документов на вход
    count_dock = int(input())

    # создадим hash_map для наших слов
    # в один hash_map будет вложен другой
    hash_map = dict()

    for index in range(count_dock):

        # строка для временного считывания
        temp_str = input().split()

        # считывем каждый элемнт по отдельности
        for elem in temp_str:
            if elem in hash_map:
                # если данный номер документа уже есть, иначе создадим
                if index in hash_map[elem]:
                    hash_map[elem][index] += 1
                else:
                    hash_map[elem][index] = 1
            else:
                hash_map[elem] = {index: 1}

    # перейдём к работе с запросами и поиску документов
    # переходим во вторую функцию
    work_with_text(hash_map)


def work_with_text(hash_map):

    # перейдём к работе с запросами
    # кол-во запросов
    count_quest = int(input())

    # обработаем каждый запрос по отдельности
    for index in range(count_quest):

        # создадим set() для подсчёта релевантности
        temp_set = dict()
        temp_str = set(input().split())

        # пройдёмся по каждому элементу запроса
        # для каждого элемента подсчитаем кол-во вхождений
        for elem in temp_str:

            if elem in hash_map:
                # пройдёмся по каждому значению поотдельности
                # если значение уже есть, то просто увеличим его значение релевантности
                # иначе создадим его и сразу добавим знаение релевантности
                for key in hash_map[elem]:
                    if key in temp_set:
                        temp_set[key] += hash_map[elem][key]
                    else:
                        temp_set[key] = hash_map[elem][key]

        # выберем пять лучших документов
        # перейдём в следующую функцию
        top_five_dock(temp_set)


# отсортируем и выберем пять лучших документов
def top_five_dock(temp_set):
    temp_set = list(temp_set.items())
    # отберём пять лучших запросов
    index = 0

    for i in range(len(temp_set)):
        if index == 5: break
        for j in range(len(temp_set) - i - 1):
            if temp_set[j][1] > temp_set[j + 1][1]:
                temp_set[j], temp_set[j + 1] = temp_set[j + 1], temp_set[j]

            elif temp_set[j][1] == temp_set[j + 1][1] and temp_set[j][0] < temp_set[j + 1][0]:
                temp_set[j], temp_set[j + 1] = temp_set[j + 1], temp_set[j]
        index += 1

    lens = len(temp_set) - 1

    for index in range(len(temp_set)):
        if index == 5: break
        print(temp_set[lens - index][0] + 1, end=" ")

    print()

# точка входа в программу
if __name__ == "__main__":
    calc_hash_map()
