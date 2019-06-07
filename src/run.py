""" importing all libraries """
try:
    #python3
    from tkinter import *
except ImportError:
    #python2
    from Tkinter import *
import random
import time

"""TK object"""
frame = Tk()
frame.title("Calci")

"""frame middle"""
w = frame.winfo_reqwidth()
h = frame.winfo_reqheight()
ws = frame.winfo_screenwidth()
hs = frame.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
frame.geometry('420x325+%d+%d' % (x, y))
frame.resizable(False,False)

"""frame creation"""
f = Frame(frame ,width =300,height=250,relief=RAISED)
f.pack(side=TOP)

"""calculator creation"""
equation=StringVar()
values=""

"""click"""
def click(num):
    global values
    values=values + str(num)
    equation.set(values)

"""clear input"""
def clear():
    global values
    values=""
    equation.set("")

"""equal"""
def equal():
    global values
    result=str(eval(values))
    equation.set(result)
    values = ""

"""display equation"""
def display():
    return values


solve=Label(f,font=('Times',15, 'bold'),width = 16,height=2, text="Calculator",bd=2,relief='groove')
solve.grid(row=0,column=0,columnspan=4,sticky="nsew")

"""input box"""
equ_display = Entry(f,font=('ariel' ,25,'bold'),textvariable=equation ,bd=2 ,insertwidth=0,bg="white",justify='right',relief='groove')
equ_display.grid(row=1,column=0,columnspan=4,sticky="nsew")

"""buttons creations"""
button7=Button(f,height=1, width=2,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="grey", command=lambda: click(7) )
button7.grid(row=2,column=0,sticky="nsew")

button8=Button(f,bd=4, height=1, width=2,fg="black", font=('ariel', 20 ,'bold'),text="8",bg="grey", command=lambda: click(8) )
button8.grid(row=2,column=1,sticky="nsew")

button9=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="9",bg="grey", command=lambda: click(9) )
button9.grid(row=2,column=2,sticky="nsew")

division=Button(f,bd=4, fg="black",height=1,width=2, font=('ariel', 20 ,'bold'),text="/",bg="grey", command=lambda: click("/") )
division.grid(row=2,column=3,sticky="nsew")

button4=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="4",bg="grey", command=lambda: click(4) )
button4.grid(row=3,column=0,sticky="nsew")

button5=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="5",bg="grey", command=lambda: click(5) )
button5.grid(row=3,column=1,sticky="nsew")

button6=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="6",bg="grey", command=lambda: click(6) )
button6.grid(row=3,column=2,sticky="nsew")

multiply=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="*",bg="grey", command=lambda: click("*") )
multiply.grid(row=3,column=3,sticky="nsew")

button1=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="1",bg="grey", command=lambda: click(1) )
button1.grid(row=4,column=0,sticky="nsew")

button2=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="2",bg="grey", command=lambda: click(2) )
button2.grid(row=4,column=1,sticky="nsew")

button3=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="3",bg="grey", command=lambda: click(3) )
button3.grid(row=4,column=2,sticky="nsew")

Substraction=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="-",bg="grey", command=lambda: click("-") )
Substraction.grid(row=4,column=3,sticky="nsew")

button0=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="0",bg="grey", command=lambda: click(0) )
button0.grid(row=5,column=0,sticky="nsew")

decimalbtn=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text=".",bg="grey", command=lambda: click(".") )
decimalbtn.grid(row=5,column=1,sticky="nsew")

modbtn=Button(f,bd=4, fg="black",height=1, width=4, font=('ariel', 20 ,'bold'),text="%",bg="grey", command=lambda: click("%") )
modbtn.grid(row=5,column=2,sticky="nsew")

addbtn=Button(f,bd=4, fg="black",height=1, width=4, font=('ariel', 20 ,'bold'),text="+",bg="grey", command=lambda: click("+") )
addbtn.grid(row=5,column=3,sticky="nsew")

equalbtn=Button(f,bd=4,width =7, fg="black",height=1, font=('ariel', 20 ,'bold'),text="=",bg="grey",command=equal)
equalbtn.grid(row=6,column=0,sticky="nsew",columnspan=3)

clearbtn=Button(f,bd=4, fg="black",height=1, width=2, font=('ariel', 20 ,'bold'),text="c",bg="grey", command=clear)
clearbtn.grid(row=6,column=3,sticky="nsew")

f.mainloop()
frame.mainloop()
