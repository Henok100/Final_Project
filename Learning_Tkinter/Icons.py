from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning Icons')
root.iconbitmap('/home/henokg/Desktop/Tkinter/Final_Project/Learning_Tkinter/ethiopia.ico')

my_img = ImageTk.PhotoImage(Image.open("Images/aspen.png"))
my_label = Label(image=my_img)
my_label.pack()



Button_quit = Button(root, text='Exit Program', command=root.quit)
Button_quit.pack()

root.mainloop()