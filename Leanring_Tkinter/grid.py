# Import everything from the tkinter module
from tkinter import *

# Create an instance of the Tk class, which initializes the Tkinter application
root = Tk()

# Create a Label widget with the parent 'root' and the text 'Hello Henok!'
myLabel1 = Label(root, text='Hello Henok!').grid(row=0, column=0)
myLabel2 = Label(root, text='My name is Henok Gashaw').grid(row=1, column=5)

# Use the pack method to add the Label widget to the window
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)

# Enter the Tkinter event loop to keep the window open and responsive
root.mainloop()
