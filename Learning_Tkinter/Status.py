from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning Icons')
#root.iconbitmap('Images/ethiopia.ico')

my_img1 = ImageTk.PhotoImage(Image.open('Images/aspen.png'))
my_img2 = ImageTk.PhotoImage(Image.open('Images/aspen2.png'))
my_img3 = ImageTk.PhotoImage(Image.open('Images/me1.png'))
my_img4 = ImageTk.PhotoImage(Image.open('Images/me2.png'))
my_img5 = ImageTk.PhotoImage(Image.open('Images/me3.png'))

Image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text='image 1 of ' + str(len(Image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def back(Img_num):
    global my_label
    global Button_next
    global Button_back

    my_label.grid_forget()
    my_label = Label(image=Image_list[Img_num - 1])
    Button_back = Button(root, text='<<', command=lambda: back(Img_num - 1))
    Button_next = Button(root, text='>>', command=lambda: next(Img_num + 1))

    if Img_num == 1:
        Button_back = Button(root, text='<<', state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    Button_back.grid(row=1, column=0)
    Button_next.grid(row=1, column=2)
    status = Label(root, text='Image ' + str(Img_num) +' of ' + str(len(Image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
def next(Img_num):
    global my_label
    global Button_next
    global Button_back

    my_label.grid_forget()
    my_label = Label(image=Image_list[Img_num-1])
    Button_back = Button(root, text='<<', command=lambda: back(Img_num-1))
    Button_next = Button(root, text='>>', command=lambda: next(Img_num + 1))
    
    if Img_num == 5:
        Button_next = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    Button_back.grid(row=1, column=0)
    Button_next.grid(row=1, column=2)
    status = Label(root, text='Image ' + str(Img_num) +' of ' + str(len(Image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)



Button_back = Button(root, text='<<', command= lambda: back, state=DISABLED)
Button_quit = Button(root, text='Exit Program', command=root.quit)
Button_next = Button(root, text='>>', command= lambda: next(2))


Button_back.grid(row=1, column=0)
Button_quit.grid(row=1, column=1)
Button_next.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()