arr=[1,2,3,4,5]
d=int(input())
#d=2  [5,4,1,2,3]
temp=arr[len(arr)-1:(len(arr)-d)-1:-1]
for i in range((len(arr)-d)+1):
    arr[i+d]=arr[i]
arr[:d]=temp
print(arr)
