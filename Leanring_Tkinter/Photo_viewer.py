from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning Icons')
root.iconbitmap('Leanring_Tkinter\ethiopia.ico')

my_img = ImageTk.PhotoImage(Image.open("Images/aspen.png"))
my_img_1 = ImageTk.PhotoImage(Image.open("Images/aspen2.png"))
my_img_2 = ImageTk.PhotoImage(Image.open("Images/me1.png"))
my_img_3 = ImageTk.PhotoImage(Image.open("Images/me2.png"))
my_img_4= ImageTk.PhotoImage(Image.open("Images/me3.png"))

Image_list = [my_img, my_img_1, my_img_2, my_img_3, my_img_4]


my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)



Button_quit = Button(root, text='Exit Program', command=root.quit)
Button_quit.pack()

root.mainloop()