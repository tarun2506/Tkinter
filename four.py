from tkinter import *

root = Tk()

entry = Entry(root, width=20, bg="blue", fg="white", borderwidth = 5 )
entry.pack()
entry.insert(0, "Enter your name")


def myClick():
    hello = "Hello " + entry.get()
    mylable = Label(root, text=hello)
    mylable.pack()


myButton = Button(root, text="Enter your name", pady=10, padx=10, command=myClick, bg="black", fg="green")
myButton.pack()

root.mainloop()