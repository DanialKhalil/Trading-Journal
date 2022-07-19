# mini project
from ast import Lambda
from cProfile import label
from calendar import c
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter.tix import TEXT
from turtle import bgcolor, right
import time
import tkinter.messagebox
import pickle

# start clock config________________________________________

text_font= ("Boulder", 18, 'bold')
background = "pink"
foreground= "#363529"
border_width = 1

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S %p \n%A %x")
   clock.config(text=time_live) 
   clock.after(2000, digital_clock)

# END clock config________________________________________

window = Tk()

window.title("Trading Journal") # title of the app
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
#window.geometry("%dx%d" % (width, height))# fullscreen



# START FRAME ADDJOURNAL ______________________________________________________________________________
  # START fuction in add journal----------------------------------------------------
space0=" "
def add_task():
    task = de_instrument.get()
    task1 = de_market_position.get()
    task2 = de_LOT_SIZE.get()
    task3 = de_RISK.get()
    task4 = de_REWARD.get()
    task5 = de_PROFIT.get()
    task6 = de_LOSS.get()
    task7 = de_SETUP.get()
    if task != "" and task1 != "":
        textboxarea.insert(tkinter.END,task +space0 +task1 +space0 +task2 
                                        +space0 +task3 +space0 +task4 +space0 
                                        +task5 +space0 +task6 +space0 +task7+time.strftime("%H:%M:%S %p \n%A %x"))
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="please fill all")
def clear():
    de_instrument.delete(0, tkinter.END)
    de_market_position.delete(0, tkinter.END)
    de_LOT_SIZE.delete(0, tkinter.END)
    de_RISK.delete(0, tkinter.END)
    de_REWARD.delete(0, tkinter.END)
    de_PROFIT.delete(0, tkinter.END)
    de_LOSS.delete(0, tkinter.END)
    de_SETUP.delete(0, tkinter.END)
 # END fuction in add journal----------------------------------------------------




ADDJOURNAL = LabelFrame(window, highlightbackground="blue", highlightthickness=2,text='ADD JOURNAL')
ADDJOURNAL.grid(row=0,column=0)    # Frame for add journal



labelINSTRUMENT=Label(ADDJOURNAL,text='INSTRUMENT :',width=10,anchor='w',padx=10,pady=5)
labelINSTRUMENT.grid(row=0,column=0)
de_instrument=Entry(ADDJOURNAL,bd=2,width=50)
de_instrument.grid(row=0,column=1,columnspan=3)

labelmarket_position=Label(ADDJOURNAL,text='POSITION :',width=10,anchor='w',padx=10,pady=5)
labelmarket_position.grid(row=1,column=0)
de_market_position=Entry(ADDJOURNAL,bd=2,width=50)
de_market_position.grid(row=1,column=1)

labelLOT_SIZE=Label(ADDJOURNAL,text='LOT_SIZE :',width=10,anchor='w',padx=10,pady=5)
labelLOT_SIZE.grid(row=2,column=0)
de_LOT_SIZE=Entry(ADDJOURNAL,bd=2,width=50)
de_LOT_SIZE.grid(row=2,column=1)

labelRISK=Label(ADDJOURNAL,text='RISK :',width=10,anchor='w',padx=10,pady=5)
labelRISK.grid(row=3,column=0)
de_RISK=Entry(ADDJOURNAL,bd=2,width=50)
de_RISK.grid(row=3,column=1)

labelREWARD=Label(ADDJOURNAL,text='REWARD :',width=10,anchor='w',padx=10,pady=5)
labelREWARD.grid(row=4,column=0)
de_REWARD=Entry(ADDJOURNAL,bd=2,width=50)
de_REWARD.grid(row=4,column=1)

labelPROFIT=Label(ADDJOURNAL,text='PROFIT :',width=10,anchor='w',padx=10,pady=5)
labelPROFIT.grid(row=5,column=0)
de_PROFIT=Entry(ADDJOURNAL,bd=2,width=50)
de_PROFIT.grid(row=5,column=1)

labelLOSS=Label(ADDJOURNAL,text='LOSS :',width=10,anchor='w',padx=10,pady=5)
labelLOSS.grid(row=6,column=0)
de_LOSS=Entry(ADDJOURNAL,bd=2,width=50)
de_LOSS.grid(row=6,column=1)

labelSETUP=Label(ADDJOURNAL,text='SETUP :',width=10,anchor='w',padx=10,pady=5)
labelSETUP.grid(row=7,column=0)
de_SETUP=Entry(ADDJOURNAL,bd=2,width=50)
de_SETUP.grid(row=7,column=1)


# START button in ADDJOURNAL-------------------------
submitbutton= Button(ADDJOURNAL,text='Submit',bg='pink',command=add_task) #tak buat command lagi
submitbutton.grid(row=8,column=1,sticky=N)

clearbutton= Button(ADDJOURNAL,text='Clear',bg='pink',command=clear) #tak buat command lagi
clearbutton.grid(row=8,column=1,sticky=W)
# END button in ADDJOURNAL-------------------------


# END FRAME ADDJOURNAL__________________________________________________________________________

# START FRAME DASHBOARDPERFOMANCE________________________________________________________________________

FRAMEPERFOMANCE = LabelFrame(window, highlightbackground="gray23", highlightthickness=1,text='DASH BOARDPERFOMANCE',bg='wheat1')
FRAMEPERFOMANCE.grid(row=0,column=1,padx=10)    # Frame for PERFOMANCE BOARDDASH

    #clock
clock = Label(FRAMEPERFOMANCE, font=text_font, bg=background, fg=foreground, bd=border_width) 
clock.pack()

     #total profit_______________________________________
labelPROFIT=Label(FRAMEPERFOMANCE,text='TOTAL PROFIT',width=50,font=25,bg='wheat1')
labelPROFIT.pack()

data_totalprofit=100
label_d_PROFIT=Label(FRAMEPERFOMANCE,text=data_totalprofit,width=50,font=25,bg='wheat1')
label_d_PROFIT.pack()
    #___________________________________________________


      #total loss_______________________________________
labelLOSS=Label(FRAMEPERFOMANCE,text='TOTAL LOSS',font=25,bg='wheat1')
labelLOSS.pack()

data_totalloss=200
label_d_PROFIT=Label(FRAMEPERFOMANCE,text=data_totalloss,width=50,font=25,bg='wheat1')
label_d_PROFIT.pack()
    #___________________________________________________


     #total profit - loss_______________________________________
labelTPL=Label(FRAMEPERFOMANCE,text='TOTAL PROFIT - LOSS ',font=25,bg='wheat1')
labelTPL.pack()

data_totalprofit_loss=data_totalprofit-data_totalloss
label_d_PROFIT=Label(FRAMEPERFOMANCE,text=data_totalprofit_loss,width=50,font=25,bg='wheat1')
label_d_PROFIT.pack()
    #___________________________________________________


SPACE=Label(FRAMEPERFOMANCE,text=" US DOLLAR $ ",font=('ARIAL',10),bg='wheat1')
SPACE.pack()


comment='currency in USD'
label_comment=Label(FRAMEPERFOMANCE,text=comment)
label_comment.pack(side=LEFT)



# END FRAME PERFOMANCE__________________________________________________________________________

# START FRAME JOURNAL________________________________________________________________________

JOURNAL = LabelFrame(window, highlightbackground="gray23", highlightthickness=1,text='JOURNAL HISTORY IMAN POWER',bg='wheat1')
JOURNAL.grid(row=2,column=0,columnspan=3,padx=10)    # Frame for PERFOMANCE BOARDDASH

textboxarea=Listbox(JOURNAL,height=25,width=50,bg='wheat1',font=('ARIAL',12))
textboxarea.grid(row=2,column=0,columnspan=3,padx=10)

my_tree = ttk.Treeview(JOURNAL) # YANG PATUT KAT ATAS !!!!!!!!!!!!!!!!!!!!!!!!!!!

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("Instrument", "Name", "Price", "Quantity")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Instrument", anchor=W, width=200)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("Price", anchor=W, width=150)
my_tree.column("Quantity", anchor=W, width=150)
my_tree.heading("Instrument", text="Instrument", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)
# END FRAME JOURNAL__________________________________________________________________________
    
    

digital_clock()
window.mainloop() #mainloop // kalau mainloop tak ada coding tak jalan
#SAJA
#biasa
