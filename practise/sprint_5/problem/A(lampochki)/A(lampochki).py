class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


# реализуем обход в высоту по дереву
# идём влево, на каждлм шаге добавляем элемент в стек, если есть
# когда достигли конца ветки, то продолжаем обход с последнего элемента в стеке
# когда закончатся все ветки и элементы в массиве возвращаем максмальное значение
# на каждой иттерации передаём в голову новый элемент

def get_max_light(node):
    tree_step_stack = []
    maximum_light = 0

    while True:
        el = node.value

        if node.value > maximum_light:
            maximum_light = node.value

        if node.left is None and node.right is None and not tree_step_stack:
            return maximum_light

        # добавляем правый узел в стек
        if node.right is not None:
            tree_step_stack.append(node.right)

        if node.left is not None:
            node = node.left
        else:
            node = tree_step_stack.pop()


def start():
    # левая ветка
    n4 = Node(14)
    n5 = Node(15)
    n3 = Node(8, n4, n5)
    n21 = Node(310)
    n2 = Node(3, n3, n21)

    # правая вектка
    n9 = Node(0)
    n8 = Node(1)
    n7 = Node(6, n9, n8)
    n6 = Node(112)
    n61 = Node(5, n6, n7)

    # голова
    n1 = Node(1, n2, n61)

    print(get_max_light(n1))


if __name__ == "__main__":
    start()
