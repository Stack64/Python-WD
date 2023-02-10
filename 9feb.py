#tuple
'''t2 = ()
l1 = list(t2)
l1.append('bus')
l1.append('car')
l1.append('train')
l1.append('bike')
print(len(l1))
print(l1)
print(tuple(l1))'''

'''t2 = ('hd','bd','er','yu','brh','zcs','qwa')
l1 = list(t2)
l1.remove('hd')
print(l1)
l1.pop()
print(l1)
l1.pop(2)
print(l1)
del l1
print(l1)'''

#tuple of tuple 

'''t1  = ((1,2,3),('car','bus','cycle'),'string')
print(t1[0][1])
print(t1)
print(t1[2][4])
print(t1)'''

'''tt1 =(2,5,8,76,43,32)
tt2 = (3,14,19,37,98)
print(tt1+tt2)
#index
e1 = (1,3,6,4,21,25,21,36,22,13,11,21)
print(e1.index(6))
#count
print(e1.count(21))

#delete the tuple
del e1
print(e1)'''

'''r1 = ('lambo','shelby','mustang','rr','nano')
(a,b,c,d,e) =r1
print(r1)
print(c)

r1 = ('lambo','shelby','mustang','rr','nano')
(a,b,c,*d) =r1
print(r1)
print(d)

r1 = ('lambo','shelby','mustang','rr','nano')
(a,b,c,d,e) =r1
print(r1[1:3])
print(a)

r1 = ('lambo','shelby','mustang','rr','nano')
(a,b,c,*d) =r1

print(r1[2:5])
print(d)'''




#Set 

'''s1 = {1,4,13,17,21,12}
print(s1)

s2 = {1,2,3,4,4,5,7,8,9}
print(s2)

s3 = {'abc',3.4,'cv',4,'abc'}
print(s3)'''

#TRUE 1
#FALSE 0
'''s4 = {'abc',True,1,4.5,'hd',0,False}
print(s4)'''

'''#tuple to set conversion
t1 = (1,4,6,2,3,9,6,5,4)
s2 = set(t1)
print(s2)
print(type(s2))
'''
'''#set
#we have add() function
s4 = {1,2,3,4,5}
s4.add(6)
print(s4)

#update() function
s5 = {'abc','def',4,True}
s4.update(s5)
print(s4)
'''
'''
s1 = {'abc','def','hgk',3.4,6}
s2= {'mvk','klg','axz',3,2.6}
s1.update(s2)
print(s1)
'''
'''j1 ={'abd','hrf','jyk','elo'}
k1 =[4,8,21,2,15]
j1.update(k1)
print(j1)

#intersection_update()
h1 = {1,4,2,6,7,10}
f1 = {4,7,19,21,1,5}
h1.intersection_update(f1)
print(h1)'''

'''s1 = {3,(4,5,6),['abc','def','ghj'],{2,3,4}}  #TypeError: unhashable type: 'list'
print(len(s1))
print(type(s1))
print(s1)'''
'''s2 = {(1,2,3),(3,2,1)}          
print(type(s2))
print(s2)'''
'''s3 = {{1,2,3},{3,2,1}}'''     #set in set
#print(type(s3))
