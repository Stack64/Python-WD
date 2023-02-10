#Removing elements or specific element

# remove() function -passing value
k =[1,2,3,4,5]
'''k.remove(5)
print(k)

#pop()  -it will remove the last element
k.pop()
print(k)
#pop(index) - it will remove the element with index no. passed
k.pop(1)
print(k)

k.extend([7,8,9,10])'''
#del function 
'''del k[1]
print(k)'''

#clear() function - it will give empty list
'''k.clear()
print (k)'''

#Membership Operator 
list1 = ['car','bike','bus','train','truck']
list2 = [14,17,9,2,11,53,28,75,61,90]

'''# in 
print('cycle' in list1)
# not in
print('cycle' not in list1)'''
'''
#sort() function
list1.sort()
print(list1)

list2.sort()
print(list2)

#reverse() function
list1.reverse()
print(list1)

list2.reverse()
print(list2)
'''

l3 = [ 23,1,6,32,17,25,8]
'''list3.sort(reverse=True)
print(list3)
'''

#list combining 
# 1 copy()  -it is used copying data in another variable
#l4 =[2,5,1,11,15,8,0,]
'''l5=l4.copy()
print(l5)'''

# +
'''l3 = l3+ l4
print(l3)'''

#extends
'''l3.extend(l4)
print(l3)
'''

#changing list
'''
l6 = ['truck','bus','bike']
l6[1:3] = ['b','c','d']
print(l6)
l6[1:3] = ['b','c','d','e']
print(l6)
l6[1:8] = ['g','n','m']
print(l6)

'''


#end of list here ---------------
'''
sort() --method 
sorted(argruments) --function
'''

'''l6 = [1,12,5,3,14,11,10,20,6]
l5 = sorted(l6)
print(l5) '''

#TUPLE - tuple are sequence data type ,stores heterogenous data and immutable(once declare cannot change later)

'''t1 =(1,2,3.4,'bus','car',7.3,12,'dhh')

print(t1[1])
print(t1[1:4])
print(t1[-2])
print(t1[-5:-3])
print(len(t1))
print(type(t1))
print(t1)

l2 = [1,2,3,4,5]
t3 = tuple(l2)
print(t3)'''

q = (1,2,4,5,8,23,11,15,39,18)
print(len(q))
print(q[1:4])
print(q[2:3])
print(q[:3])
print(q[-6:-2])

q1 = ('dgh')
print(type(q1))

q1 = ('shd',)
print(type(q1))

q2 = (3)
print(type(q2))
q2 = (3,)
print(type(q2))

q3 = (4.5)
print(type(q3))
q3= (3.3,)
print(type(q3))




