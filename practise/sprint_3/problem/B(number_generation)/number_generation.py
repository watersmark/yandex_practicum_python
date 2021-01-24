def req_number(map_digit, seq, result="", lvl_now=0):
    for elem in map_digit[seq[lvl_now]]:

        if lvl_now == len(seq) - 1:
            print(result + elem, end=" ")
        else:
            req_number(map_digit, seq, result + elem, lvl_now + 1)


map_digit = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

seq = input()

req_number(map_digit, seq)
