'''
def f1(a):
    return lambda n : a*n

var1 = f1(2)
print(var1(11))
'''
'''
def f2(a):
    return a*a

print(f2(4))
'''
'''
def f3(s):
   return s[::-1]
print(f3('fgh'))

v1=lambda s: s[::-1]
print(v1('tyu'))
'''
'''
def f4(n):
    print(n)
    if n==0:
       return 
    return f4(n-1)

print(f4(4))
'''
'''
def h2(n):
    if n<=1:
        return n
    else: 
        return h2(n-1)+h2(n-2)

n= int(input('N ='))
for i in range(n):
   print(h2(i),end=' ')
'''
'''
#class and object
class stud:
    def __init__(self,name,rollno):
        self.n = name
        self.r = rollno
    def study(self):
        return self.r *2
        
s1 = stud('john',23)
print(s1.study())
'''