s={}
print(type(s))  #empty dictionary
s1=set()  #empty set
print(s1)
k=[]
print(type(k))  #empty list
s=()
print(type(s)) #empty tuple
h={1122,"harika",12.3,True,1122,12.3,0.5}
print(h)  #prints the unique elements present in the set in unodered foramt
#m={"meghana",(12,13,14),("help","save"),[12,13]}  #list datatype is not used in the set because of mutable nature of list
m={"meghana",(12,13,14),("help","save")}
print(m)
#looping in set
for i in m:
    print(i)
#enumerate function in set
for i,j in enumerate(m):
    print(i,j)
#methods 
#1.clear()
m.clear()  #empties the set
print(m)
p={"harika",True,12,13.5,1122}
#2.add()
p.add(90)  #adds an element to the set
print(p)
#3.pop()
p.pop()  #removes random element from the set
print(p)
#4.discard
p.discard(90)  #removes a particular element
print(p)
p.discard(78)
print(p)
#5.remove()
p.remove(1122)  #removes a particular element if not found leads to error
print(p)
#p.remove(89)  error
#6.update 
p1={11,22,33,99}
p2={44,55,22,77}
p1.update(p2)
print(p1)
print(p2)
#7.union
print(p1.union(p2)) #doesnot update the set both p1 and p2
print(p1|p2)
#8.intersection
print(p1&p2)
print(p1.intersection(p2))
p1.intersection(p2)
h1={11,22,33,55,99,44}
h2={44,55,77,100,89}
h1.intersection(h2)
print(h1) #doesnot update the sets when we apply intersection union and difference
print(h2)
#9.difference
print(h1-h2)
print(h1.difference(h2)) #return the elements present in h1 but not h2
#10.symmetric_difference
print(h1^h2) #returns the elements that are unique in both the sets that is removes the common elements 
print(h1.symmetric_difference(h2))
h1.symmetric_difference(h2)
print(h1) #doesnot update the set
#11.disjoint
print(h1.isdisjoint(h2)) #returns true if there is no common elements
#12.intersection_update
k1={10,20,30,40}
k2={10,60,20,50,30}
k1.intersection_update(k2)
print(k1) #returns common elements 
print(k2)
#13.difference_update
l1={10,90,80,70}
l2={50,60,30,70,80}
l1.difference_update(l2)
print(l1)
print(l2)
#14.symmetric_difference_update
o1={10,20,90,80,40}
o2={60,90,30,12,69}
o1.symmetric_difference_update(o2)
print(o1)
print(o2)
#15.issubset()  
e1={10,22,33,44}
e2={88,90,78,22,10,22,33,44}
print(e1.issubset(e2)) #return true when every element in set e1 is present in e2
#16.issuperset()
print(e1.issuperset(e2)) #return true if the everey element in the other set is present in the set
print(e2.issuperset(e1))


        
