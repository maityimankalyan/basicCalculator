"""This is a basic calculator application to learn basics of GUI programming
"""

from tkinter import *

def btnClick(numbers):
    """Function to run after button click"""
    global operator
    operator += str(numbers)
    text_Input.set(operator)


def btnClear():
    """Function to run after button C or clear"""
    global operator
    operator = ''
    text_Input.set('')


def btnEuqalsInput():
    """Function to run after button Equals ="""
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ''


cal = Tk()
cal.title('Calculator Application')
operator = ''
text_Input = StringVar()
# formating display text
textDisplay = Entry(cal, font=('calibri', 15, 'bold'),
                    textvariable=text_Input, bd=10,
                    insertwidth=4, bg='white',
                    justify='right').grid(columnspan=4)
# Lambda function to create button
createBtn = lambda n, r, c: Button(cal, padx=8, pady=8, bd=4, fg='black', font=('calibri', 15, 'bold'),
                                    text=str(n), bg='white',
                                    command=lambda:btnClick(n)).grid(row=r, column=c)
# top row buttons
btn7 = createBtn(7, 1, 0)
btn8 = createBtn(8, 1, 1)
btn9 = createBtn(9, 1, 2)
btnDev = createBtn('/', 1, 3)
# from top 2nd row buttons
btn4 = createBtn(4, 2, 0)
btn5 = createBtn(5, 2, 1)
btn6 = createBtn(6, 2, 2)
btnMul = createBtn('*', 2, 3)
# 3rd row buttons
btn1 = createBtn(1, 3, 0)
btn2 = createBtn(2, 3, 1)
btn3 = createBtn(3, 3, 2)
btnSub = createBtn('-', 3, 3)
# 4th row buttons
btnClr = Button(cal, padx=8, pady=8, bd=4, fg='black', font=('calibri', 15, 'bold'),
                text='C', bg='white', command=btnClear).grid(row=4, column=0)
btn0 = createBtn(0, 4, 1)
btnEqul = Button(cal, padx=8, pady=8, bd=4, fg='black', font=('calibri', 15, 'bold'),
                text='=', bg='white', command=btnEuqalsInput).grid(row=4, column=2)
btnAdd = createBtn('+', 4, 3)

cal.mainloop()