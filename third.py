from tkinter import *

root = Tk()

def myClick():
    mylable = Label(root, text="Look I am working perfectly!")
    mylable.pack()


myButton = Button(root, text="Click Me!", pady=10, padx=10, command=myClick, bg="black", fg="green")
myButton.pack()

root.mainloop()