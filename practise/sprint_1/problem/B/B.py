import sys

a, b, c  = [int(elem) for elem in sys.stdin.readline().strip().split()]

if a % 2 == 0 and b % 2 == 0 and c % 2== 0:
    print("WIN")
elif a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print("WIN")
else:
    print("FAIL")


