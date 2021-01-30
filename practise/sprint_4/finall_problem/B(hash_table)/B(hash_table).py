# вспомогательный класс для метода цепочек
# создаём наши узлы
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


# класс для обработки запросов к хещ таблице
class HashTable:

    # определяем размер массива и mod для корзин
    def __init__(self):
        self.mass = [[]] * 99971
        self.mod = 99971

    # вставляем новый элемент
    def put(self, key, value):
        hash = key % self.mod

        # если массив пустой, то просто добавляем элемент
        # в ином случае, ищем в связном списке
        if len(self.mass[hash]) == 0:
            self.mass[hash] = Node(value)
        else:
            temp_head = self.mass[hash]

            # проверяем каждый узел, если ничего не нашли для
            # обновления, то просто добавляем новый элемент в начало
            while temp_head is not None:
                if temp_head.value == value:
                    temp_head.value = value
                    break

                temp_head = temp_head.next

            # так как мы не нащли элемента, мы добавим его в начало
            new_node = Node(value)
            new_node.next = self.mass[hash].next
            self.mass[hash].next = new_node

    # получаем элемент
    def get(self):
        pass

    # удаляем элемент
    def delete(self):
        pass


# считаем еол-во комманд
count_command = int(input())

# раюотаем с командами
for _ in range(count_command):
    command = input().split()

    if command[0] == 'put':
        pass

    if command[0] == 'get':
        pass

    if command[0] == 'delete':
        pass



















