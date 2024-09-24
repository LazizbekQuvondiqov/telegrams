# Butun sonli massivni yaratish
import random

A = [[random.randint(1, 100) for j in range(20)] for i in range(10)]

# Massivni ekranga chiqarish
print("Massiv: ")
for i in range(10):
    for j in range(20):
        print(A[i][j], end=" ")
    print()

# Xil elementlarni hisoblash
unique_elements = set()
for i in range(10):
    for j in range(20):
        unique_elements.add(A[i][j])

# Xil elementlar sonini ekranga chiqarish
print("Xil elementlar soni: ", len(unique_elements))

# Xil elementlarni "aa.txt" fayliga yozish
with open("aa.txt", "w") as file:
    file.write(str(len(unique_elements)))
