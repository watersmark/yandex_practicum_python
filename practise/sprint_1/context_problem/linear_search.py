# это линейный поиск его проход происходит за линейное время
def linear_search(mass_elem, elem):
    for index in range(len(mass_elem)):
        if mass_elem[index] == elem:
            return index

    return -1

print(linear_search([1, 3, 5, 6, 1], 5))
