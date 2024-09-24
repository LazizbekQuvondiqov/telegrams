f=open('test.txt','r')
a=f.read()
s=a
n=len(s)
i=0
x=' '
q=''
while i<n:
    while i<n and s[i] !=x:
        q+=s[i]
        i=i+1
    print(int(q)*2)
    i=i+1
    q=' '
