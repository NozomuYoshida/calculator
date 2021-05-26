from tkinter import *

root = Tk()

root.geometry('430x500')

expression = ''

def set_expression(number):
    global expression
    expression = expression + str(number)
    value.set(expression)
    
def calculator():
    try:
        global expression
        answer = str(eval(expression))
        value.set(answer)
    except:
        value.set('Enter correct expression')    
        expression = ''

def clear():
    global expression
    expression = ''
    value.set(expression)

large_font = ('Verdana', 15)
small_font = ('verdana', 10)

value = StringVar(value='Enter expression')

Entry(root, textvariable=value, font=large_font).grid(row=0, column=0, columnspan=4, ipadx=70)

# fg and bg optins don't work on Mac
#Button(root, text="+", fg='red', command=lambda:
#   set_expression("+"), height=4,width=8).grid(row=1,column=0,pady=10)


Button(root, text="+", highlightbackground='black', command=lambda:
    set_expression("+"), height=4,width=8).grid(row=1,column=0,pady=10)
Button(root, text="-", highlightbackground='black', command=lambda:
    set_expression("-"), height=4, width=8).grid(row=2, column=0, pady=10)
Button(root, text="X", highlightbackground='black', command=lambda: 
    set_expression("*"), height=4, width=8).grid(row=3, column=0,pady=10)
Button(root, text="/", highlightbackground='black', command=lambda: 
    set_expression("/"), height=4, width=8).grid(row=4, column=0,pady=10)
Button(root, text="1", highlightbackground='black', command=lambda: 
    set_expression("1"), height=4, width=8).grid(row=1, column=1,pady=10)
Button(root, text="2", highlightbackground='black', command=lambda: 
    set_expression("2"), height=4, width=8).grid(row=1, column=2,pady=10)
Button(root, text="3", highlightbackground='black', command=lambda: 
    set_expression("3"), height=4, width=8).grid(row=1, column=3,pady=10)
Button(root, text="4", highlightbackground='black', command=lambda: 
    set_expression("4"), height=4, width=8).grid(row=2, column=1,pady=10)
Button(root, text="5", highlightbackground='black', command=lambda: 
    set_expression("5"), height=4, width=8).grid(row=2, column=2)
Button(root, text="6", highlightbackground='black', command=lambda: 
    set_expression("6"), height=4, width=8).grid(row=2, column=3,pady=10)
Button(root, text="7", highlightbackground='black', command=lambda: 
    set_expression("7"), height=4, width=8).grid(row=3, column=1,pady=10)
Button(root, text="8", highlightbackground='black', command=lambda: 
    set_expression("8"), height=4, width=8).grid(row=3, column=2,pady=10)
Button(root, text="9", highlightbackground='black', command=lambda: 
    set_expression("9"), height=4, width=8).grid(row=3, column=3,pady=10)
Button(root, text="0", highlightbackground='black', command=lambda: 
    set_expression("0"), height=4, width=8).grid(row=4, column=2,pady=10)
Button(root, text=".", highlightbackground='black', command=lambda: 
    set_expression("."), height=4, width=8).grid(row=4, column=1,pady=10)

Button(root, text='=', highlightbackground='black', command=calculator, height=4, width=8).grid(row=4, column=3, pady=10)

Button(root, text='Clear', highlightbackground='black', command=clear, height=4, width=20).grid(row=5, column=1, pady=10)

root.mainloop()









    