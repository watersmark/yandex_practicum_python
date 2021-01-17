def solution(node, idx):
    new_head = node

    if idx == 0:
        return node.next_item

    while True:
        if idx == 1:
            break

        node = node.next_item
        idx -= 1

    node.next_item = node.next_item.next_item

    return new_head