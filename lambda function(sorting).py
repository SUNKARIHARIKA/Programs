#synatax:
  #lambda argements:expression
add=lambda x,y:x+y
print(add(5,3))
pairs=([1,2],[4,5],[7,8],[2,0],[5,2])
#sorting the pairs based on the first index
sorted_pairs=sorted(pairs,key=lambda pair:pair[0])
print(sorted_pairs)
#sorting the pairs based on the second index
sorted_pairs1=sorted(pairs,key=lambda x:x[1])
print(sorted_pairs1)
#sorting the pairs based on the first index if it is same sort based on the second index
x=([1,2],[1,4],[3,8],[3,0],[5,6],[9,8])
sorted_pairs2=sorted(x,key=lambda y:(y[0],y[1]))
print(sorted_pairs2)
#sorting the dictionary
dict={'1':'9','5':'0','4':'3'}
sorted_pairs3=sorted(dict.items(),key=lambda z:z[1])
print(sorted_pairs3)
#use of map() function + lambda
#if we want to apply any operation to all the elements present in list tuple or any other iterable
l=[1,2,3,4,5]
squared=list(map(lambda x: x**2,l))
print(squared)
#finding the minimum eleemnt based on first index using lambda
l2=[(1,2),(0,6),(8,9),(6,7)]
minimum=min(l2,key=lambda x:x[0])
print(minimum)
#finding maximum element based on the second index using lambda
l3=[(1,2),(6,7),(8,9),(4,5)]
maximum=max(l3,key=lambda x:x[1])
print(maximum)
#sort function by default return in asceneding order to return in descending order (reverse=True)
pairs1=([1,4],[1,5],[6,7],[8,9],[10,11])
sorted_list5=sorted(pairs1,key=lambda x:x[0],reverse=True)
print(sorted_list5)
#if we want to sort first index in incresing order and second index in decresing order
sorted_list6=sorted(pairs1,key=lambda x:(x[0],-x[1]))
print(sorted_list6)