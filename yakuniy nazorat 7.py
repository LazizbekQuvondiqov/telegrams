n = int(input("N natural sonini kiriting: "))
raqam_soni = 0
while n > 0:
    raqam_soni += 1
    n //= 10
print("Berilgan sonning raqamlari soni:", raqam_soni)
