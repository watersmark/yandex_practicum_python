# посылка: 48012881

# ___________________пространственная сложность_____________
# (считывание данных O(n))
# использование констант O(1)
# общая сложность O(n)

# _____________________временная сложность______________
# заполнение dict O(n) +
# поиск релевантности O(1) + O(k)
# Сортировка O(n*log(n))
# Общая сложность O(n*log(n))

def calc_hash_map():
    document_count = int(input())

    # в один hash_map будет вложен другой
    index_storage_dock = dict()

    for index in range(document_count):

        dock_str = input().split()
        for word in dock_str:

            if word in index_storage_dock:
                # если данный номер документа уже есть, иначе создадим
                if index in index_storage_dock[word]:
                    index_storage_dock[word][index] += 1
                else:
                    index_storage_dock[word][index] = 1
            else:
                index_storage_dock[word] = {index: 1}

    # перейдём к работе с запросами и поиску документов
    work_with_text(index_storage_dock)


def work_with_text(hash_map):
    # перейдём к работе с запросами
    # кол-во запросов
    count_quest = int(input())

    for index in range(count_quest):
        relevancy_set = dict()
        temp_str = set(input().split())

        # пройдёмся по каждому элементу запроса
        # для каждого элемента подсчитаем кол-во вхождений
        for elem in temp_str:

            if elem in hash_map:
                # пройдёмся по каждому значению поотдельности
                # если значение уже есть, то просто увеличим его значение релевантности
                # иначе создадим его и сразу добавим знаение релевантности
                for key in hash_map[elem]:
                    if key in relevancy_set:
                        relevancy_set[key] += hash_map[elem][key]
                    else:
                        relevancy_set[key] = hash_map[elem][key]

        # выберем пять лучших документов
        print_top_five_docs(relevancy_set)


# отсортируем и выберем пять лучших документов
def print_top_five_docs(temp_set):
    temp_set = list(temp_set.items())
    temp_set = sorted(temp_set, key=lambda item: (item[1], -item[0]))

    # выведем наши топ 5 документов
    lens = len(temp_set) - 1
    for index in range(len(temp_set)):
        if index == 5: break
        print(temp_set[lens - index][0] + 1, end=" ")

    print()


if __name__ == "__main__":
    calc_hash_map()
