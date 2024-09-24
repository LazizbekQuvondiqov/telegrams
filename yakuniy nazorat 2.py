# sonni o'qish
x = int(input("Sonni kiriting: "))

# raqamlar yig'indisi va ko'paytmasini hisoblash
rustam = [int(i) for i in str(x)]
sum_rustam = sum(rustam)
mul_rustam = 1
for i in rustam:
    mul_rustam *= i

# natijani chiqarish
print("Raqamlar yig'indisi:", sum_rustam)
print("Raqamlar ko'paytmasi:", mul_rustam)
