#--------OUTPUT STATEMENTS--------
#single value printing statements
x=10
print("the number is",x)
print("the number is %d"%x)
print(f"the number is {x}")
print("the number is {0}".format(x))
print("the number is {}".format(x))
print("$%7d$"%1122) #---$1122$
print("$%2d$"%1122) #$1122$
print("$7%d$"%1122) #$71122$
#justification(-) is used to allocate values to the left side
print("$%-7d$"%1122) #$1122---$
#padding(0)
print("$%07d$"%1122) #$0001122$
#float values
print("$%5f$"%1122.12345) #$1122.123450$  by default f takes six decimal places
print("$%11f$"%1122.12345) #$1122.123450$
print("$%15f$"%1122.12345) #$----1122.123450$
print("$%5.2f$"%1122.12345) #$1122.12$
print("$%9.2f$"%1122.12345) #$--1122.12$
print("$%.3f$"%1122.12345)  #$1122.123
#multiple value printing statemnts
x,y=10,20
print("the two numbers are",x,y)
print("the two numbers are %d %d"%(x,y))
print("x=%d y=%d"%(x,y))
print(f"the two numbers are {x} {y}")
print("the two numbers are {0} and {1}".format(x,y))

#by default print() function throws cusor to the next line to print in same line end attribute is used
print("hello",end=' ')
print("hi")
#escape characters
print("my name is harika\nmy age is 19")  #new line
print("my name is harika\tmy age is 19")  #tab space
print("my name is harika\\n my age is 19")  #escape the effect of escape character
#repition of string
print(3*'harika')
#sep attribute-used to seperate the values in the output
a,b=15,16
print(x,y,sep=":")
print(x,y,sep="----")
#string printing
name="harika"
print(name)
print("my name is %s"%name)
print("my name is "+name)
print("my name is",name)
print(name[:])
print('hai %20s'%name)
print('hai %-20s'%name)
#character printing
print('%c'%name[0])
#--------INPUT STATEMENTS------
#in python input function is used to take the input from the keyboard which is in the form of string
st1=input("enter input")
print(st1)
#convert input string to integer and float
x=int(input("enter a number"))
print(x)
y=float(input("enter a float value"))
print(y)
#to accept more than one integer in a same line
#for example if we have to read he input line 10 20 30 40
a,b,c,d=[int(x) for x in input().split()]
print(a+b+c+d)






