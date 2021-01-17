# для тестов создадим голову списка и его элементы

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def node_step(node):
    while True:
        print(node.value)

        if node.next_item == None:
            break

        node = node.next_item


third = Node(10, None)
second = Node(20, third)
head = Node(30, second)

print(node_step(head))
