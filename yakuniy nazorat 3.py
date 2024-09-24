# ketma-ketlikni o'qish
a = [float(x) for x in input("Ketma-ketlikni kiriting: ").split()]

# eng katta va kichik elementlarni topish
max_index = a.index(max(a))
min_index = a.index(min(a))

# o'rinlarni almashtirish
a[0], a[min_index] = a[min_index], a[-1]
a[-1], a[max_index] = a[max_index], a[0]


# natijani chiqarish
print("Natija:", a)

