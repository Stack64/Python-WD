#iterator
'''
mytuple = ('apple','banana','cherry')
myit= iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
'''
#scope
'''
y=10
def f1():
    y =20
    print(y)
    
f1()
print(y)

x =20
def f2():
    global x
    x = 10
    print(x)
    
f2()
print(x)
'''

'''import x
x.f1('sohail')
'''

'''
import sys
sys.path.append('C:\\Users\\Reshma\\OneDrive\\Desktop\\')
print(sys.path)
from index import f2
f2()

'''


