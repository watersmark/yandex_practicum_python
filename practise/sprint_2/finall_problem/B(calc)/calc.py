import math


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()


stack = Stack()
for elem in input().split(" "):

    try:
        stack.add(int(elem))
    except:
        operation = elem
        if operation == '+':
            stack.add(stack.pop() + stack.pop())
        if operation == '-':
            stack.add(-stack.pop() + stack.pop())
        if operation == '*':
            stack.add(stack.pop() * stack.pop())
        if operation == '/':
            first_pop = stack.pop()
            second_pop = stack.pop()
            stack.add(math.floor(second_pop / first_pop))

print(stack.pop())
