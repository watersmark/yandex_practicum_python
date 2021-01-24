# кол-во домов и бюджет
count_home, count_money = [int(elem) for elem in input().split(" ")]

# стоимость домов
home = [int(elem) for elem in input().split(" ")]
home.sort()

count = 0
for home_cost in home:
    if home_cost > count_money:
        break
    else:
        count += 1
        count_money -= home_cost

print(count)
