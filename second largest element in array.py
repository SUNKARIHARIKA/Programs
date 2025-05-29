#brute force approach
#the time complexity of the above approach is o(nlogn)+o(n)    nlogn-->sorting  o(n)--serching space complexity is o(1)
arr=[1,2,4,5,7,7]
arr.sort()
print(arr)
largest=arr[len(arr)-1]
print(largest)
secondlargest=-1
for i in range(len(arr)-2,0,-1):
    if arr[i]!=largest:
        secondlargest=arr[i]
        break
print(secondlargest)
#better approach
#the time complexity of the above approach is o(2n)  because we are iterating two loops of size n
arr=[1,2,4,7,7,5]
#the first pass is to find the maximum number in the array
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print(largest)
#the second pass is used to calculate the second largest element in array
secondlargest=-1
for i in range(len(arr)):
    if arr[i]>secondlargest and arr[i]!=largest:
        secondlargest=arr[i]
print(secondlargest)
#optimal approach
arr=[1,2,4,7,7,5]
largest=arr[0]
secondlargest=float('-inf')
for i in range(1,len(arr)):
    if arr[i]>largest:
        secondlargest=largest
        largest=arr[i]
    elif arr[i]<largest and arr[i]>secondlargest:
        secondlargest=arr[i]
print(secondlargest)
