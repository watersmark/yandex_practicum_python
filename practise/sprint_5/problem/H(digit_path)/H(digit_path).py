class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

# суть данной задачи обойти последовательно прямым обходои всё дерево
# надо так же уметь возвращаться, если мы сильно углубились при движении влево
# и уметь возвращаться, если углубились при движени вправо

def solution(node):
    sum_of_tree = 0
    step_of_right_tree = []

    mass_of_temp_digit = []

    while True:

        # делаем проверку чтобы ноль не стоял сначала
        if not mass_of_temp_digit and node.value == 0:
            pass
        else:
            mass_of_temp_digit.append(str(node.value))


        # добавляем элементы, если дошли до листа
        if node.left is None and node.right is None:
            sum_of_tree += int("".join(mass_of_temp_digit))
            step_of_right_tree.append(None)

            while True:

                # выходим из цикла, если массив пуст
                if not step_of_right_tree: return sum_of_tree
                next_node = step_of_right_tree.pop()

                # удаляем элемент из массива, есди в другом массиве он помечен как None
                if next_node is None:
                    mass_of_temp_digit.pop()
                else:
                    node = next_node
                    break

        else:
            # чтобы можно было вернуться из правой ветви
            if node.right is not None:
                step_of_right_tree.append(None)
            # на каждой иттерации добавляем значение правой ветви, чтобы
            # если сделали много шагов по левой ветви можно было вернуться
            step_of_right_tree.append(node.right)
            if node.left is None:
                node = step_of_right_tree.pop()
            else:
                node = node.left

def start():
    n5 = Node(2)
    n4 = Node(2)
    n3 = Node(1)
    n2 = Node(3, n4, n3)
    n1 = Node(1, n5, n2)

    #____________________
    # n3 = Node(3)
    # n2 = Node(5)
    # n1 = Node(1, n3, n2)

    #_____________________

    # n9 = Node(1)
    # n8 = Node(6)
    # n7 = Node(4, n9, n8)
    # n6 = Node(3, None, n7)
    # n5 = Node(2, None, n6)
    # n4 = Node(2)
    # n3 = Node(1)
    # n2 = Node(3, n4, n3)
    # n1 = Node(1, n5, n2)

    print(solution(n1))

if __name__ == "__main__":
    start()
