l1=[1,2,3,4]
l2=[2,3,4,5]
l=zip(l1,l2)
print(list(l))
#suppose if we want to pair the consecutive elements in the list use zip to pair
l3=[1,2,3,4,5,6]
print(list(zip(l3,l3[1:])))
s="Hello userTwooo"
print(s.count(' '))