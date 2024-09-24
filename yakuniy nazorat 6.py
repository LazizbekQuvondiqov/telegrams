x = int(input("Введите значение x: "))
S = 0
i = 2
while i <= 20:
    S += x ** i
    i += 2
print("Значение S =", S)
