#inheritance
'''
class Parent:
    def walk(self):
        print('walking')
        
class child(Parent):
    pass

obj = child()
obj.walk()
'''

'''
class phone:
    def spotify(self):
        print('Music')
    
class android(phone):
    def callreco(self):
        print('call recording')

class iphone(phone):
    def callreco(self):
        print('call recording not allowed')

obj = android()
obj.spotify()
obj.callreco()

obj1 = iphone()
obj1.spotify()
obj1.callreco()
'''

class student:
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks
    
class report(student):
    def result(self):
        self.result =((sum(self.marks)*100) // 500)
        print(self.result,'%')
        
    def isPass(self):
        if self.result >= 33:
            print('passed')
        else:
            print('fail')
    
    def giveGrace(self):
        if self.result <=33 and self.result > 25:   
            print('give grace') 
            print(33-self.result)
        elif self.result <= 25:
            print('no need')
        
obj = report('sohail',[16,19,30,49,22])
obj.result()
obj.isPass()
obj.giveGrace()