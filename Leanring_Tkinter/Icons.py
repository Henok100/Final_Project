from tkinter import *

root = Tk()
root.title('Learning Icons')
root.iconbitmap('Leanring_Tkinter\ethiopia.ico')

Button_quit = Button(root, text='Exit Program', command=root.quit)
Button_quit.pack()

root.mainloop()