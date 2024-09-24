import random

# Massivni tasodifiy qiymatlar bilan to'ldirish
arr = [random.randint(1, 100) for i in range(12)]

# Massivni ekranga chiqarish
print("Massiv: ", arr)

# Massivning elementlar diapazonini topish
min_elem = min(arr)
max_elem = max(arr)

# Diapazonni ekranga chiqarish
print("Elementlar diapazoni: ", min_elem, "-", max_elem)

# Diapazonni faylga yozish
with open("aaa.txt", "w") as file:
    file.write(str(min_elem) + "-" + str(max_elem))
