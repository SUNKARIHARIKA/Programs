arr=[1,2,3,4,5,6]
left=0
right=len(arr)-1
result=[]
while left<=right:
    if left==right:
        result.append(arr[left])
    else:
        result.append(arr[left])
        result.append(arr[right])
    left+=1
    right-=1
print(result)