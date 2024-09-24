a=[0]*9
for i in range(len(a)-1):
    i=str(i+1)
    print("massivning "+i+"- elementini kiriting; i"+i+"=", end=" ")
    i=int(i)
    a[i]=int(input())

min=a[0]
max=[0]

for i in range(len(a)):
     if (a[i]<min):
         min=a[i]
     if (a[i] >max):
         max=a[i]
min=str(min)
max=str(max)

print("minimal qiymati - " +min)
print ("maxsimal qiymati -" +max)
