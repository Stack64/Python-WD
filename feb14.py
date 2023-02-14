#Control Statements
#Decision Making (Continue)

#nested if else
'''
n=int(input('enter the no. : '))
if n%3==0:
    if n%4==0:
        print('Number is divisible by 12')
    else:
        print('No. is not divisible by 4 but divisble by 3')
else:
    print('No. is not divisble by 12')
    
'''

#using logoical Operators 
# and , or , not

'''
n=int(input('enter the no. : '))
if n%3==0 and n%4==0:
    print('no. is divisble by 12')
else:
    print('no. is not divisble by 12')
    
'''

#Q3 
#smarks = int(input('Enter the Student Marks'))
'''
math = int(input('Enter the Maths marks'))
ss= int(input('Enter the Social Studies marks'))
eng =int(input('Enter the English marks'))
sci = int(input('Enter the Science marks'))
if math >45 and ss >45 :
    print('passed in math and social studies')
elif sci>80:
    print('passed in science')
elif eng<30:
    print('fail in english')
else:
    print('fail')
'''

#Q4
'''
bike = input('Enter the Bike name: ' )
if bike =='duke':
    print('this is owned by KTM')
elif bike =='pulsar':
    print('this is owned by bajaj')
elif bike=='bullet':
    print('this is owned by Royal Enfield')
elif bike=='Harley':
    print('this is owned by Davidson')
else:
    print('this is owned by owned By ME')
'''

#Q5 (Switch question)
'''
tiers = int(input('Enter the no. of tiers : '))
if tiers==2:
    print('bike')
elif tiers==3:
    print('autorickhaw')
elif tiers==4:
    print('car')
elif tiers==5 or tiers==6:
    print('bus or truck')
else:
    print('invalid')
'''
    
#short hand if  
'''
n= int(input('enter the no.'))
if n>18 : print('n is greater than 18')'''

#print('even') if n%2==0 else print('odd')

'''n= int(input('enter the no.'))
print('postive') if n>0 else print('zero') if n==0 else print('negative')'''

'''
a = 30
b = 30
print("A") if a > b else print("=") if a == b else print("B")
'''