
from itertools import product, permutations

count = 0
for elem in permutations('abcd', 0):
    print(elem)
    count += 1

print(count)

# count = 0
# for elem in product(range(5), repeat=2):
#     print(elem)
#     count += 1
# print(f'It is {count}')