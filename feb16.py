#Pattern making

#question 1
'''for i in range(1,4):
    for j in range(1,5):
        print('* ',end='')
    print()
'''

#question 2
'''
row = int(input('enter the row: '))
col = int(input('enter the col: '))
for i in range(1,row+1):
    for j in range(1,col+1):
        if i==1 or i==row or j==1 or j==col:
            print('* ',end='')
        else:
            print('  ',end='') 
    print()
'''

#question 3
'''
#row = int(input('enter the row: '))
for i in range(1,5):
    for j in range(1,i+1):
        print('* ',end='')
    print()
'''

#question 4
'''
row = int(input('enter the row: '))
for i in range(5,0,-1):
    for j in range(1,i+1):
        print('* ',end='')
    print()
'''

#question 5
'''
row = int(input('enter the row: ')) 
for i in range(1,row+1):
    for j in range(1,row+1-i):
        print('* ',end='')
    print()
    '''

#question 6
'''
row = int(input('enter the row: ')) 
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
'''
#question 7
'''
row = int(input('enter the row: ')) 
for i in range(1,row+1):
    for j in range(1,i+1):
        print(i," ",end='')
    print()
'''
#question 8
'''
row = int(input('enter the row: ')) 
for i in range(row+1,0,-1):
    for j in range(1,i+1):
        print(i," ",end='')
    print()
'''

#question 9
'''
row = int(input('enter the row: ')) 
for i in range(row+1,0,-1):
    for j in range(1,i+1):
        print(j," ",end='')
    print()
'''
#question 10

'''
row = int(input('enter the row: ')) 
for i in range(row,0,-1):
    for j in range(row,row-i,-1):
        print(j," ",end='')
    print()
'''

#q11
'''row = int(input('enter the row: ')) 
for i in range(row,0,-1):
    for j in range(row,row-i,-1):
        print(j," ",end='')
    print()
    '''
    
#q12
'''size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")'''
    
#q13
'''
row = 5
for i in range(1,row):
    for j in range(1,5-i):
        print(" ",end='')
    for k in range(1,5):
        print('*',end='')
    print()
'''
#q14 pyramid
'''
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,i+1):
        print('* ',end='')
    print()
'''
#q15 rhombus
'''
for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end='')
    for k in range(1,5):
        print('*',end='')
    print()
'''

'''
#Q16 Circle
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
#Q
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
#Q
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
#Q
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
#Q

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
#Q
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
  