import sys

count_digit = int(input())
mass_digit = [int(elem) for elem in sys.stdin.readline().strip().split()]

if len(mass_digit) > 1:

    day_of_an = 0
    for index in range(len(mass_digit)):
        if index == 0:
            day_of_an += 1 if mass_digit[index] > mass_digit[index + 1] else 0
        elif index == len(mass_digit) - 1:
            day_of_an += 1 if mass_digit[index] > mass_digit[index - 1] else 0
        else:
            day_of_an += 1 if mass_digit[index - 1] < mass_digit[index] > mass_digit[index + 1] else 0
    print(day_of_an)
else:
    print(1)

