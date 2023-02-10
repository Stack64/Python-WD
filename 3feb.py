'''
Python has the following data types 
built-in by default,in these categories:
1 Text Type:	str
2 Numeric Types:	int, float, complex
3 Sequence Types:	list, tuple, range
4 Mapping Type:	dict
5 Set Types:	    set, frozenset
6 Boolean Type:	bool
7 Binary Types:	bytes, bytearray, memoryview
8 None Type:	    NoneType
'''

#Getting the Data Type
#type() function is used to check the 
# datatype of the Variable 
'''
x =4
print(type(x))
'''
#1 Text Type : str
'''
y ='SOHAIL'
print(type(y))

y = str('hi JOHN')
print(type(y))
'''
#2 Numeric Data Types : int , float ,complex
#2.1 int
'''
z = 3
print(type(z))

z = int(2)
print(type(z))
'''
#2.2 float
'''
s = 4.5
print(type(s))

s = float(3.5)
print(type(s))
'''
#2.3 Complex
'''
x = 3j
print(type(x))

x =complex(8+4j)
print(type(x))
'''

#3 Sequence Types:	list, tuple, range
#3.1 list
'''
x = ['apple','banana','cherry']
print(x)
print(type(x))

x = list(('apple','banana','cherry'))
print(x)
print(type(x))
'''

#3.2 tuple
'''
x = ('john','jimmy','sams')
print(x)
print(type(x))

x = tuple(('dj','sk','rj'))
print(x)
print(type(x))
'''

#3.3 range 
'''
s =range(4)    # range will be from 0 to 1
print(s)
print(type(s))
'''

#4 Mapping Type : dict
'''
c = {"Name" : "Sohail" ,"AGE" : 19}
print(c)
print(type(c))

c = dict(name = 'Abbas', age = 23)
print(c)
print(type(c))
'''
#5 Set Types : set , frozenset
#5.1 set 
'''
x ={"apple","banana","cherry"}
print(x)
print(type(x))

x = set({"apple","cherry","banana"})
print(x)
print(type(x))
'''
#5.2 frozenset
'''
x = frozenset({"apple","banana","cherry"})
print(x)
print(type(x))
'''

#6 Boolean Type : bool
'''
b = True
print(b)
print(type(b))
'''
#7 Binary Types: bytes, bytearray, memoryview
#7.1 bytes
'''
x = b"Hello"
print(x)
print(type(x))

x = bytes(5)
print(x)
print(type(x))
'''

#7.2 bytearray

'''
c = bytearray(5)
print(c)
print(type(c))
'''
#7.3 memoryview
x= memoryview(bytes(5))
print(x)
print(type(x))
#8 None Type: NoneType