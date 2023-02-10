#Python String

#1 function length() to find the length 
#of the string
'''
x ='String'
print(len(x))
'''

#2 UpperCase function()
'''
x = 'string'
print(x.upper())
'''

#3 LowerCase function()
'''
x = 'RKNFNMMX'
print(x.lower())
'''

# Slicing
#x [ starting index : ending index]
#ending index does not include

#postive side    [0,1,2,3,4,5]
#negative side  [-6,-5,-4,-3,-2,-1]
'''x = 'Sohail'
print(x[2])
print(x[2:4])
print(x[2:])
print(x[:4])'''

#for Neagative index
#greater index first : smaller index
'''print(x[-3:-1])'''

#for mix Negative : Postive 
#Greater negative index : smaller postive index
'''print(x[-5,2])'''

#String Concatination
#1 adding two string
'''str1 = 'Hi'
str2 = 'Sohail'
print(str1+str2)'''
'''
c = "this is my book"
'''
#2 title function()
#Every word starts with capital letters
'''print(c.title())'''
#3 Capitalize function()
#only first letter of line will be capital
'''print(c.capitalize())'''
#4 strip -removing spaces from front
'''f = '  this is my code'
print(f.strip())'''
'''
#5 split -division
print(f.split())
#6 count function
print(f.count('i'))
#7 find function
print(f.find('my'))
#8 encode 
print(f.encode())
'''

#9 String formating
a = 'i am a student of b.tech {} year'
print(a.format(4))

q = 4
item = 23
price = 50
x = 'I want {} pieces of item {} for {} dollars.'
print(x.format(q,item,price))

#You can use index numbers {0} to be 
#sure the arguments are placed in the
#correct placeholders:

#for Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {} dollars for {0} pieces of item {1}."
print(myorder.format(3, 12, 80))      
# as we are giving maunal indexing for {2} it could not define it automatically
#full automatic or Fully manually

#10 escape function()
#The escape character allows you to use double quotes 
#when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

#escape character generally used
'''
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	   Form Feed	
\ooo	Octal value	
\xhh    Hex value
'''