import math

# A(x,y) sonlarini kiritish
x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))

# Aylana markazining koordinatalari
center_x = 1
center_y = 0

# Aylana radiusini hisoblash
radius = math.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)

# Aylana radiusini ekranga chiqarish
print("Aylana radiusi:", radius)

# Aylana markazining koordinatalarini ekranga chiqarish
print("Aylana markazi: (", center_x, ",", center_y, ")")

# Aylana tenglamasini ekranga chiqarish
print("Aylana tenglamasi: (x -", center_x, ")^2 + (y -", center_y, ")^2 =", radius ** 2)
