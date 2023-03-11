#GUI
from tkinter import *
def run():
    print('HELLO WORLD')

def f1():
    global str
    str = input.get()
    print(str)
    
window = Tk()
window.geometry('650x650')
lb = Label(window,text='SOhail')

lb.pack()
btn = Button(window,text='SK', command= run)
btn.pack()
input = Entry(window)
input.pack()
btn = Button(window,text='Submit', command= f1)
btn.pack()


window.mainloop()
