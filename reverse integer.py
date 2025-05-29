k = -123456
rev=0
n=abs(k)
while n>0:
    x=n%10
    rev=rev*10+x
    n=n//10
if k>=0:
    print(rev)
else:
    print(-rev)

