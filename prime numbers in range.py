left = 10
right = 19
def seve(n):
    primes=[True]*(n+1)
    primes[0]=primes[1]=False
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i,n+1,i):
                primes[j]=False
    return primes
primes=seve(10**6)
count=0
for i in range(2,10**6):
    count=count+primes[i]
    primes[i]=count
print(primes[right]-primes[left-1])
l=[]
for i in range(left,right+1):
    if primes[i]:
        l.append(i)
print(l)
