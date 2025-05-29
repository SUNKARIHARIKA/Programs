#<-----ONES COMPLIMENT------>
#ones complement of a decimal number is first we have to convert the number into binary form and flip the bits like 1 changes to 0 and 0 to 1
#python compiler will give different answer because it takes all finite bits where as humans consider only set of bits like 8,16
x=13
print(~x)
#  ~n eqauls to -(n+1)
print(~16)
#<-------TWOS COMPLIMENT------>
#adding one to ones compliment binary form
a=10
print(~a+1)
#<------AND Operator---->
# >> all true means true  >>one false means false
print(13&7)
#<------XOR Operator------>
# >> same bit results to 0 different bit result to 1
print(13^6)
# >>xor of same numbers is 0
print(5^5)