def solution(node):

    while True:

        node.next, node.prev = node.prev, node.next

        if node.prev == None:
            return node

        node = node.prev
