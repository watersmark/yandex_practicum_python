str_get = input()

# курсоры ставим на первый и последний индекс
first_cursor = 0
second_cursor = len(str_get) - 1


# проверка, что число входит в нужный диапазон чисел
def is_true_char(char):
    if 97 <= ord(char.lower()) <= 122 or 48 <= ord(char) <= 57:
        return True
    return False

# временная проверка
def check():
    # курсоры сошлись
    if first_cursor == second_cursor:
        print(True)
        return True


while True:

    if check(): break

    if not is_true_char(str_get[first_cursor]):
        first_cursor += 1
        continue
    if not is_true_char(str_get[second_cursor]):
        second_cursor -= 1
        continue

    if str_get[first_cursor].lower() != str_get[second_cursor].lower():
        print(False)
        break
    else:
        first_cursor += 1
        if check(): break

        second_cursor -= 1

