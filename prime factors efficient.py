nums = [2,4,3,7,10,6]
def prime(n):
    l=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            l.add(i)
            while(n%i==0):
                n=n//i
    if n!=1:
        l.add(n)
    return l
s=set()
for i in nums:
    s=s|prime(i)
print(s)
