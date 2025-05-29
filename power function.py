x = 2
n = 10
m=abs(n)
ans=1
while m>0:
    if m%2==0:
        x=x*x
        m=m//2
    else:
        ans=ans*x
        m=m-1
print(ans)


