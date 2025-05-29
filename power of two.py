#brute force approach - if the binary representation of the number has exactly one set bit then it is power of 2
n=32
print("True" if str(bin(n)).count('1')==1 else "false")
#using operators
print("True" if n&(n-1)==0 else "false")