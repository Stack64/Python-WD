#                      Control Statements
'''                           |
      1                       2                         3
Decision Making           iteration                Jump statement
if else                    for loop                   break
if else ladder             while loop                 padss
Nested if                                            continue 
switch                                                go
'''


#Decision Making 

# if else
'''
a=20
b=40
if a>b :
    print(a)
else:
    print(b)
    '''
#if else ladder 
'''
a=60
b=60
if a>b:
    print('a is greater')
elif a==b:
    print('both are equal')
else:
    print('b is greater')
'''


'''a = -5'''
'''a = int(input('Enter the number = '))
if a>0:
  print('a is postive')
elif a<0:
  print('a is negative')
else:
  print('a is zero')
'''
  
''' 
#Nested if else 
age=int(input('Enter the age : '))
if age>18:
  weight=float(input('Enter the weight : '))
  if weight>46:
    print('person is eligible to donate blood')
  else :
    print('weight is below mentioned category')
else:
  print('Not eligible to 'donate blood')
'''
'''
#Q1
age=int(input('Enter the age : '))
if age>18:
  voterid=(input('Enter the voter id : '))
  if voterid=='yes':
    print('person is eligible to vote')
  else :
    print('person is not eligible to vote')
else:
  print('age is less than voting age limit')
'''
'''
#Q2
n=int(input('Enter the no. : '))
if n%2==0:
  print('even')
else:
  print('odd')
'''