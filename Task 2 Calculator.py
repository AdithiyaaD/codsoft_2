from tkinter import *

root = Tk()
root.title("Calculator")

expression = ""


def number_0(event):
    global expression
    expression = expression + '0'
    screen['text'] = expression


def number_1(event):
    global expression
    expression = expression + '1'
    screen['text'] = expression


def number_2(event):
    global expression
    expression = expression + '2'
    screen['text'] = expression


def number_3(event):
    global expression
    expression = expression + '3'
    screen['text'] = expression


def number_4(event):
    global expression
    expression = expression + '4'
    screen['text'] = expression


def number_5(event):
    global expression
    expression = expression + '5'
    screen['text'] = expression


def number_6(event):
    global expression
    expression = expression + '6'
    screen['text'] = expression


def number_7(event):
    global expression
    expression = expression + '7'
    screen['text'] = expression


def number_8(event):
    global expression
    expression = expression + '8'
    screen['text'] = expression


def number_9(event):
    global expression
    expression = expression + '9'
    screen['text'] = expression


def add_button(event):
    global expression
    expression = expression + '+'
    screen['text'] = expression


def subtract_button(event):
    global expression
    expression = expression + '-'
    screen['text'] = expression


def mutliply_button(event):
    global expression
    expression = expression + '*'
    screen['text'] = expression


def divide_button(event):
    global expression
    expression = expression + '/'
    screen['text'] = expression


def equalto_button(event):
    global expression
    expression = eval(expression)
    screen['text'] = expression


def clear_button(event):
    global expression
    expression = ""
    screen['text'] = 0


screen = Label(root, text="0", width=33, height=6, bg="black", fg="white", font=('Times', 10))
number0 = Button(root, text="0", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number0.bind('<Button-1>', number_0)
number1 = Button(root, text="1", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number1.bind('<Button-1>', number_1)
number2 = Button(root, text="2", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number2.bind('<Button-1>', number_2)
number3 = Button(root, text="3", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number3.bind('<Button-1>', number_3)
number4 = Button(root, text="4", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number4.bind('<Button-1>', number_4)
number5 = Button(root, text="5", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number5.bind('<Button-1>', number_5)
number6 = Button(root, text="6", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number6.bind('<Button-1>', number_6)
number7 = Button(root, text="7", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number7.bind('<Button-1>', number_7)
number8 = Button(root, text="8", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number8.bind('<Button-1>', number_8)
number9 = Button(root, text="9", width=10, height=5, bg="black", fg="white", font=('Times', 10))
number9.bind('<Button-1>', number_9)
addbutton = Button(root, text="+", width=10, height=5, bg="black", fg="white", font=('Times', 10))
addbutton.bind('<Button-1>', add_button)
subtractbutton = Button(root, text="-", width=10, height=5, bg="black", fg="white", font=('Times', 10))
subtractbutton.bind('<Button-1>', subtract_button)
multiplybutton = Button(root, text="*", width=10, height=5, bg="black", fg="white", font=('Times', 10))
multiplybutton.bind('<Button-1>', mutliply_button)
dividebutton = Button(root, text="/", width=10, height=5, bg="black", fg="white", font=('Times', 10))
dividebutton.bind('<Button-1>', divide_button)
equaltobutton = Button(root, text="=", width=10, height=5, bg="blue", fg="white", font=('Times', 10))
equaltobutton.bind('<Button-1>', equalto_button)
clearbutton = Button(root, text="C", width=33, height=5, bg="orange", fg="white", font=('Times', 10))
clearbutton.bind('<Button-1>', clear_button)

screen.grid(row=0, column=0, columnspan=3)
number1.grid(row=1, column=0)
number2.grid(row=1, column=1)
number3.grid(row=1, column=2)
number4.grid(row=2, column=0)
number5.grid(row=2, column=1)
number6.grid(row=2, column=2)
number7.grid(row=3, column=0)
number8.grid(row=3, column=1)
number9.grid(row=3, column=2)
addbutton.grid(row=4, column=0)
number0.grid(row=4, column=1)
subtractbutton.grid(row=4, column=2)
multiplybutton.grid(row=5, column=0)
dividebutton.grid(row=5, column=1)
equaltobutton.grid(row=5, column=2)
clearbutton.grid(row=6, column=0, columnspan=3)

root.mainloop()