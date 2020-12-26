import sys
import math

digit = int(input())

if math.log(digit, 4) % 2 == 0.0 or digit == 4:
    print(True)
else:
    print(False)
