def solution(node):
    sum_of_tree = 0
    step_of_right_tree = []

    mass_of_temp_digit = []

    while True:

        mass_of_temp_digit.append(str(node.value))

        # добавляем элементы, если дошли до листа
        if node.left is None and node.right is None:
            sum_of_tree += int("".join(mass_of_temp_digit))
            step_of_right_tree.append(None)

            while True:

                if not step_of_right_tree: return sum_of_tree
                next_node = step_of_right_tree.pop()

                if next_node is None:
                    mass_of_temp_digit.pop()
                else:
                    node = next_node
                    break

        else:
            step_of_right_tree.append(node.right)

            if node.left is None:
                node = step_of_right_tree.pop()
                step_of_right_tree.append(None)
            else:
                node = node.left