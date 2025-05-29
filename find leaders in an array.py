arr=[10,22,12,3,0,6]  #find the element such that the right side elements of that number are smaller than that particular number
#brute force approach
result=[]
for i in range(len(arr)):
    flag=True
    for j in range(i+1,len(arr)):
        if arr[i]<=arr[j]:
            flag=False
            break
    if flag:
        result.append(arr[i])
print(result)
#the time complexity of the above approach is o(n**2)
#the space complexity is o(n)
#optimal solution
'''result=[]
maximum=float('-inf')
for i in range(len(arr)-1,-1,-1):
    if arr[i]>maximum:
        result.append(arr[i])
        maximum=arr[i]
print(result)'''

