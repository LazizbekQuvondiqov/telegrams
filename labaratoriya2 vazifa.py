matn=str(input("Matn kiriting:")); 
m=0;n=0;k=0; 
for i in range(len(matn)): 
 S=matn[i:i+1]; 
 if S=='I': 
  n=n+1; 
 if S=='G': 
  m=m+1; 
 if S==' ': 
  k=k+1; 
print("Matnda I=",n,'-ta, G=',m,"-ta,  matnda bo'sh joy=",k,'-ta');
import math; 
matn=str(input("Matn kiriting:")); 
s=len(matn);t=0; 
for i in range(1,math.ceil(s/2)): 
 if matn[:i]==matn[-i:]:
     t=t+1;
print("So'z ikkiyoqlama");
 elif t==s%2:
         print("So'z ikkiyoqlama emas");
