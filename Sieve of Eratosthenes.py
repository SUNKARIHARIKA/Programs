import math
n=int(input("enter the numbers"))
primes=[True]*(n+1)
primes[0]=primes[1]=False
for i in range(2,int(math.sqrt(n))+1):
    if primes[i]:
        for j in range(i*i,n+1,i):
            primes[j]=False
l=[i for i in range(n) if primes[i]==True]
print(l)