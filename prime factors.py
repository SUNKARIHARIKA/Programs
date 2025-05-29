def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input("enter the number"))
l=[]
for i in range(1,int(num**0.5)+1):
    if num%i==0:
        l.append(i)
        if i!=num//i:
            l.append(num//i)
l1=[i for i in l if prime(i)]
print(l1)


