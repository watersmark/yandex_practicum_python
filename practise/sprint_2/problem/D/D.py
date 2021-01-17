class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def find_value(node, elem):
    idx = -1
    index = 0

    while True:

        if elem == node.value:
            return index

        if node.next_item is None:
            return idx

        index += 1
        node = node.next_item


def node_step(node):
    while True:
        print(node.value)

        if node.next_item == None:
            break

        node = node.next_item


third = Node(10, None)
second = Node(20, third)
head = Node(30, second)

print(solution(head, 20))
# print(node_step())