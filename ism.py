def my_function (name):
    print(name + " dasturchi")
my_function ("Faxriddin")
my_function ("Bekmurod")
def yuza ( a,b,c):
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**1/2
    return s
x1=float(input("x1="))
x2=float(input("x2="))
x3=float(input("x3="))
ss=yuza(x1,x2,x3)
print("Yuza=",ss)
def circle(r):
    PI=3,14
    len=2*PI*r
    return len


def ff(n):
    p=0
    for i in range(0.1, n+1):
        i=0.1
        p+=i
        return p
a=float(input("a="))
print("Natija -" + ff(a))



