def is_a_valid_message(message):
    mass = ['1','2','3','4','5','6','7','8','9','0']

    if message == "":
        return True

    if message[0] not in mass:
        return False

    if message[len(message) - 1] in mass:
        return False

    digit = ""
    count_word = 0
    digit_int = 0
    is_bool = True

    for elem in message:
        if elem in mass:

            if is_bool:
                if count_word == digit_int:
                    digit = ""
                    count_word = 0
                    digit_int = 0

                    if elem == '0':
                        return False
                else:
                    return False

            digit += elem
            is_bool = False
        else:
            is_bool = True
            digit_int = int(digit)
            count_word += 1

    if count_word != digit_int:
        return False

    return True

str = input()
# str = "3hey5hello2hi"
print(is_a_valid_message(str) == True)