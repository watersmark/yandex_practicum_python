def local_search():
    # введём кол-во кружков
    count_circle = int(input())

    map_circle = dict()

    for index in range(count_circle):
        elem = input()

        if elem in map_circle:
            pass
        else:
            map_circle[elem] = None
            print(elem)


local_search()
