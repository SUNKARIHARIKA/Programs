'''n=int(input("enter a number"))
l=[]
found=False
for i in range(1,n+1):
    l.append(i)
for i in l:
    if(i**2 in l):
        print(i**2,end=" ")
        found=True
if not found:
    print(-1)'''
n=int(input("enter number"))
l=[i**2 for i in range(1,n+1)]
l1=[]
for i in range(1,n+1):
    if i in l:
        l1.append(i)
print(str(l1),end=" ")
        