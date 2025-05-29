#with parameter with return type
def prime(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag==1):
        return("number is not prime")
    else:
        return("number is prime")
num=int(input("enter number"))
c=prime(num)
print(c)'
#with parameter without return type
def prime(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag==1):
        print("number is not prime")
    else:
        print("number is prime")
num=int(input("enter number"))
prime(num)
#without parameters with return type
def prime():
    n=int(input("enter number"))
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag==1):
        return "number is not prime"
    else:
        return "number is prime"
c=prime()
print(c)
#without parameter without return type
def prime():
    n=int(input("enter number"))
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag==1):
        print("number is not prime")
    else:
        print("number is prime")
prime()
