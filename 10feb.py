#set remove
'''s1 = {1,4,5,6,8,2}'''
'''
s1.pop()
print(s1)
'''
#remove method
'''
s1.remove(4)
print(s1)
'''
#discard method 
'''
s1.discard(2)
print(s1)
'''

#intersection - common values
'''
s1 = {1,2,4,55,'abc','def'}
s2 = {4,55,6,7,'def',8}
s1.intersection(s2)
print(s1)'''

#question
'''
s1 ={1,2,3,5,7}
s2 ={2,3,5,7,8}
#print(s1+s2)
l1 = [2,4,6,12,13]
t1 =(1,4,9,10,12)
s1.update(l1)
s1.update(t1)
print(s1)

s1.union(s2)
print(s1)

s1.intersection_update(s2)
print(s2)

del s2
print(s2)'''
'''
a1 ={1,3,5,6,8,12,11,0}
a2 ={5,6,8,12,13,5,7,1}

a3 = a1.intersection(a2)
print(a3)
a1.intersection_update(a2)
print(a1)

a3 = a1.symmetric_difference(a2)
print(a3)

a1.symmetric_difference_update(a2)
print(a1)'''

#dictionary

'''d1 = {'name':['s','m','a','t'],'rollno':(1,2,3,4),'batch':1} 
#if two same key is given in the dictionary then it will override it
d2 = dict({'dq':[1,2,4],'fg':(2,3,4),'rte':3,'rte':4})
print(len(d2))
print(type(d2))
print(d2)
print(d1.keys())
print(d1.values())
print(d1.items())
print(d2)'''

#d1 = {'name':'sohail','rollno':11,'class':'python'}
'''print(d1['class'])
d1['class']='java'
print(d1)
print(d1.values())

#direct update
d1['place'] = 'future finder'
print(d1)

#update
d1.update({'tower':'KB'})
print(d1)'''

   
'''d1.update({'place':'ff','tower':'kb','city':'mohali'})
print(d1)


d1['rollno'] = 1129
print(d1)'''

'''
# Q - 3dict in 1dict 
dx = {'boy1':{'name':'sohail','age':22},'boy2':{'name':'sakib','age':22},'boy3':{'name':'sahil','age':22}}
#acessing value of dict of dict
print(dx['boy1']['name'])

#updating the value of dict of dict
dx['boy2']['name']='john'
print(dx.items())
'''