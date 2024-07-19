# Import everything from the tkinter module
from tkinter import *

# Create an instance of the Tk class, which initializes the Tkinter application
root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
     
myButton = Button(root, text='Enter Your Name', command=myClick, fg='blue', bg='yellow')
myButton.pack()

root.mainloop() 