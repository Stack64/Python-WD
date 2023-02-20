
'''
#Q1 Circle
  * * *
*       *
*       *
*       *
  * * *
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if (i!=j) and (i+j!=6) and (i==1 or i==5 or j==1 or j==5):
            print('* ',end='')
        else:
            print('  ',end='')
    print()
'''
'''
#Q2
   1
  2 2
 3 3 3
4 4 4 4
'''
'''
for i in range(1,5):
    for j in range(1,5-i):
        print('',end=" ")
    for k in range(i):
        print(i,end=" ")
    print()
'''
'''
#Q3
   1
  1 2
 1 2 3
1 2 3 4
'''
'''
for i in range(1,5):
    n=1
    for k in range(1,5-i):
        print('',end=" ")
    for j in range(1,5):
        if j> i : print("",end=" ")
        else: 
            print(n,end=" ") 
            n+=1
    print()
'''   
'''
#Q4
1
2 3
4 5 6
7 8 9 10
'''
'''
count =1 
for i in range(1,5):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()

'''
'''
#Q5

      1
    2 1 2
  3 2 1 2 3
4 3 2 1 2 3 4
'''
'''
for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for l in range(2,i+1):
        print(l,end=" ")
    print()
'''

'''
#Q6
  * * * *
    * * *
      * *
        *
'''

'''
for i in range(1,6):
    for j in range(1,i+1):
        print(' ',end=" ")
    for j in range(1,6-i):
        print("*",end=" ")
    print('')
'''
   
'''
#Q7
1
0 1
1 0 1
0 1 0 1
'''
'''
for i in range(1,5):
    for j in range(1,i+1):
        if(i+j)%2==0:
            print('1',end=" ")
        else:
            print('0',end=" ")
    print()   
''' 

'''
#Q8
1
01
001
0001
00001

'''
'''
for i in range(1,6):
    for j in range(2,i+1):
        print('0',end='')
    for j in range(i+1,i+2):
        print('1',end="")
    print()
'''
'''
#Q9

0
10
110
1110
11110
'''
'''
for i in range(1,6):
    for j in range(2,i+1):
        print('1',end='')
    for j in range(i+1,i+2):
        print('0',end="")
    print()
'''
'''
#Q10

1
0 1
1 0 1
0 1 0 1
'''
'''
for i in range(1,5):
    for j in range(1,i+1):
        if(i+j)%2==0:
            print('1',end=" ")
        else:
            print('0',end=" ")
    print()   
''' 

'''
#Q11

1
01
001
0001
00001

'''
'''
for i in range(1,6):
    for j in range(2,i+1):
        print('0',end='')
    for j in range(i+1,i+2):
        print('1',end="")
    print()
'''
'''
#Q12

0
10
110
1110
11110
'''
'''
for i in range(1,6):
    for j in range(2,i+1):
        print('1',end='')
    for j in range(i+1,i+2):
        print('0',end="")
    print()
'''
