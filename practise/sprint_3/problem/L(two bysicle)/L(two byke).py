# реализация бинарного поиска с помощью цикла
def BinarySearch(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1

    while (first <= last) or last >= first:
        mid = (first + last) // 2

        if lys[mid] >= val:
            index = mid + 1
            last = mid - 1
        else:
            first = mid + 1

    return index


# кол-во дней наблюдений
count_day = int(input())

mass_day = [int(elem) for elem in input().split(" ")]
bike_cost = int(input())

print(BinarySearch(mass_day, bike_cost), end=" ")
print(BinarySearch(mass_day, bike_cost * 2), end=" ")
