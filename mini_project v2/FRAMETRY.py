from tkinter import *
from PIL import Image, ImageTk

root = Tk()
"""
# Create a photoimage object of the image in the path
image1 = Image.open("C:\Users\dmuhd\Documents\GitHub\Trading-Journal\cr.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)
root.mainloop()
"""

root.title("TRADING JOURNAL")
root.geometry("1350x750+0+0")
root.iconbitmap('C:\\Users\\MUHAMMAD IMAN\\Desktop\\SEM 2 UNIMAP\\NMT 12704 PROGRAMING\\miniproject programming\\Trading-Journal\\mini_project v2\\download.ico')
root.config(bg="gray50")
"""image_0=Image.open("C:\\Users\\MUHAMMAD IMAN\\Desktop\\SEM 2 UNIMAP\\NMT 12704 PROGRAMING\\miniproject programming\\Trading-Journal\\mini_project v2\\PNG_transparency_demonstration_1.png")
back_end=ImageTk.PhotoImage(image_0)
labelo=Label(root,Image=back_end)
labelo.place(x=0,y=0)"""
bg=PhotoImage(file="C:\\Users\\MUHAMMAD IMAN\\Desktop\\SEM 2 UNIMAP\\NMT 12704 PROGRAMING\\miniproject programming\\Trading-Journal\\mini_project v2\\PNG_transparency_demonstration_1.png")
my_label = label(root,image=bg)
my_label.place(x=0,y=0,relWith=1,relheight=1)
