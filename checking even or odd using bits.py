n=int(input("enter a number"))
x=bin(n)
n1=str(x)[2:]
if n1[len(n1)-1]=='0':
    print("even number")
else:
    print("odd number")
#most efficient way
n5=10
if(n5&1==0):
    print("even number")
else:
    print("odd number")

