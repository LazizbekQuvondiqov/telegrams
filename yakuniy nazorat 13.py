import math

# n ni kiriting
n = int(input("n ni kiriting: "))

# sin qiymatlarini hisoblash va yig'indisini hisoblash
sin_sum = 0
for i in range(1, n+1):
    sin_sum += math.sin(i)

# A ni hisoblash
A = n / sin_sum

# A ni ekranga chiqarish
print("A =", A)
