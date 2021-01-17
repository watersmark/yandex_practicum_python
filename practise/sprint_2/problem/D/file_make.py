def solution(node, elem):
    idx = -1
    index = 0

    while True:

        if elem == node.value:
            return index

        if node.next_item is None:
            return idx

        index += 1
        node = node.next_item