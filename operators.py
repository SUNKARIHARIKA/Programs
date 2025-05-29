#----OPERATORS------
#1.Arithmetic operators
import math
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
#division-(true division floor division ceil division)
#1.true division-(returns float value)
print(10/5)  #2.0
print(12/5)  #2.4
print(10/2.5)  #4.0
print(-10/2.5) #-4.0
print(-10/-2.5) #4.0
#2.floor division-return largest integer which is less than or equal to quotient
print(10//3)  #3
print(-10//3)  #-4
print(10//-3)  #-4
print(-10//-3) #3
print(10.5//3) #3.0
print(-10.5//3) #-4.0
print(10.5//-3) #-4.0
print(-10.5//-3) #3.0
print(10//5) #2
#ceil()-return the smalles integer greater or equal than quotient
print(math.ceil(10.5)) #11
print(math.ceil(12.2)) #13
#modulus-returns remainder
''' if the left side value is smaller than the right side value the result will left side value
else perform the division reminder will be the results if the values are negative 
then follow the formula a%b = a-(b*(a//b))'''
print(10%5)  #0
print(2%4)  #2
print(-15%3) #0
#power
base=2
exponent=3
print(base**exponent)
print(pow(base,exponent))
#-----RELATIONAL OPERATORS-----
#(>,>=,<,<=,==,!=) returns boolean value either true or false
#------LOGICAL OPERATORS------(logical and,logical or,logical not )
#logical and-returns last expression if all expressions evaluate to true otherwise it returns fistr value that evaluates to false
n1=11
n2=22
rs=n2 and n1>9
print(rs) 
r1=0 and n2 and n1>9
print(r1)
r2=1122 and 13>12 and 0
print(r2) 
r3=0>5 and 11
print(r3)  #false
#logical or-returns the first value that evaluates to true otherwise it returns last value that evaluates to false
r4=55 or 4>6
print(r4) #55
r5=55 or 4<6
print(r5)  #55
print(55>11 or 6) #True
print(0 or 5<4 or 66 or 11>9)  #66
#logical not--negates the value result is either true or false
p=11
r6=not p
print(r6) #false
print(not(11==p))  #false
print(not(-p==11))  #true
#----MEMBERSHIP OPERATORS----(in,not in)
name="harika"
r7='h' in name
print(r7) #True
print('z' in name )
print('i' not in name)
#----IDENTITY OPERATOR---(is,isnot)-used to check wheather two variables have same address or not
h1=1122
print(id(h1))
h2=1122
print(id(h2))
print(h1 is h2) #True
h3="1122"
print(id(h3))
print(h1 is not h3) #true
print(h2 is h3)  #false
#---BITWISE OPERATORS----(&,|,^,>>,<<)
a=25
b=90
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b>>5)
