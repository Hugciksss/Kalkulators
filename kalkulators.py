from tkinter import*

mansLogs=Tk()
mansLogs.title('Kalkulators')

def btnClick(number):
    current=e.get()#nolasa skaitli
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)#ievieto displejā
    return 0

def btnCommand(command):
    global number
    global num1#jāiegaumē skaitlis, darība
    global mathOp#matemātiskais operators
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0

e=Entry(mansLogs,width=15,bd=10,font=("Arial Black",20),justify="right")
e.grid(row=0,column=0,columnspan=4)

btn0=Button(mansLogs,text='0',padx='40',pady='20',command=lambda:btnCommand(0))
btn1=Button(mansLogs,text='1',padx='40',pady='20',command=lambda:btnCommand(1))
btn2=Button(mansLogs,text='2',padx='40',pady='20',command=lambda:btnCommand(2))
btn3=Button(mansLogs,text='3',padx='40',pady='20',command=lambda:btnCommand(3))
btn4=Button(mansLogs,text='4',padx='40',pady='20',command=lambda:btnCommand(4))
btn5=Button(mansLogs,text='5',padx='40',pady='20',command=lambda:btnCommand(5))
btn6=Button(mansLogs,text='6',padx='40',pady='20',command=lambda:btnCommand(6))
btn7=Button(mansLogs,text='7',padx='40',pady='20',command=lambda:btnCommand(7))
btn8=Button(mansLogs,text='8',padx='40',pady='20',command=lambda:btnCommand(8))
btn9=Button(mansLogs,text='9',padx='40',pady='20',command=lambda:btnCommand(9))

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn0.grid(row=4,column=0)

btnSask=Button(mansLogs,text='+',padx='40',pady='20')
btnAtn=Button(mansLogs,text='-',padx='40',pady='20')
btnReiz=Button(mansLogs,text='*',padx='40',pady='20')
btnDal=Button(mansLogs,text='/',padx='40',pady='20')
btnC=Button(mansLogs,text='C',padx='40',pady='20')

btnSask.grid(row=1,column=3)
btnAtn.grid(row=2,column=3)
btnReiz.grid(row=3,column=3)
btnDal.grid(row=4,column=3)
btnC.grid(row=4,column=1)

def btnClick(number):
   current=e.get()#nolasa skaitli
   e.delete(0,END)#nodzēš
   newNumber=str(current)+str(number)
   e.insert(0,newNumber)#ievieto displejā
   return 0
 
 










mansLogs.mainloop()