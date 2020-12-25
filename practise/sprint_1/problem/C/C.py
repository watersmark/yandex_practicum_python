import sys

# кол-во строк
row = int(input())

# кол-во элементов в строке
col = int(input())

# массив матрицы
mass = []

for _ in range(row):
    mass.append(sys.stdin.readline().strip().split())

# позиция по строке
row_pos = int(input())

# позиция по столбцу
col_pos = int(input())

# массив элементов, которые находятся рядом
mass_around = []

# случае для левого элемента
if col_pos > 0:
    mass_around.append(int(mass[row_pos][col_pos - 1]))

# для правого элемента
if col_pos < col - 1:
    mass_around.append(int(mass[row_pos][col_pos + 1]))

# для верхнего элемента
if row_pos > 0:
    mass_around.append(int(mass[row_pos - 1][col_pos]))

# для нижнего элемента
if row_pos < row - 1:
    mass_around.append(int(mass[row_pos + 1][col_pos]))

mass_around.sort()
print(*mass_around)
