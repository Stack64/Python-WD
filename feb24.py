
#nested function: function inside a function is known as nested function
'''def f1():
    def f2():
        print('this is nested function')
        
    f2()    
f1()
'''

'''
def f2():
    x = lambda n : n**2
    print(x(4))
f2()
'''
#Arbitrary arguments
'''
def f1(x,*y):
    print(x,y)
    
f1(10,30,40,50,60)
'''
'''
def f1(x,*y):
    print(x,y[1])
    
f1(10,30,40,50,60)
'''

#manual arguments
'''
def f3(x,y):
    print(x,y)
    
f3(x=81,y=34)
'''
#keyword arguments -->  **kwargs

'''
def f2(**x):
    print(x['rollno'])
    
f2(xname='xyz' , rollno=14, Class='B.tech')
'''
#First Class Function: --> when a function is passed as an argument for another
'''
def f4(x,y):
    def f5(z):
        return x+y+z
    return f5
v1 = f4(2,5)
print(v1(3))
'''
'''
def h1(x,y):
  def h2(z):
    def h3(w):
       return x+y+z+w
    return h3
  return h2
v1 = h1(4,5)
v2 = v1(1)
print(v2(3))
'''

#varible 

#1 local Variable
'''
def f2(x,y):
    sum = x+y
    print(sum)
f2(10,5)
'''

#2 Global Variable
'''
sum=0
def f2(x,y):
    global sum
    sum = x+y
    
f2(10,5)
print(sum)
'''
#OOPs
'''
class details:
    name ='sohail'
    course='python'
    branch='CSE'
    
obj = details()
obj.name = 'Manpreet'
print(obj.name)
'''
'''
class details:
    def info(self,name,course,depart):
        print(f'My name is {name} , my course is {course} and my department is {depart}')
        
obj= details()
obj.info('sohail','btech','IT')
'''