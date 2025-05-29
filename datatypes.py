#--------DATA TYPES-----
#there are 4 data types in python
#1---The none type--return nothing
#2---Numeric types(int,float,complex)--represents numbers
a=10
print(type(a))
b=12.5
print(type(b))
c=2+4j
print(type(c))
d=str(a)  #converting integer to string
print(type(d))
e=complex(a) #converting integer to complex
print(e)
#adding two complex numbers
c1,c2=map(int,input().split())
c=complex(c1,c2)
d1,d2=map(int,input().split())
d=complex(d1,d2)
print(c+d)
#bool data type-True as 1 and 0 as False
a=10>5
print(a)
print(True+True)  #2
print(True-False)  #1
#3--sequence types()
'''1.string
   2.bytes
   3.bytearray
   4.list
   5.tuple
   6.range'''
#4.set-set data type,frozenset data type,mapping types
'''the frozen set data type is same as the set datatype the main difference is that the elemnts
int the set datatype can be modified whereas the elements in the frozen set cannot be modified'''
#creating frozenset
s={10,20,30,40}
print(s)
fs=frozenset(s)
print(fs)


