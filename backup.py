import tkinter  as tk 
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("505x270")  
from time import strftime
def my_time():
    time_string = strftime('%H:%M:%S %p \n %A \n %x') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',52,'bold') # display size and style

l1=tk.Label(my_w,font=my_font,bg='yellow')
l1.grid(row=1,column=1,padx=5,pady=25)


my_time()
my_w.mainloop()
___________________________________________
from tkinter import *
from tkinter.tix import TEXT
from turtle import bgcolor, right
from time import strftime

window = Tk()

@ -61,15 +62,22 @@ labelSETUP=Label(ADDJOURNAL,text='SETUP :',width=50,anchor='w',padx=50,pady=5)
labelSETUP.grid(row=7,column=0)
de_SETUP=Entry(ADDJOURNAL,bd=2,width=30)
de_SETUP.grid(row=7,column=0)


# END FRAME ADDJOURNAL__________________________________________________________________________
#time-------------------------------------(sat xsiap lgi----jgan kcau coding ni lgi)---------------------------------------------------
def my_time():
    time_string = strftime('%H:%M:%S %p') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',52,'bold') # display size and style
l1=Label(window,font=my_font,bg='yellow')
l1.grid(row=3,column=3,padx=5,pady=25)
#------------------------------------------------------------------------------------------------

# START FRAME DASHBOARDPERFOMANCE________________________________________________________________________

FRAMEPERFOMANCE = LabelFrame(window, highlightbackground="gray23", highlightthickness=1,text='DASH BOARDPERFOMANCE',bg='wheat1')
FRAMEPERFOMANCE.grid(row=0,column=1,padx=10)    # Frame for PERFOMANCE BOARDDASH

     #total profit_______________________________________
labelPROFIT=Label(FRAMEPERFOMANCE,text='TOTAL PROFIT',width=50,font=25,bg='wheat1')
labelPROFIT.pack()
@ -123,4 +131,5 @@ textboxarea.pack()


window.mainloop() #mainloop // kalau mainloop tak ada coding tak jalan
my_time()#demi masa