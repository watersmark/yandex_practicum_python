import sys

line = sys.stdin.readline().strip()
idx, pows = line.split()

idx = int(idx)
pows = int(pows)


step = 2

first = 1
second = 1

while True:

    if idx == 0 or idx == 1:
        print(1)
        break

    if step >= idx:
        print((first + second) % (10 ** pows))
        break

    temp = first

    first = second
    second = (temp + second) % (10 ** pows)

    step += 1

