'''
#Q1
1
0 1
1 0 1
0 1 0 1

'''
'''
for i in range(1,5):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
    
'''

'''
#Q2
****
 ***
  **
   *
'''
'''
for i in range(1,6):
    for j in range(2,i+1):
        print(' ',end=' ')
    for j in range(1,6-i):
        print(' * ',end=' ')
    print()
    '''
'''
#Q3
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
#Q4

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
#Q5
      1
    2 1 2
  3 2 1 2 3
4 3 2 1 2 3 4

'''
'''for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    for j in range(2,i+1):
        print(j,end=' ')
    print()
    '''
'''
#Q6

*             *
* *         * *
* * *     * * *
* * * * * * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *
'''
'''
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=" ")
    for k in range(1,2*(4-i)+1):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=" ")
    print()
    
for i in range(4,0,-1):
    for j in range(1,i+1):
        print('*',end=" ")
    for k in range(1,2*(4-i)+1):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=" ")
    print()
'''