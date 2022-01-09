import tkinter
from math import *

window = tkinter.Tk()
window.geometry('400x200')
window.configure(bg='grey40')
window.resizable(0,0)
window.title('Summation')

def equation_get():
    global equation
    equation = Eq.get()


Label1 = tkinter.Label(window,text='Equation', bg='grey40', fg='white')
Label1.place(x=5,y=10)
Eq = tkinter.Entry(window, width=40)
Eq.place(x=85,y=10)
entereq = tkinter.Button(window, text='Enter', bg='grey', fg='white', width=8, command=equation_get)
entereq.place(x=333, y=8)


def nums_get():
    global Start
    global End
    if Decimal_var == 0:
        Start = int(Nums1.get())
        End = int(Nums2.get())
    else:
        Start = int(Nums1.get())
        End = int(Nums2.get())

Label2 = tkinter.Label(window, text='Start,Stop', bg='grey40', fg='white')
Label2.place(x=5, y=40)
Nums1 = tkinter.Entry(window, width=5)
Nums1.place(x=85, y=40)
Nums2 = tkinter.Entry(window, width=5)
Nums2.place(x=150, y=40)

Decimal_var = tkinter.IntVar()
Decimal_check = tkinter.Checkbutton(window, text='Decimals in inputs', bg='grey40', variable=Decimal_var,activebackground='black')
Decimal_check.place(x=5, y=70)
Label3 = tkinter.Label(window, text='X, Y', bg='grey40', fg='white',width=10)
Label3.place(x=250,y=40)
numsenter = tkinter.Button(window, text='Enter', bg='grey', fg='white', width=8, command=nums_get)
numsenter.place(x=333, y=38)


def Summation():
    Result = 0
    for number in range(Start, End+1):
        x = number
        Result += eval(equation, {'sqrt': sqrt, 'pow': pow,'x':number,'inf':inf,'e': e})
        Result_Label = tkinter.Label(window, text=Result, width=55)
        Result_Label.place(x=5, y=150)

Execute = tkinter.Button(window, width=10, text='Evaluate', bg='grey', fg='white', command=Summation)
Execute.place(x=5, y=100)










window.mainloop()