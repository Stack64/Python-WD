'''
def f1(n):
    if n%4==0 and n%100==0 and n%400==0:
        return True
    elif n%4==0 and n%100==0:
        return False
    elif n%4==0:
        return True
    else:
        return False
    
print(f1(1900))'''

'''
for i in range(5):
    print(i,end=' ')
'''
'''
def f3(n):
    sum=0
    for i in range(len(str(n))):
        r = n%10
        n=n//10
        sum+=r*(2**i)
    print(sum)
    
f3(101)
'''
'''
s1 = 'HelLo'
s2 = ''

for i in s1:
    if ord(i)>=97:
        s2 += i.upper()
        
    elif ord(i)>65:
        s2 +=i.lower()

print(s2)
    '''
'''
for i in range(0,5):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    
for i in range(5,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()'''

#Another form
'''
x=3
y=2*x-1
c=0

for i in range(1,y+1):
    if i>x:
        c+=2
    print('* '*(i-c))
'''
'''
      *   
    *   *   
  *   *   *   
*   *   *   *   
*   *   *   *   
  *   *   *   
    *   *   
      *   
      *   
    *   *   
  *   *   *   
*   *   *   *   
'''
'''
x=4
y = 2*x-2
for i in range(1,x+1):
    print(' '*y+'*   '*i)
    y=y-2
y=0
for i in range(x,0,-1):
    print(' '*y+'*   '*i)
    y=y+2
x=4
y = 2*x-2
for i in range(1,x+1):
    print(' '*y+'*   '*i)
    y=y-2
'''
'''
        *   
      *   *
    *       *
  *           *
*   *   *   *   *
'''
'''
x=5
y = 2*x-2
c=3
for i in range(1,x+1):
         if i==1 or i==x:
            print(' '*y + "*   "*i)
         else:
             print(' '*y+'*'+' '*c+'*')
             c+=4
         y=y-2
'''