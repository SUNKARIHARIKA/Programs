#<-------Analysis of pattern programs------->
'''
pattern program consist of nested loops
1.for the outer loop count the number of lines or number of rows
2.for the inner loop focus on the columns and somehow connect with the rows
3.print ''  inside the inner for loop
4.observe symmetry(optional)
'''
#<-----------Pattern1(Square pattern)----------->
'''
****
****
****
****
'''
n=int(input("enter the number"))
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()
#<-----------Pattern2(right angle traingle)---------------->
'''
*
**
***
****
*****
'''
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()
#<---------------Pattern3(Number Triangle Pattern)------------------->
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
for i in range(n):
    for j in range(1,i+2):
        print(j,end=' ')
    print()
#<-------------Pattern4(Number Pyramid)-------------------->
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
for i in range(n):
    for j in range(i+1):
        print(i+1,end=' ')
    print()
#<-------------Pattern5----------------------->
'''
* * * * *
* * * *
* * *
* *
*
'''
for i in range(n,0,-1):
    print('* '*i)
#another way
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
#another approach
for i in range(n):
    for j in range(n-i):   #total number of rows-row number
        print('*',end=' ')
    print()
#<-----------------Pattern 6------------>
'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
for i in range(n):
    for j in range(1,(n-i)+1):
        print(j,end=' ')
    print()
#for every inverted decreasing pattern the number of elements in each row=(total number of rows-current row)
#<--------------Pattern6-------->
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
observe the pattern the pattern is in the form of space star and space lets analize it(assume n as number of rows)
row no [space,star,space]  
row=0  [4,1,4]
row=1  [3,3,3]
row=2  [2,5,2]
row=3  [1,7,1]
row=4  [0,9,0]   spaces are decresing (n-i-1) stars are increasing (2*i+1) 
'''
for i in range(n):
    #spaces
    for j in range(n-i-1):
        print( '',end='')
    #stars
    for j in range(2*i+1):
        print('*',end='')
    #spaces
    for j in range(n-i-1):
        print(' ',end='')
    print()
#<--------------Pattern7------------>
'''
         * * * * * * * * *
           * * * * * * *
             * * * * *
               * * *
                 *
row no   [space,star,space]
row=0    [0,9,0]
row=1    [1,7,1]
row=2    [2,5,2]
row=3    [3,3,3]
row=4    [4,1,4]  spaces are increasing (i+1) stars are decreasing (2n-(2i+1))
'''
for i in range(n):
    #spaces
    for j in range(i+1):
        print(' ',end='')
    #stars
    for j in range(2*n-(2*i+1)):
        print('*',end='')
    #spaces
    for j in range(i+1):
        print(' ',end='')
    print()
#<-----------Pattern8--------------->
'''
            *
            * *
            * * *
            * * * * 
            * * * * *
            * * * *
            * * *
            * * 
            *
'''
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n-1):
    for j in range((n-1)-i):
        print('*',end=' ')
    print()
#another way
''' To find the another way first observe the symmetry upto 5 rows the number of stars are increasing (n=5) after 5th row the number
ogf stars are decreasing total number of rows= (2*n-1) for outer loop'''
for i in range(2*n-1):
    if i<=(n-1):
        stars=i+1
    else:
        stars=(2*n-i-1)
    print('* '*stars)
#<--------------Pattern9--------->
'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''
for i in range(n):
    if i%2==0:
        for j in range(i+1):
            if j%2==0:
                print('1 ',end='')
            else:
                print('0 ',end='')
        print()
    else:
        for j in range(i+1):
            if j%2==0:
                print('0 ',end='')
            else:
                print('1 ',end='')
        print()
#another way
for i in range(n):
    val=1 if i%2==0 else 0
    for j in range(i+1):
        print(val,end=' ')
        val=1-val
    print()
#<-------------pattern 10--------------->
'''
     1             1
     1 2         2 1
     1 2 3     3 2 1
     1 2 3 4 4 3 2 1
'''
''' n=4 if we analyze the pattern it is in the form of number space number
row no    [number space number]
row=0     [row+1,6,row+1]
row=1     [row+1,4,row+1]
row=2     [row+1,2,row+1]
row=3     [row+1,0,row+1]'''
for i in range(n):
    #number
    for j in range(1,i+2):
        print(j,end='')
    #spaces
    for j in range(2*(n-1-i)):
        print(' ',end='')
    #numbers
    for j in range(i+1,0,-1):
        print(j,end='')
    print()
#<---------------pattern11----------->
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
num=1
for i in range(n):
    for j in range(i+1):
        print(num,end=' ')
        num=num+1
    print()
#<----------------Pattern12------------->
'''
A
AB
ABC
ABCD
ABCDE
'''
for i in range(5):
    alp='A'
    for j in range(i+1):
        print(alp,end=' ')
        alp=chr(ord(alp)+1)
    print()
#<-------------------Pattern13--------------->
'''
A
B B
C C C
D D D D
E E E E E
'''
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=' ')
    print()
#<-----------pattern14------------->
'''
A B C D E
A B C D
A B C
A B
A
'''
for i in range(n):
    alpha='A'
    for j in range(n-i):
        print(alpha,end=' ')
        alpha=chr(ord(alpha)+1)
    print()
#<------------pattern15------------>
'''
E
D E
C D E
B C D E
A B C D E
'''
for i in range(5):
    start=69-i
    for j in range(i+1):
        print(chr(start+j),end=' ')
    print()
#<--------------Pattern16------------>
'''
            * * * * * * * * * *
            * * * *     * * * *
            * * *         * * *
            * *             * *
            *                 *
            *                 *
            * *             * *
            * * *          * * *
            * * * *      * * * *
            * * * * * *  * * * *
'''
#firstly consider upward symmetry is in the form of star space star
'''
row=0   [5,0,5]
row=1   [4,2,4]
row=2   [3,4,3]
row=3   [2,6,2]
row=2   [1,8,1]
'''
for i in range(n):
    #stars
    for j in range(n-i):
        print('*',end='')
    #spaces
    for j in range(2*i):
        print(' ',end='')
    #stars
    for j in range(n-i):
        print('*',end='')
    print()
'''
row=0 [1,8,1]
row=1 [2,6,2]
row=3 [3,4,3]
row=4 [4,2,4]
row=5 [5,0,5]
'''
for i in range(n):
    #stars
    for j in range(i+1):
        print('*',end='')
    #spaces
    for j in range(2*(n-i-1)):
        print(' ',end='')
    #stars
    for j in range(i+1):
        print('*',end='')
    print()
#<------------pattern17---------------->
'''
       *                        *
       *  *                  *  *
       *  *  *            *  *  *
       *  *  *  *      *  *  *  *
       *  *  *  *  * * *  *  *  *
       *  *  *  *      *  *  *  *
       *  *  *            *  *  *
       *  *                  *  *
       *                        *
'''
#there are left and right symmetry 
#left symmetry  [star,space]
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    for j in range(2*(n-i-1)):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()
#right symmetry
for i in range(5-2,-1,-1):
    for j in range(i+1):
        print('*',end='')
    for j in range(2*(n-i-1)):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()






