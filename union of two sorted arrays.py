arr1=[1,1,2,3,3,4,5,5]
arr2=[1,2,2,4,5,6]
#brute force solution
'''s=set(arr1+arr2)
print(s)'''
#the time complexity of brute force approach is o(m+n) where m=len(arr1) and n=len(arr2)
#<----otimal approach--->
n1=len(arr1)
n2=len(arr2)
union=[]
i,j=0,0
while i<n1 and j<n2:
    if(arr1[i]<=arr2[j]):
        if not union or union[-1]!=arr1[i]:
            union.append(arr1[i])
        i+=1
    else:
        if not union or union[-1]!=arr2[j]:
            union.append(arr2[j])
        j+=1
while j<n2:
    if not union or union[-1]!=arr2[j]:
        union.append(arr2[j])
    j+=1
while i<n1:
    if not union or union[-1]!=arr1[i]:
        union.append(arr1[i])
    i+=1
print(union)
     

