len_mass = int(input())
mass = [int(elem) for elem in input().split(" ")]
sort_yet = True

for index_i in range(len_mass):
    reverse_elem = 0
    for index_j in range(0, len_mass - index_i - 1):

        first = mass[index_j]
        second = mass[index_j + 1]

        if first > second:
            mass[index_j], mass[index_j + 1] = second, first
            reverse_elem += 1

    if reverse_elem == 0:
        if sort_yet:
            print(" ".join([str(elem) for elem in mass]))
        break
    print(" ".join([str(elem) for elem in mass]))
    sort_yet = False
