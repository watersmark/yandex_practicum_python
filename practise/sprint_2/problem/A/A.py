
# кол-во строк и столбцов
row = int(input())
col = int(input())

matrix = []
for _ in range(row):
    matrix.append(input().split(" "))

for index_col in range(col):
    for index_row in range(row):
        print(matrix[index_row][index_col], end=" ")
    print()

