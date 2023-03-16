import numpy as np

'''
l1 = np.array([1,3,4,5,8])
print(l1)
'''

#type of array
'''
print(l1.dtype)
'''

#check the dimension of array
'''
l2 = np.array([1,3,4,5,8],ndmin=5)
print(l2)
'''

#type of class
'''
print(type(l1))
'''
'''
l1 = np.array([[[1,3,4,5,11,14],[4,2,5,9,16,19],[1,6,5,15,21,17]]])
'''
'''
print(l1[0,1::2])
print(l1[1,::-2])
'''

'''
l1 = np.array([[[1,2],
                [3,4]],
               [[5,6],
                [7,8]]])

print(l1)
print(l1.ndim)
'''
'''
s1= np.array([1,2,3],dtype='str')
print(s1)
'''
'''
s2= np.array([1,2,0,1,0])
s2.astype(str)
print(s2)
'''
'''
a=np.zeros((3,2))
print(a)
b=np.ones((4,3))
print(b)
'''

#arange = list of range
'''
a1 = np.arange(2,6)
print(a1)
'''

#linspace = it will divide the range in equal parts 
'''
a2 = np.linspace(1,4,9)
for i in a2:
    print(i)
'''  

#Addition,substraction,multiply,division,square root of arrays
'''
q1 = np.array([1,5,9])
q2 = np.array([3,7,3])
a = np.add(q1,q2)
print(a)
b= np.subtract(q1,q2)
print(b)
c = np.multiply(q1,q2)
print(c)
d = np.divide(q1,q2)
print(d)
e = np.sqrt(q2)
print(e)
'''
