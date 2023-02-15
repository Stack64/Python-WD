#Iteration

#for loop
'''
#for loop in list
l1 = ['abc','def',True,23,1.8]
for i in l1:
    print(i)


#for loop in tuple
l1 = ('abc','def',True,23,1.8)
for i in l1:
    print(i)
    
#for loop in set
l1 = {'abc','def',True,23,1.8}
for i in l1:
    print(i)
'''

#for loop in String
'''
l1 = 'this is string'
for i in l1:
    print(i)
'''

#for loop in dictionary
'''
d1 = {'a':1,'b':2,'c':3,'d':4}
for x in d1:
    print(x)

d1 = {'a':1,'b':2,'c':3,'d':4}
for x in d1.keys():
    print(x)

d1 = {'a':1,'b':2,'c':3,'d':4}
for x in d1.values():
    print(x)

d1 = {'a':1,'b':2,'c':3,'d':4}
for x in d1.items():
    print(x)
'''

#range(start,end)
'''
for i in range(11):
    print(i)

for x in range(1,11):
  print(x)
'''
'''
for x in range(1,22,3):
  print(x)
'''

#nested for loop
'''for w in range(1,4):
    for e in range(1,4):
        print(w,e)
        '''
#pass
'''for i in range(6):
    pass
'''
#break
'''for i in range(6):
    if i==4:
        break
    print(i)
'''
#continue
'''
for i in range(8):
    if i==4:
        continue
    print(i)
'''
'''
l1 = ['alto','bmw','GTR','RR','Swift','Thar']
for x in l1:
  if x == 'RR':
      break
  print(x)
'''
'''
import string

for i in string.ascii_lowercase:
    print(i)
    
for i in string.ascii_uppercase:
    print(i)

for i in range(65,91):
  print(chr(i))

for i in range(97,123):
  print(chr(i))
'''

'''
t1 =(1,2,3,4,5)
t2 =('alto','bmw','RR','GTR','swift')
for i in t1:
    for j in t2:
        print(i,' ',j)
        '''

'''s1 ={1,2,3,4,5}
s2 ={'alto','bmw','RR','GTR','swift'}
for i in s1:
    for j in s2:
        print(i,' ',j)
'''

#Question pattern making
'''
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    print('\r')
'''