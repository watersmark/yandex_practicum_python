class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node):

    while True:

        node.next, node.prev = node.prev, node.next

        if node.prev == None:
            return node


