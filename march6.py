'''
class Person:
    def __init__(self,name):
        self.name= name
        print('constructor')
        
    def printName(self):
        print(f'this is my {self.name}')
        
obj = Person('Sohail')
obj.printName()'''

'''
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        a = self.length * self.breadth
        print(f'The area of Rectangle is {a}')      
    
    def parameter(self):
        b = 2*(self.length+self.breadth)
        print(f'The parameter of Rectangle is {b}')  
        
obj = Rectangle(2,5)
obj.area()
obj.parameter()
'''

'''
class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        a = self.num1 + self.num2
        print(f'The addition of n1 and n2 is {a}')      
    
    def sub(self):
        b = self.num1 - self.num2
        print(f'The substraction of n1 and n2 is {b}')  
        
    def mul(self):
        c = self.num1 * self.num2
        print(f'The Multiplication of n1 and n2 is {c}')  
    
    def divi(self):
        d = self.num1 / self.num2
        print(f'The division of n1 and n2 is {d}')  
        
obj = calculator(10,5)
obj.add()
obj.sub()
obj.mul()
obj.divi()'''

'''
class ATM:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposite(self,dp):
        self.balance = self.balance+dp
        print(f'The deposite amount is {dp}')  
        
    def withdraw(self,wd):
        self.balance = self.balance-wd
        print(f'The withdraw amount is {wd}')        
        
    def getBalance(self):
        print(f'The current balance is {self.balance}')   
        
obj = ATM('JoHn',5000)
obj.deposite(100)
obj.withdraw(1000)
obj.getBalance()

'''
class Supermarket:
    item_list = {'milk':30,'bread':50,'eggs':20}
    
    cart = {}
    def __init__(self,customerID):
        self.customerID=customerID
        
    def addItems(self,items,quantity):
        self.cart[items] = quantity
        
    def removeItems(self,items,quantity):
        if self.cart[items]>quantity:
            self.cart[items]-=quantity
        else:
            del self.cart[items]           
    
    def getPrice(self):
        self.price =0
        for i in self.cart:
            self.price +=self.cart[i]*self.item_list[i]
        
        print(self.price)
        
obj = Supermarket(1)
obj.addItems('eggs',3)
obj.removeItems('eggs',2)
obj.getPrice()


