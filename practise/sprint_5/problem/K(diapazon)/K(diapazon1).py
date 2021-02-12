class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def print_range(node: Node, l: int, r: int):

    if node.value >= l and node.left is not None:
        print_range(node.left, l, r)

        if l <= node.value <= r:
            print(node.value)

    elif node.left is None:
        if l <= node.value <= r:
            print(node.value)

    # проверки для правого поддерева
    if node.right is not None and node.value <= r:
        print_range(node.right, l, r)


def start():
    n7 = Node(value=2)
    n6 = Node(None, n7, 1)
    n5 = Node(None, None, 8)
    n4 = Node(None, n5, 8)
    n3 = Node(n4, None, 9)
    n2 = Node(n3, None, 10)
    n1 = Node(n6, n2, 5)
    print_range(n1, 2, 8)


if __name__ == "__main__":
    start()
