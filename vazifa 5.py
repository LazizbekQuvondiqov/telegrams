import math
x=int(input("x ni kiriting:"))
n=int(input("n ni kiriting:"))
i=1
while i<=n:
    print(i)
    i+=(x**(2*n+1)*(x**(2*n)))/math.factorial(n)

"""import math
i=-math.pi/18
while i<4*math.pi:
    y=math.cos(i)
    i+=math.pi/18
    print(y)"""

