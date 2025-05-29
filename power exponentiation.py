x=int(input("enter a number"))
n=int(input("enter a number"))
m=x
ans=1
while n>0:
    if n%2==0:
        x=x*x
        n=n//2
    else:
        ans=ans*x
        n=n-1
if m<0:
    print(1//ans)
print(ans)
