nums = [9,12,5,10,14,3,10]
pivot = 10
#output-[9,5,3,10,10,12,14]
#the numbers that are less than pivot should be left side in order and greater should be on right
smaller=[]
larger=[]
equal=[]
for i in nums:
    if i<pivot:
        smaller.append(i)
    elif i==pivot:
        equal.append(i)
    else:
        larger.append(i)
print(smaller+equal+larger)