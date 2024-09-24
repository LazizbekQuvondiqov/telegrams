from array import *
massiv= array('i' ,[1,2,3,4,45,5])
massiv.reverse()
print(massiv)
from array import *
d1=[]
for j in  range(5):
     d2=[]
     for i in range(5):
         d2.append(i)
         d1.append(d2)
for i in d1:
    print(i)
from array import *
d1=[]
for k in  range(5):
     d2=[]
     for j in range(5):
         d3=[]
         for i in range(5):
             d3.append(i)
         d2.append(d3)
         d1.append(d2)
for i in d1:
    print(i)
