# идём до первого нуля с начала
def digit_add(result_mass, index):

    for value in range(index + 1):
        result_mass.append(index - value)
    return True

# # идём до первого нуля с конца
# def digit_add_reverse(result_mass, index):
#
#     for value in range(index):
#         if value
#
#     return True

# считаем значения из стандартного потока ввода
count = int(input())
home_seq = input().split(" ")


# сделаем два обхода и найдём наилучшие результаты
len_zero = 0
result_mass = [] * 10
bool = False

for index in range(len(home_seq)):
    if home_seq[index] == '0':
        if not bool:
            bool = digit_add(result_mass, index)
            continue

        len_zero = 0
        result_mass.append(0)
    elif not bool:  # если значение стало True
        continue
    else:
        result_mass.append(len_zero + 1)
        len_zero += 1

# print(result_mass)


len_zero = 0
bool = False
for index in range(len(home_seq)):
    if home_seq[len(home_seq) - 1 - index] == '0':
        # if not bool:
        #     bool = digit_add_reverse(result_mass, index)
        #     continue
        len_zero = 0
        bool = True
    elif not bool:
        continue
    else:
        if len_zero < result_mass[len(home_seq) - 1 - index]:
            result_mass[len(home_seq) - 1 - index] = len_zero + 1
        len_zero += 1

for elem in result_mass:
    print(elem, end=" ")