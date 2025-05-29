num = 9
#28 = 1 + 2 + 4 + 7 + 14
l=[]
import math
s1=0
for i in range(1,int(math.sqrt(num))+1):
    if num%i==0:
        s1=s1+i
        if i!=num//i:
            s1=s1+num//i
print(s1-num==num)