# hello

def polinom():

    osn = int(input())
    mod = int(input())
    str = input()


    if len(str) == 1:
        return ord(str[0]) % mod
    if len(str) == 2:
        return ord(str[0] * osn + str[1]) % mod

    index = 0
    res_hash = 0

    for _ in range(len(str) - 1):

        if index == 0:
            res_hash = (ord(str[0]) * osn + ord(str[1])) % mod
            index += 2
        else:
            res_hash = (res_hash * osn + ord(str[index])) % mod
            index += 1

    return res_hash


print(polinom())
