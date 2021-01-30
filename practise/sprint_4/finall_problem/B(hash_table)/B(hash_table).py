# номер посылки: 47614883
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
        hash = self.get_hash(key)

        # если массив пустой, то просто добавляем элемент
        # в ином случае, ищем в связном списке
        if not self.mass[hash]:
            self.mass[hash] = Node(key, value)
        else:
            temp_head = self.mass[hash]

            # проверяем каждый узел, если ничего не нашли для
            # обновления, то просто добавляем новый элемент в начало
            while temp_head is not None:
                if temp_head.key == key:
                    temp_head.value = value
                    return

                temp_head = temp_head.next

            # так как мы не нашли элемента, мы добавим его в начало
            new_node = Node(key, value)
            new_node.next = self.mass[hash].next
            self.mass[hash].next = new_node

    # получаем элемент
    def get(self, key):
        hash = self.get_hash(key)

        # если корзина пуста
        if self.mass[hash] == []:
            return None
        else:
            temp_head = self.mass[hash]

            while temp_head is not None:
                if temp_head.key == key:
                    return temp_head.value
                temp_head = temp_head.next

            return None

    # удаляем элемент
    def delete(self, key):
        hash = self.get_hash(key)
        temp_head = self.mass[hash]
        last_elem = temp_head
        step = 0

        if self.mass[hash]:
            while temp_head is not None:
                if temp_head.key == key:
                    # элемент который удаляем
                    value_elem = temp_head.value

                    # удаляем элемент
                    if step == 0:
                        self.mass[hash] = []
                    else:
                        last_elem.next = temp_head.next

                    return value_elem

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


# начало работы программы
if __name__ == "__main__":
    start()
