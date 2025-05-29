
n=int(input("enter number"))
d=int(input("enter denominator: "))
try:
    q=n/d
    print("Qotient: ",q)
except ZeroDivisionError:
    print("Denominator can not be zero")

try:
    n=int(input("enter number"))
    d=int(input("enter denominator: "))
    q=n/d
    print("Qotient: ",q)
except ZeroDivisionError:
    print("Denominator can not be zero")
except ValueError:
    print("Invalid data type")

#else clause
try:
    n=int(input("enter number"))
    d=int(input("enter denominator: "))
    q=n/d
    print("Qotient: ",q)
except ZeroDivisionError:
    print("Denominator can not be zero")
except ValueError:
    print("Invalid data type")
else:
    print("Successfully Terminating")
