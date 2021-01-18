class StackMaxEffective:

    def __init__(self):
        self.stack = []
        self.max = []

    def push(self, elem):

        if len(self.max) > 0:
            if elem >= self.max[-1]:
                self.max.append(elem)
        else:
            self.max.append(elem)

        self.stack.append(elem)

    def pop(self):
        if len(self.stack) == 0:
            print('error')
        else:
            if self.stack.pop() == self.max[-1]:
                del self.max[-1]

    def get_max(self):
        if len(self.stack) == 0:
            print(None)
        else:
            print(self.max[-1])



count_command = int(input())
stack_obj = StackMaxEffective()

for _ in range(count_command):
    command = input().split(" ")

    if command[0] == 'pop':
        stack_obj.pop()
    if command[0] == 'get_max':
        stack_obj.get_max()
    if command[0] == 'push':
        stack_obj.push(int(command[1]))
