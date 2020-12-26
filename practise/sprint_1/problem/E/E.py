import sys

# длина строки
len_str = int(input())

# полученная строка
string_get = sys.stdin.readline().strip()

long_word = ""
temp_word = ""

do_step = 0
for char in string_get:
    if ord(char) == 32:
        long_word = temp_word if len(temp_word) > len(long_word) else long_word
        temp_word = ""
    else:
        temp_word += char

if len(temp_word) > len(long_word): long_word = temp_word
print(long_word, len(long_word), sep="\n")