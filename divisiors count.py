num=21
count=0
for i in range(1,int(num**0.5)+1):
    if num%i==0:
        count+=1
        if i!=num//i:
            count+=1
print(count)
