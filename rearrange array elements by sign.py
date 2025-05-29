arr=[3,4,-2,9,-3,-1]
positive=[]
negative=[]
for i in arr:  #o(n)
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
result=[]
for i in range(len(arr)//2):  #o(n/2)
    arr[i*2]=positive[i] 
for i in range(len(arr)//2):  #o(n/2)
    arr[2*i+1]=negative[i]
print(arr)
#the total time complexity o(2n)
#the total space complexity is  o(n).....o(n/2) for positives and another o(n/2) for nrgatives
#another optimal approach
positive=0
negative=1
result=[0]*(len(arr))
for i in arr:
    if i>0:
        result[positive]=i
        positive+=1
    else:
        result[negative]=i
        negative+=2
print(result)
#the time complexity of the above approach is o(n)
#the space complexity of the above approach is o(n)
#<---------------IF the condition that number of positive and negative elements are not same----------->
#arr=[-1,2,3,4,-3,1] #here the number of positive elements are 4 and negative elements are 2
#output:[2,-1,3,-3,4,1]
arr=[-1,2,3,-3,-4,-5] 
# output:[2,-1,3,-3,-4,-5]
positive=[]
negative=[]
for i in arr:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
minimum=min(len(positive),len(negative))
if len(positive)>len(negative):
    for i in range(minimum):
        arr[i*2]=positive[i]
        arr[i*2+1]=negative[i]
    index=minimum*2
    for i in range(minimum,len(positive)):
        arr[index]=positive[i]
        index+=1
    print(arr)
else:
    for i in range(minimum):
        arr[i*2]=positive[i]
        arr[i*2+1]=negative[i]
    index=minimum*2
    for i in range(minimum,len(negative)):
        arr[index]=negative[i]
        index+=1
    print(arr)


