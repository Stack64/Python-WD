'''
#Q1
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
'''
#Q2
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
'''
#Q3
54321
4321
321
21
1
'''
'''
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
'''
'''
#Q4
11111
2222
333
44
5
'''
'''
for i in range(1,6):
    for j in range(6-i,0,-1):
        print(i,end=" ")
    print()
'''
'''
#Q5
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2 
0 1
'''
'''
for i in range(5,0,-1):
    for j in range(0,i+1):
        print(j,end=' ')
    print()
'''
'''
#Q6
1
33
555
7777
99999
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i*2-1,end=' ')
    print()
'''
'''
#Q7
55555
4444
333
22
1
'''
'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
'''
#Q8
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 

'''
'''
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
'''
#Q9
     *
    * *
   * * *
  * * * *
 * * * * *
'''
'''
for i in range(0,5):
    for j in range(0,5-i):
        print('',end=' ')
    for j in range(0,i+1):
        print('*',end=' ')
    print("")
'''
'''
#Q10
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
'''

'''
for i in range(5,-1,-1):
    for j in range(5-i,0,-1):
        print('',end=' ')
    for j in range(0,i+1):
        print('*',end=' ')
    print("")
'''