class Node:

    def __init__(self, value):
        self.next = None
        self.value = value


class QueList:

    def __init__(self):
        self.size = 0

    # метод получения нового элемента из очереди
    def get(self, head):
        if self.size == 0:
            print('error')
            return

        print(head.value)
        self.size -= 1
        return head.next

    # метод добавления нового элемента в очередь
    def put(self, head, digit):

        # если нет элементов в очереди
        if self.size == 0:
            self.size += 1
            return Node(digit)

        head_temp = head

        while True:
            if head.next is None:
                break
            head = head.next

        node_temp = Node(digit)
        head.next = node_temp

        self.size += 1
        return head_temp

    # вывести размер очереди
    def get_size(self):
        print(self.size)


count_command = int(input())
que_first = QueList()
head = None

for _ in range(count_command):
    command = input().split(" ")

    if command[0] == 'get':
        head = que_first.get(head)
    if command[0] == 'put':
        head = que_first.put(head, int(command[1]))
    if command[0] == 'size':
        que_first.get_size()
