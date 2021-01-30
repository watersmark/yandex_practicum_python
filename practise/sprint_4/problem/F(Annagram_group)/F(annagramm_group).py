# поиск анаграмм
def search_anagram():
    count_str = int(input())
    res_str = input().split()
    res_map = dict()

    index = 0
    for elem in res_str:
        temp = sorted(elem)

        if "".join(temp) in res_map:
            res_map["".join(temp)].append(index)
        else:
            res_map["".join(temp)] = [index]
        index += 1

    for elem in res_map.values():
        for elems in elem:
            print(elems, end=" ")
        print()



search_anagram()
