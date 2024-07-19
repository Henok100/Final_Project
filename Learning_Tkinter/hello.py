# Import everything from the tkinter module
from tkinter import *

# Create an instance of the Tk class, which initializes the Tkinter application
root = Tk()

# Create a Label widget with the parent 'root' and the text 'Hello Henok!'
myLabel = Label(root, text='Hello Henok!')

# Use the pack method to add the Label widget to the window
myLabel.pack()

# Enter the Tkinter event loop to keep the window open and responsive
root.mainloop()
