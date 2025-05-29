arr=[1,6,3,9,9,7,3,7,2]
largest=arr[0]
slargest=float('-inf')
tlargest=float('-inf')
for i in range(1,len(arr)):
    if arr[i]==largest or arr[i]==slargest or arr[i]==tlargest:
        continue
    elif arr[i]>largest:
        tlargest=slargest
        slargest=largest
        largest=arr[i]
    elif arr[i]<largest and arr[i]>slargest:
        tlargest=slargest
        slargest=arr[i]
    elif arr[i]<slargest and arr[i]>tlargest:
        tlargest=arr[i]
print(tlargest)
