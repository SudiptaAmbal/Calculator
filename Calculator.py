from tkinter import *
import math

def click(value):
    ex = screen.get()
    answer = ''

    try:
        if value == '⇐':
            ex = ex[0:len(ex) - 1]
            screen.delete(0, END)
            screen.insert(0, ex)
            return

        elif value == 'x':
            screen.insert(END, '*')
            return

        elif value == '÷':
            screen.insert(END, "/")
            return

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == '∛':
            answer = round(eval(ex) ** (1 / 3))

        elif value == '^':
            screen.insert(END, '**')
            return

        elif value == '!':
            answer = str(math.factorial(int(ex)))

        else:
            screen.insert(END, value)
            return

        screen.delete(0, END)
        screen.insert(0, answer)

    except SystemError:
        pass

def clear(value):
    if value == 'AC':
        screen.delete(0, END)

def equal(value):
    try:
        ex = screen.get()
        answer = ''
        if value == '=':
            answer = eval(ex)
        screen.delete(0, END)
        screen.insert(0, answer)
    except:
        screen.delete(0, END)
        screen.insert(0, "ERROR")

root = Tk()
root.title('Calculator')
root.config(bg='red')
root.geometry('350x361')
root.resizable(width=False,height=False)
# icon = PhotoImage(file= "c_icon.ico")
root.iconbitmap("c_icon.ico")

screen = Entry(root, font=('arial', 20, 'bold'), bg='black', fg='white', bd=9, relief=SUNKEN, width=22)
screen.grid(row=0, column=0, columnspan=5,pady=2)


buttons = [    "!",    "(", ")", "%", "⇐", 
            "x\u00B2", "9", "8", "7", "+",
            "x\u00B3", "6", "5", "4", "-",
               "√",    "3", '2', "1", "x", 
               "∛",    "^", "0", ".", "÷"]
row = 1
column = 0
for i in buttons:
    button = Button(root, width=4, height=1, relief='raised', text=i, bg='teal', fg='white', font=('arial', 18, 'bold'),
                    activebackground='Aquamarine', command=lambda button=i: click(button))
    button.grid(row=row, column=column)
    column += 1
    if column > 4:
        row += 1
        column = 0

button = Button(root, width=11, height=1, relief='raised', text='AC', bg='teal', fg='white',
            font=('arial', 18, 'bold'), activebackground='Aquamarine', command=lambda button='AC': clear(button))
button.place(x=0, y=311)
button = Button(root, width=11, height=1, relief='raised', text='=', bg='#05595B', fg='white',
            font=('arial', 18, 'bold'), activebackground='skyblue', command=lambda button='=': equal(button))
button.place(x=175, y=311)

root.mainloop()