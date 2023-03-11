from tkinter import *
from functools import partial

res =0
def g1(i):
    global res
    first = int(input1.get())
    second = int(input2.get())
    
    if i=='+':
        res =first+second
    elif i=='-':
        res =first-second
    elif i=='*':
        res =first*second
    elif i=='/':
        res =first/second
    elif i=='=':
        q2.config(text=res)

window = Tk()
window.geometry('650x650')
q = Label(window,text='Calculator',foreground='white',background='black')
q.pack()

input1 = Entry(window)
input1.pack()
input2 = Entry(window)
input2.pack()
btn1 = Button(window,text='+', command= partial(g1,'+'))
btn1.pack()
btn2 = Button(window,text='-', command= partial(g1,'-'))
btn2.pack()
btn3 = Button(window,text='*', command= partial(g1,'*'))
btn3.pack()
btn4 = Button(window,text='/', command= partial(g1,'/'))
btn4.pack()

q1 = Label(window,text='Result:')
q1.pack()
btn5 = Button(window,text='=', command= partial(g1,'='))
btn5.pack()
q2 = Label(window,text="")
q2.pack()

window.mainloop()