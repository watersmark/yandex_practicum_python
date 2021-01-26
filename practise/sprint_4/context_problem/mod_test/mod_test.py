str = "GOSH"

hash_str = 0
index = len(str) - 1
q = 251
R = 256

for elem in str:
    hash_str += ord(elem) * (q ** index)
    index -= 1

print(hash_str % R)