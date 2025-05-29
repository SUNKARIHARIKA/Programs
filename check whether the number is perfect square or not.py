'''n=int(input("enter the value"))
import math
print(math.ceil(math.sqrt(n)))==math.floor(math.sqrt(16))
print(math.isqrt(15))
l1=[1,2,3,4,5]
l2=[1,2,3,4]
print(l1==l2)'''
head = [1,2,3,4,5]
#[1,3,5,2,4]
odd=0
even=1
while odd<len(head) and even<len(head):
    if head[odd]%2!=0:
        odd+=2
    elif head[even]%2==0:
        even+=2
    else:
        head[odd],head[even]=head[even],head[odd]
        odd+=2
        even+=2
print(head)

