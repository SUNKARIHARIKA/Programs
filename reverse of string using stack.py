s=input("enter string")
rev=''
stack=[]
for i in s:
    stack.append(i)
while stack:
    rev=rev+stack.pop()
print(rev)
