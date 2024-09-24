n = int(input("Massivning uzunligini kiriting: "))
a = []
b = []
for i in range(n):
    row = []
    for j in range(2):
        element = int(input(f"{i+1}-qator, {j+1}-elementni kiriting: "))
        row.append(element)
    a.append(row)
    
# Birinchi qator elementlarini ko'paytirish
result = 1
for i in range(n):
    result *= a[i][0]
    
print("Birinchi qator elementlari ko'paytmasi:", result)
