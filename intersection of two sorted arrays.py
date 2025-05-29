arr1=[2,2,4]
arr2=[2,2]
#brute force approach
intersection=[]
visited=[]
for i in range(len(arr1)):
    if arr1[i] in arr2 and arr1[i] not in visited:
        intersection.append(arr1[i])
        visited.append(arr1[i])
print(intersection)
#the time complexity id o()
#optimal solution
'''n1=len(arr1)
n2=len(arr2)
intersection=[]
i,j=0,0
while i<n1 and j<n2:
    if arr1[i]==arr2[j]:
        intersection.append(arr1[i])
        i+=1
        j+=1
    elif arr1[i]<arr2[j]:
        i+=1
    else:
        j+=1
print(intersection)'''


