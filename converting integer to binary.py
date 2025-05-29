n=10
rs=''
while n!=0:
    if n%2==1:
        rs=rs+'1'
    else:
        rs=rs+'0'
    n=n//2
print(rs[::-1])
#conerting binay to integer
s='1010'
r=''
for i in s:
    rs=rs+int(i)*(2**int(i))
print(rs)




