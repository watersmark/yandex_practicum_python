def solution(node):

    while True:
        print(node.value)

        if node.next_item == None:
            return None

        node = node.next_item