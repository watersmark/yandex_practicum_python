import sys

a, x, b, c =[int(elem) for elem in sys.stdin.readline().strip().split()]

print(a * x ** 2 + b * x  + c)