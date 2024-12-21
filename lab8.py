def fill_array(m, n):
    result = [m * i for i in range(1, n + 1)]
    return result

m = int(input("Введіть значення M: "))
n = int(input("Введіть значення N: "))

array = fill_array(m, n)
print("Заповнений масив:", array)
