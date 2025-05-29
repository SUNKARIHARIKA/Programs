arr=[1,2,3,4,5,0]
for i in range(1,len(arr)):
    if arr[i]<=arr[i-1]:
        print("False array is not in sorted order")
        break
else:
    print("True array is in sorted order")
