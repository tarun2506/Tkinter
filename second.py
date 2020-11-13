from tkinter import *

root = Tk()

#Creating a lable widget
mylable1 = Label(root, text="Hello World!")
mylable2 = Label(root, text="Tarun here")
#Displaying it on the window or screen
mylable1.grid(row=0, column=0)
mylable2.grid(row=1, column=1)

root.mainloop()
