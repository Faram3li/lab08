def fill_matrix(n):
    matrix = []
    value = n * n
    for i in range(n):
        row = []
        for j in range(n):
            row.append(value)
            value -= 1
        matrix.append(row)
    return matrix

n = int(input("Введіть значення N: "))

matrix = fill_matrix(n)

print("Заповнена матриця:")
for row in matrix:
    print(" ".join(map(str, row)))
