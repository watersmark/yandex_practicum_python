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



def delete_node(node, idx) -> Node:
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


third = Node(10, None)
second = Node(20, third)
head = Node(30, second)

print(node_step(head))
head = delete_node(head, 2)
print(node_step(head))
