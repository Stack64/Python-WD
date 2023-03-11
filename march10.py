from tkinter import *
def f1():
    global str
    str = int(input1.get())+int(input2.get())
    print(str)
    
def f2():
    global str
    str = int(input1.get())-int(input2.get())
    print(str)
    
def f3():
    global str
    str = int(input1.get())*int(input2.get())
    print(str)
    
def f4():
    global str
    str = float(input1.get())//float(input2.get())
    print(str)
    
def f5(i):
    global g1 
    g1= int(input1.get())
    global g2 
    g2= int(input2.get())
    if i=='+':
        print(g1+g2)

window = Tk()
window.geometry('650x650')
q = Label(window,text='Calculator',foreground='white',background='black')
q.pack()
input1 = Entry(window)
input1.pack()
input2 = Entry(window)
input2.pack()
btn = Button(window,text='+', command= f1)
btn.pack()
btn = Button(window,text='-', command= f2)
btn.pack()
btn = Button(window,text='*', command= f3)
btn.pack()
btn = Button(window,text='/', command= f4)
btn.pack()
q1 = Label(window,text='Result')
q1.pack()

window.mainloop()