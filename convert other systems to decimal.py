#converting hexadecimal to decimal
st=input("enter hexadecimal number")
n1=int(st,16)
print(n1)
#converting octal to decimal
st1=input("enter octal string")
n2=int(st1,8)
print(n2)
#converting binary to decimal
st2=input("enter binary number")
n3=int(st2,2)
print(n3)
'''a binary number should be written by prefixing 0b or 0B for exampple 4-0b100
   and a octal number should be written by prefixing 0o or 0o
   hexadecimal number should be written by prefixing 0x or 0X'''
h=0b100
print(int(h))
n1=0b1110010
print(int(n1))
n2=0xa
print(int(n2))
#converting decimal to binary octal hexadecimal
#bin()-is used to convert decimal to binary
#oct()-is used to convert decimal to ocatal
#hex()-is used to convert decimal to hexadecimal
print(bin(4))
print(oct(612))
m=hex(10)
print(m)
#bool data type-True as 1 and 0 as False
a=10>5
print(a)

