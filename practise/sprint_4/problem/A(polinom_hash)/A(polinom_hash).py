q = int(input())
R = int(input())
str = input()

index = len(str) - 1
res_hash = 0

for elem in str:
    res_hash += ord(elem) * (q ** index)
    index -= 1

print(res_hash % R)
