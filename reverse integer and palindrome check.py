#reverse of the number
k = 121
m=k
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
#tracing of the code
'''
k=-123  abs(k)=123  n=123
iteration 1: 
123>0 enters loop
x=123%10 x=3 units digit will be extracted
rev=0 rev=0*10+3  rev=3
n=n//10 123//10 n=12
iteration 2:
12>0 enters loop
x=12%10  x=2 unit digit 2 is extracted
rev=3 rev=3*10+2  rev=32
n=12//10 n=1
iteration 3:
1>0 enters loop
x=1%10 x=1
rev=32*10+1
rev=321
n=n//10 n=1//10 n=0
'''
#pallindrome check
if rev==m:
    print('The number is pallindrome')
else:
    print('the number is not a Pallindrome')

