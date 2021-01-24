first_str = input()
second_str = input()

index_now = 0
for elem in second_str:

    if index_now == len(first_str):
        break
    if elem == first_str[index_now]:
        index_now += 1


if index_now == len(first_str):
    print(True)
else:
    print(False)
