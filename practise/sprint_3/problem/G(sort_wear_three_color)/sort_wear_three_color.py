try:
    count_wear = int(input())
    wear_mass = [int(elem) for elem in input().split(" ")]

    mass = [0, 0, 0]

    for wear in wear_mass:
        mass[wear] += 1

    for index in range(3):
        if mass[index] != 0:
            print(" ".join(str(index) * mass[index]), end=" ")

except:
    pass  # случай при подаче нуля элементов и касте к int
