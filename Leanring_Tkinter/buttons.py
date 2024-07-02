# Import everything from the tkinter module
from tkinter import *

# Create an instance of the Tk class, which initializes the Tkinter application
root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.pack()
     
myButton = Button(root, text='Click Me!', command=myClick, fg='blue', bg='yellow')
myButton.pack()

# Enter the Tkinter event loop to keep the window open and responsive
root.mainloop() 
