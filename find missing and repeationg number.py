arr= [4,3,6,2,1,1]
n=6
#brute foce approach
for i in range(1,n+1):
    cnt=0
    for j in range(n):
        if i==arr[j]:
            cnt+=1
    if cnt==0:
        print('missing number is',i)
    if cnt==2:
        print('repeating number is',i)
#the time complexity is o(n**2)
#the space complexity is o(1)
#better solution
hashing=[0]*(n+1)
for i in arr:
    hashing[i]+=1
for i in range(1,len(hashing)):
    if hashing[i]==2:
        print('the repeating number is',i)
    elif hashing[i]==0:
        print('the missing number is',i)
#the time complexity is o(2n)
#the space complexity is o(n) for storing the array hashing
#whenever there is a concept of counting use hashing
#optimal solution
sn=n*(n+1)//2
s2n=n*(n+1)*(2*n+1)//6
s=0
s2=0
for i in arr:
    s=s+i
    s2=s2+i**2
val1=sn-s
val2=s2n-s2
val2=val2/val1
x=(val1+val2)//2
y=x-val1
print('missing number',x)
print('repeating number',y)
#another optimal approach (using xor)
xor1=0
xor2=0
for i in range(1,n):
    xor1=xor1^i
    xor2=xor2^arr[i-1]
xor1=xor1^n
xor2=xor1^(xor1^xor2)
print(xor2)
