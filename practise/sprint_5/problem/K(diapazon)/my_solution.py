def print_range(node, l, r):
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
