num1=int(input("enter a number"))
num2=int(input("enter a number"))
gcd=1
m=min(num1,num2)
'''for i in range(1,m+1):
    if num1%i==0 and num2%i==0:
        if i>gcd:
            gcd=i
print(gcd)'''
#another method
for i in range(m,2,-1):
    if num1%i==0 and num2%i==0:
        gcd=i
        break
print(gcd)
