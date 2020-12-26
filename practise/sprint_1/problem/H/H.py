first_digit = input()
second_digit = input()

result = bin(int(first_digit, 2) + int(second_digit, 2))
print(result[2:])