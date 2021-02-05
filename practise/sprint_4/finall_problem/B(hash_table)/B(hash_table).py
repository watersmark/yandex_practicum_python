# номер посылки: 48012485
# временная сложность в среднем O(1)
# пространственная O(n)

# вспомогательный класс для метода цепочек
# создаём наши узлы
class Node:

    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None


# класс для обработки запросов к хеш таблице
# дополнительный метод для определения get_hash
class HashTable:

    # определяем размер массива и mod для корзин
    def __init__(self):
        self.mass = [[]] * 999_71
        self.mod = 999_71

    # функция для полуения hash
    def get_hash(self, key):
        return key % self.mod

    # вставляем новый элемент
    def put(self, key, value):
        hash_value = self.get_hash(key)

        # если массив пустой, то просто добавляем элемент
        # в ином случае, ищем в связном списке
        if not self.mass[hash_value]:
            self.mass[hash_value] = Node(key, value)
        else:
            temp_head = self.mass[hash_value]

            # проверяем каждый узел, если ничего не нашли для
            # обновления, то просто добавляем новый элемент в начало
            while temp_head is not None:
                if temp_head.key == key:
                    temp_head.value = value
                    return

                temp_head = temp_head.next

            # так как мы не нашли элемента, мы добавим его в начало
            new_node = Node(key, value)
            new_node.next = self.mass[hash_value].next
            self.mass[hash_value].next = new_node

    def get(self, key):
        hash_value = self.get_hash(key)

        if self.mass[hash_value]:
            temp_head = self.mass[hash_value]

            while temp_head is not None:
                if temp_head.key == key:
                    return temp_head.value
                temp_head = temp_head.next

    def delete(self, key):
        hash_value = self.get_hash(key)
        temp_head = self.mass[hash_value]
        last_elem = temp_head
        step = 0

        if self.mass[hash_value]:
            while temp_head is not None:

                if temp_head.key == key:
                    delete_value = temp_head.value
                    if step == 0:
                        self.mass[hash_value] = []
                    else:
                        last_elem.next = temp_head.next
                    return delete_value

                last_elem = temp_head
                temp_head = temp_head.next
                step += 1
        return None


def start():
    # считаем кол-во комманд
    count_command = int(input())

    # создадим объект хеш-таблицы
    hash_table = HashTable()

    # работаем с командами
    for _ in range(count_command):
        command = input().split()

        # добавляем или обновляем элемент
        if command[0] == 'put':
            hash_table.put(int(command[1]), int(command[2]))
        if command[0] == 'get':
            print(hash_table.get(int(command[1])))
        if command[0] == 'delete':
            print(hash_table.delete(int(command[1])))


if __name__ == "__main__":
    start()
