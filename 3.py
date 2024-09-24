n = int(input("Введите размер массива: "))
a = []
for i in range(n):
    row = input().split()
    for j in range(len(row)):
        row[j] = int(row[j])
    a.append(row)

product = 1
for i in range(n):
    product *= a[0][i]

print("Произведение элементов первой строки массива: ", product)
-
