class Deq:

    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size

        self.stack = [None for elem in range(1001)]  # размер первой части дэка
        self.que = [None for elem in range(1001)]  # размер второй части дека

        self.head = -1  # голова стека
        self.tail = 0  # хвост очереди

        self.stack_que = False  # показывает в каком массиве мы находимся для стека
        self.que_stack = True  # показывает в каком массив е мы находимся для очереди

    # добавить элемент в начало дека
    def push_front(self, value):
        if self.size == self.max_size:
            print("error")
            return

        # общий случай добавления в стек
        if not self.stack_que:
            self.head += 1
            self.stack[self.head] = value
            self.size += 1

        else:  # частный случай удаления из стека
            self.head -= 1
            # условие возврата в массив стек
            if self.head == -1:
                self.head = 0
                self.stack_que = False

                self.stack[self.head] = value
                self.size += 1
                return

            # случай без возврата в стек
            self.que[self.head] = value
            self.size += 1

    # добавить элемент в конец дека
    def push_back(self, value):
        if self.size == self.max_size:  # массив переполнен
            print('error')
            return

        if not self.que_stack:  # случай классического добавления в очередь
            self.tail += 1
            self.que[self.tail] = value
            self.size += 1

        else:  # случай особого добавления в очередь
            self.tail -= 1
            if self.tail == -1:
                self.tail = 0
                self.que_stack = False

                self.que[self.tail] = value
                self.size += 1
                return

            self.stack[self.tail] = value
            self.size += 1

    # вывести и удалить элемент с начала дека
    def pop_front(self):
        if self.size == 0:
            print('error')
            return

        # особый случай
        if self.head == -1:
            self.head = 0

            print(self.que[self.head])

            self.head += 1
            self.stack_que = True
            self.size -= 1
            return

        # общий случай удаления
        if not self.stack_que:
            print(self.stack[self.head])
            self.head -= 1
            self.size -= 1

            if self.head == -1:  # условие перехода в массив que
                self.stack_que = True
                self.head = 0

        else:  # частный случай удаления
            print(self.que[self.head])
            self.head += 1
            self.size -= 1

    # вывести и удалить первый элемент
    def pop_back(self):
        if self.size == 0:
            print('error')
            return

        # общий случай удаления из que
        if not self.que_stack:
            print(self.que[self.tail])
            self.tail -= 1
            self.size -= 1

            if self.tail == -1:  # условие перехода в массив stack
                self.que_stack = True
                self.tail = 0

        else:  # частный случай удаления из que
            print(self.stack[self.tail])
            self.tail += 1
            self.size -= 1


count_command = int(input())
max_deq_size = int(input())
deq_first = Deq(max_deq_size)

for _ in range(count_command):
    command = input().split(" ")

    if command[0] == 'push_back':
        deq_first.push_back(int(command[1]))
    if command[0] == 'push_front':
        deq_first.push_front(int(command[1]))
    if command[0] == 'pop_front':
        deq_first.pop_front()
    if command[0] == 'pop_back':
        deq_first.pop_back()

