# кол-во детей
count_children = int(input())
children = [int(elem) for elem in input().split(" ")]

# кол-во печенья
count_cookie = int(input())
cookie = [int(elem) for elem in input().split(" ")]

# отсортировали массивы
children.sort()
cookie.sort()

index_now = len(cookie) - 1
result_will = 0

for will in children[::-1]:

    if cookie[index_now] >= will and index_now >= 0:
        result_will += 1
        cookie[index_now] -= 1
        index_now -= 1

print(result_will)
