matn=str(input('Matnni kiriting:')); 
belgi=str(input('Izlanayotgan belgini  kiriting:')); 
m=len(matn); 
n=len(belgi); 
b=0; 
for i in range((m-n)+1): 
 if matn[i:i+1]==belgi: 
 b=b+1; 
if b==0: 
 print("Matnda izlanayotgan belgi yo'q"); 
else: print("Matnda izlanayotgan  belgi",b,"ta");

