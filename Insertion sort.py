arr=[25,20,15,10,5]
n=len(arr)
for i in range(n):
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)