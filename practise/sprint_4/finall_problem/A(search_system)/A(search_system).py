def 


# начало работы программы
def start():
    # кол-во документов на вход
    count_dock = int(input())

    # создадим hash_map для наших слов
    # в один hash_map будет вложен другой
    hash_map = dict()

    for index in range(count_dock):

        # строка для временного считывания
        temp_str = input().split()
        for elem in temp_str:
            if elem in hash_map:
                # если данный номер документа уже есть, иначе создадим
                if index in hash_map[elem]:
                    hash_map[elem][index] += 1
                else:
                    hash_map[elem][index] = 1
            else:
                hash_map[elem] = {index: 1}

    # перейдём к работе с запросами
    # кол-во запросов
    count_quest = int(input())

    # создадим set() для подсчёта релевантности
    temp_set = dict()

    # обработаем каждый запрос по отдельности
    for index in range(count_quest):
        temp_set = dict()
        temp_str = set(input().split())

        # пройдёмся по каждому элементу запроса
        # для каждого элемента подситаем кол-во вхождений
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

        temp_set = sorted(list(temp_set.items()), key=, reverse=True)

        print(temp_set)

        index = 0
        while index != 5 and len(temp_set) > index:
            print(temp_set[index][0] + 1, end=" ")
            index += 1

        print('end step')


# точка входа в программу
if __name__ == "__main__":
    start()
    # dict = {1: 2, 0: 2, 2: 3}
    #
    # dict = sorted(list(dict.items()), key=lambda item: (item[0], item[1]))
    # print(dict)
    # mass = [(1, 2), (0, 2)]
    # print(mass[1][0])
