#using left shift
n=13
i=2
if (n&(1<<i))==0:
    print("0")
else:
    print("1")
#using right shift
if n&(n>>i)==0:
    print("0")
else:
    print("1")
