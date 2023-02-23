#how to make function 
'''
def function1():
    print('this is a python')
    
function1()

def addition(x,y):
    sum = x + y
    print(f'the sum of {x} and {y} is',sum)

addition(10,20)
addition(30,40)
'''
'''
def f2(x,y):
    m = x*y
    d = x/y
    print(f'the multiplication of {x} and {y} is',m)
    print(f'the Division of {x} and {y} is',d)

f2(10,5)
f2(5,10)
'''
'''
def f3(x,y):
    sum1= x+y
    return sum1

print(f3(2,4))
'''
#use of yield it become generatir in python
'''
def f4(x,y):
    yield x+y
    yield x-y
    yield x*y
    yield x/y
    
for i in f4(20,5):
    print(i)
  '''  
'''
def f5():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5
  
for i in f5():
    print(i)
    '''
'''
def f5():
  for i in range(1,6):
   yield i
  
for i in f5():
    print(i)
'''

'''
def f5(n):
  for i in range(1,n+1):
   yield i
for i in f5(7):
    print(i)
'''
#check whether number is odd or even
'''
def f6(n):
    if n%2==0:
       print('even')
    else:
       print('odd')
        
f6(5)
'''
#check whether no. is postive or negative or zero
'''
def f7(n):
    if n==0:
       print('zero')
    elif n>0:
       print('postive')
    else:
       print('negative')
f7(-364)
'''
#Anonymous function --->   doesn't have any name
#                   --->   single line function
#                   --->  can take as many argument as possible
#                   --->  syntax       lambda parameters : expression
'''
square = lambda x : x**2
print(square(4))
'''
#multiplication of two number
'''
mul= lambda x,y : x*y
print(mul(4,5))
'''
#triple addition
'''
d = lambda x,y,z : x+y+z
print(d(1,2,3))
'''

#check n is odd or even using lambda function
'''
w = lambda n: print('even') if n%2==0 else print('odd')
w(4)
'''
#check n is postive or negative or zero using lambda function
s = lambda n : print('+ve') if n>0 else print('-ve') if n<0 else print('zero')
s(0)