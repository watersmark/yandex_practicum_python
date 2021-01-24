from functools import cmp_to_key


def my_cmp(x, y):
    if x + y > y + x:
        return -1
    elif x + y == y + x:
        return 0
    else:
        return 1


count = int(input())
a = [int(elem) for elem in input().split(" ")]
a.sort(key=cmp_to_key(my_cmp))

print(*a, sep='')
