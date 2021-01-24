from random import randint

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)


for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)


# 1 2 3 4 5 6 7 -> наилучший
# 9 8 7 6 5 4 3 2 1 -> наихудший
# 1 2 8 4 9 0 -> O(n ^ 2) -> средний


# O(n) = O(n ^ 2)
# T(n) = O(n) * 4 * O(n) = 4 * O(n ^ 2)


