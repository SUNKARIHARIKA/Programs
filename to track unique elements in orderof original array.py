arr=[1,2,1,3,4,2,6,1,3,5]
seen=set()
result=[]
for i in arr:
    if i not in seen:
        seen.add(i)
        result.append(i)
print(result)
