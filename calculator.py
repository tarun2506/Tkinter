from tkinter import *

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=35, borderwidth = 5 )
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(num):
    # entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))

def button_clear():
    entry.delete(0, END)

def button_add():
    num1 = entry.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(num1)
    entry.delete(0, END)


def button_equal():
    num2 = entry.get()
    entry.delete(0,END)
    
    if math=="Addition":
        entry.insert(0, f_num + int(num2))
    elif math=="Subtraction":
        entry.insert(0, f_num - int(num2))
    elif math=="Multiplication":
        entry.insert(0, f_num * int(num2))
    elif math=="Division":
        entry.insert(0, f_num / int(num2))
    elif math=="Modulus":
        entry.insert(0, f_num % int(num2))
    elif math=="Power":
        entry.insert(0, f_num ** int(num2))

    

def button_subtract():
    num1 = entry.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = int(num1)
    entry.delete(0, END)

def button_multiply():
    num1 = entry.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = int(num1)
    entry.delete(0, END)

def button_divide():
    num1 = entry.get()
    global f_num
    global math
    math = "Division"
    f_num = int(num1)
    entry.delete(0, END)


def button_modulus():
    num1 = entry.get()
    global f_num
    global math
    math = "Modulus"
    f_num = int(num1)
    entry.delete(0, END)


def button_power():
    num1 = entry.get()
    global f_num
    global math
    math = "Power"
    f_num = int(num1)
    entry.delete(0, END)

#Define buttons

button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=29, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=70, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=60, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=30, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=31, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=31, pady=20, command=button_divide)

button_modulus = Button(root, text="%", padx=69, pady=20, command=button_modulus)
button_power = Button(root, text="^", padx=29, pady=20, command=button_power)



#Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_power.grid(row=7, column=0)
button_modulus.grid(row=7, column=1, columnspan=2)




myButton = Button(root, text="Enter your name", pady=10, padx=10, bg="black", fg="green")


root.mainloop()