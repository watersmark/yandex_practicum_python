import sys


def req_fib(first, second, idx, rang, step=2):
    if idx == 0 or idx == 1:
        return 1

    if step == idx:
        return (first + second) % (10 ** rang)

    return req_fib(second, (first + second) % (10 ** rang), idx, rang, step + 1)


sys.setrecursionlimit(10 ** 7)
idx, rang = input().split(" ")
print(req_fib(1, 1, int(idx), int(rang)))
