class StackMax:

    def __init__(self):
        self.stack = []
        self.max = None

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if len(self.stack) == 0:
            print('error')
        else:
            self.stack.pop()

    def get_max(self):
        if len(self.stack) == 0:
            print(None)
        else:
            print(max(self.stack))


count_command = int(input())
stack_obj = StackMax()

for _ in range(count_command):
    command = input().split(" ")

    if command[0] == 'pop':
        stack_obj.pop()
    if command[0] == 'get_max':
        stack_obj.get_max()
    if command[0] == 'push':
        stack_obj.push(int(command[1]))
