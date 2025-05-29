#empty dictionary
d={}
print(type(d))
d1=dict()
print(type(d1))
#different keys may have same value
d3={'a':'3',"b":'3',"c":'4'}
print(d3)
#keys must be unique
d4={'a':'h','b':'3','c':'r','b':'7'} #when duplicate keys are allowed latest key value pair is updated
print(d4)
#same keys and same values
d4={'a':'h','b':'3','c':'r','b':'3'} #when duplicate keys values are allowed only one key value pair will be printed
print(d4)
#accessing values
d5={"name":"harika","htno":"1449","branch":"cse","subject":"python"}
print(d5)  #whole dictionary is accessed
print(d5["name"])
print(d5["subject"])
#adding keys
d5["pi"]=3.14
print(d5)
d5["subject"]="java"
print(d5)
#deleting
del(d5["subject"]) #deleting single key
print(d5)
#del(d5)   #removes the entire dictionary
#d5.clear()  #returns empty dictionary withount any keys
#nested dictionary
plyrs={'p1':{'nm':'rohit','jersy':'45'},
       'p2':{'nm':'virat','jersy':'18'}}
print(plyrs)
for n,j in plyrs.items():
    print(n,j)
#methods in the dictionary
#1.fromkeys()
kys=['name',"htno","subject"]
v="harika"
dict=dict.fromkeys(kys,v)  #is used to create a dictionary with some particular keys specified with a particular value
print(dict)
#2.get() #allows you to access the values of a given key if key is not present returns none
d8={'a':97,'z':122,'A':65,'Z':122,'0':47,'9':57}
print(d8.get("a"))
print(d8.get("a",-1))
print(d8.get(2,-1))  #2 is nor present in dictionary returns the default value -1
print(d8.get(2))  #2 and default value both are not present so return none
#3.keys()-to display a list of values that are present in the dictionary
print(d8.values())
for i in d8.values():
    print(i)
#3.enumerate in dictionary
for i,(j,k) in enumerate(d8.items()):
    print(i,j,k)
#4.pop()-if key is present delete the key else default
#if default is not given and key is not in the dictionary a key error is raised
d8.pop("a")
print(d8)
 #d8.pop("k")
print(d8.pop("k",-1))
#5.popitem()-removes and returns a keyvalue pair from the dictionary
d8.popitem()
print(d8)
#raises error when key is not present
#6.setdafault()-if key is in dictionary return its value if not insert key with a value of default
d9={"fruit":"apple","vegetable":"tomato","juice":"orange"}
print(d9.setdefault("fruit"))
print(d9.setdefault("junk","pizza"))
print(d9)
print(d9.setdefault("drink"))  #none