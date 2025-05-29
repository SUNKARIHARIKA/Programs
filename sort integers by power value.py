lo = 12
hi = 15
k = 2
l={}
for i in range(lo,hi+1):
    count=0
    n=i
    while n!=1:
        if n%2==0:
            n=n//2
            count+=1
        else:
            n=3*n+1
            count+=1
    l[i]=count
sorted_items = sorted(l.items(), key=lambda x: (x[1], x[0]))
print(sorted_items[k-1][0])