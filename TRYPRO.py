from sqlite3 import Time
from tkinter import *
from PIL import Image, ImageTk
#GMBR
window = Tk()
img1 = ImageTk.PhotoImage(Image.open("pip install pillow"))
imgDisplay = Label(window, image = img1)
imgDisplay.pack()
#GMBR
window.geometry("1280x800")
f1 = LabelFrame(window,bg="pink",text="ADD Journal")
f1.pack(side=LEFT)
lblDate = Label(f1, text = "Date :").pack()
Date = Entry(f1, width=50)
Date.pack()
lblTime = Label(f1,text = "Time :").pack()
Time = Text(f1, width=38, height=1)
Time.pack()
lblintrumesnt = Label(f1, text = "intrumesnt :").pack()
intrumesnt = Entry(f1, width=50)
intrumesnt.pack()
window.mainloop()