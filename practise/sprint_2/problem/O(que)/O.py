class MyQueueSized:

    def __init__(self, max_size):

        # максимальный размер очереди
        self.max_size = max_size

        # голова очереди
        self.head = 0

        # хвост очереди
        self.tail = 0

        # размер очереди
        self.size = 0

        # сама очередь
        self.que = [None for _ in range(max_size)]

    #добавить элемент
    def push(self, elem):
        if self.size == self.max_size:
            print('error')
            return

        self.que[self.head] = elem
        self.head = (self.head + 1) % self.max_size
        self.size += 1

    # удалить первый элемент
    def pop(self):
        if self.size == 0:
            print(None)
            return


        print(self.que[self.tail])
        self.que[self.tail] = None
        self.tail = (self.tail + 1) % self.max_size
        self.size -= 1

    # напечатать первое число в очереди
    def peek(self):
        if self.size == 0:
            return None

        return self.que[self.tail]

    # получить размер очереди
    def get_size(self):
        return self.size


count_command = int(input())
que_max_size = int(input())

que_first = MyQueueSized(que_max_size)

for _ in range(count_command):
    command = input().split(" ")

    if command[0] == 'pop':
        que_first.pop()
    if command[0] == 'peek':
        print(que_first.peek())
    if command[0] == 'size':
        print(que_first.get_size())
    if command[0] == 'push':
        que_first.push(int(command[1]))


















