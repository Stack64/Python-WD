#tuple to list
'''t1 = (1,3,5,'sh','jdj')
l1 = list(t1)
print(l1)
print(type(l1))'''
#String 
'''s = 'this is python'
print(type(s))
l1 = list(s)
print(l1)
print(type(l1))'''

#l1 = [3,53,'cbd','djhg',8.42,1,True]
#length
'''print(len(l1))
print(l1[4])
print(l1[-5])
print(l1[2:5])
print(l1[-6:-1])'''

'''print(l1[0:])
print(l1[1:])
print(l1[:3])'''
'''
l2 = [0,1,2,3,4,5,6,7,8,9,10.11,12]
print(l2[0:11:3])
'''
#append 
lq = [1,2,3,4,5]
'''print(len(lq))
lq.append(6)
lq.append(7)
print(lq)
print(len(lq))

#insert
lq.insert(2,7)
print(lq)'''
'''lq.insert(1,2)
lq.insert(3,'def')
lq.insert(5,'abc')
#lq.insert(1,2)
print(lq)
print(len(lq))'''

#extend
'''
lq.extend([6,7,8])
print(lq)
print(len(lq))
lq.insert(2,[9,10,11])  
print(lq)
print(len(lq))
print(type(lq[2]))
'''
#Revision
#list - ordered ,allow duplicates ,changeable,len,
'''mylist= [1,2,3,4,5]
print(len(mylist))'''

#The list() Constructor --It is also possible to use the 
# list() constructor when creating a new list.
'''d = list([1,4,5,6,7,3])
print(d)

#acessing the list
print(d[2])
print(d[:4])
print(d[-5:-1])
print(d[1:])
'''
#change List items
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[0:2]= ["kiwi", "mango"]
print(thislist)'''

#Add list Items
# append() function - To add an item to the end of the list, use the append() method
'''
lr = [1,2,3,4]
lr.append(5)
print(lr)
'''

# insert() function - To insert a list item at a specified index, use the insert() method.
'''
lr.insert(2,5)
print(lr) 
'''

#extend List - To append elements from another list to the current list, use the extend() method.
'''
dn = [11,16,17,19,25]
lr.extend(dn)
print(lr)
'''

#Remove Specified Item
#The remove() method removes the specified item.
'''
lr.remove(2)
lr.remove(5)
print(lr)
'''
#Removing specific index -
# The pop() method removes the specified index.
'''
lr.pop(1)
print(lr)
'''

#If you do not specify the index, the pop() method removes the last item.
'''
lr.pop()
print(lr)
'''

#The del keyword also removes the specified index:

'''
del lr[1]
print(lr)
'''

#it can delete whole list 
'''
del lr
print(lr)
'''

#Clear List
#The clear() method empties the list.
#The list still remains, but it has no content.
'''
ln = ['w','t','e','f','c','n']
ln.clear()
print(ln)
'''






'''

#hw
lw = []
3 - 'def'
5 - 'abc'
0 - 'list'
4 - [1,2,3,4]
6 -(7,8,9)
7 - ['list1','list2','list3']
#len
'''

'''lw  = [11]
lw.insert(0,'list')
lw.insert(3,'def')
lw.insert(4,[1,2,3,4])
lw.insert(5,'abc')
lw.insert(6,(7,8,9))
lw.insert(7,['list1','list2','list3'])
print(lw)
print(len(lw))'''