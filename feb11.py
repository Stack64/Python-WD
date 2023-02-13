# dictionary
#pop() ,popitem() ,clear() ,del 
'''d1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}'''
'''d1.pop('b')
print(d1)
d1.popitem()
print(d1)
del d1['d']
print(d1)
d1.clear()
print(d1)
del d1
print(d1)
'''

#deleting the element of list in dictionary
'''d2 = {'a':[1,2,3,4],'b':4,'c':7}
del d2['a'][1]
print(d2)'''

#frozenset -immutable 
l1 =[1,2,3,4,5]
t1 =(2,4,6,7,9)
s1 ={1,3,6,13,17}

Sz = frozenset(l1)
print(Sz)

Sz = frozenset(t1)
print(Sz) 

Sz = frozenset(s1)
print(Sz) 