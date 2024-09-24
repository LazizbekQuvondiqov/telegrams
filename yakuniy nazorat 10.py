n = int(input("10 xonali sonni kiriting: "))
oxirgi_uch_raqam = n % 1000
yigindi = oxirgi_uch_raqam // 100 + oxirgi_uch_raqam % 100 // 10 + oxirgi_uch_raqam % 10
print("Oxirgi uch raqam yig'indisi:", yigindi)
