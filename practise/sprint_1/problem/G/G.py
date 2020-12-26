import sys

def convert_x10_x2(digit):

    result = []
    while digit >= 2:

        result.append(digit % 2)
        digit //= 2

    result.append(digit)
    result.reverse()
    return "".join([str(elem) for elem in result])

digit = int(input())
print(convert_x10_x2(digit))
