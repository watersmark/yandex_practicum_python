# считываем все стороны треугольников
count_area = int(input())
area_mass = [int(elem) for elem in input().split(" ")]
area_mass.sort()

max_sqrt = 0
index_now = len(area_mass) - 1

for elem in area_mass[::-1]:
    if index_now <= 1:
        break
    else:
        if area_mass[index_now] < area_mass[index_now - 1] + area_mass[index_now - 2]:
            max_sqrt = area_mass[index_now] + area_mass[index_now - 1] + area_mass[index_now - 2]
            break

    index_now -= 1

print(max_sqrt)
