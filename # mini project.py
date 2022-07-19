# mini project
from ast import Lambda
from cProfile import label
from calendar import c
from cgitb import text
from tkinter import *
from tkinter.tix import TEXT
from turtle import bgcolor, right

window = Tk()

window.title("Trading Journal") # title of the app
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
#window.geometry("%dx%d" % (width, height))# fullscreen


# START FRAME ADDJOURNAL ______________________________________________________________________________

ADDJOURNAL = LabelFrame(window, highlightbackground="blue", highlightthickness=2,text='ADD JOURNAL')
ADDJOURNAL.grid(row=0,column=0)    # Frame for add journal



labelINSTRUMENT=Label(ADDJOURNAL,text='INSTRUMENT :',width=50,anchor='w',padx=50,pady=5)
labelINSTRUMENT.grid(row=0,column=0)
de_instrument=Entry(ADDJOURNAL,bd=2,width=30)
de_instrument.grid(row=0,column=0)

labelmarket_position=Label(ADDJOURNAL,text='POSITION :',width=50,anchor='w',padx=50,pady=5)
labelmarket_position.grid(row=1,column=0)
de_market_position=Entry(ADDJOURNAL,bd=2,width=30)
de_market_position.grid(row=1,column=0)

labelLOT_SIZE=Label(ADDJOURNAL,text='LOT_SIZE :',width=50,anchor='w',padx=50,pady=5)
labelLOT_SIZE.grid(row=2,column=0)
de_LOT_SIZE=Entry(ADDJOURNAL,bd=2,width=30)
de_LOT_SIZE.grid(row=2,column=0)

labelRISK=Label(ADDJOURNAL,text='RISK :',width=50,anchor='w',padx=50,pady=5)
labelRISK.grid(row=3,column=0)
de_RISK=Entry(ADDJOURNAL,bd=2,width=30)
de_RISK.grid(row=3,column=0)

labelREWARD=Label(ADDJOURNAL,text='REWARD :',width=50,anchor='w',padx=50,pady=5)
labelREWARD.grid(row=4,column=0)
de_REWARD=Entry(ADDJOURNAL,bd=2,width=30)
de_REWARD.grid(row=4,column=0)

labelPROFIT=Label(ADDJOURNAL,text='PROFIT :',width=50,anchor='w',padx=50,pady=5)
labelPROFIT.grid(row=5,column=0)
de_PROFIT=Entry(ADDJOURNAL,bd=2,width=30)
de_PROFIT.grid(row=5,column=0)

labelLOSS=Label(ADDJOURNAL,text='LOSS :',width=50,anchor='w',padx=50,pady=5)
labelLOSS.grid(row=6,column=0)
de_LOSS=Entry(ADDJOURNAL,bd=2,width=30)
de_LOSS.grid(row=6,column=0)

labelSETUP=Label(ADDJOURNAL,text='SETUP :',width=50,anchor='w',padx=50,pady=5)
labelSETUP.grid(row=7,column=0)
de_SETUP=Entry(ADDJOURNAL,bd=2,width=30)
de_SETUP.grid(row=7,column=0)


# END FRAME ADDJOURNAL__________________________________________________________________________

# START FRAME DASHBOARDPERFOMANCE________________________________________________________________________

FRAMEPERFOMANCE = LabelFrame(window, highlightbackground="gray23", highlightthickness=1,text='DASH BOARDPERFOMANCE',bg='wheat1')
FRAMEPERFOMANCE.grid(row=0,column=1,padx=10)    # Frame for PERFOMANCE BOARDDASH

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

# START FRAME DASHBOARDPERFOMANCE________________________________________________________________________

JOURNAL = LabelFrame(window, highlightbackground="gray23", highlightthickness=1,text='JOURNAL HISTORY',bg='wheat1')
JOURNAL.grid(row=2,column=0,columnspan=3,padx=10)    # Frame for PERFOMANCE BOARDDASH

textboxarea=Text(JOURNAL,height=25,width=100,bg='wheat1')
textboxarea.pack()

# END FRAME PERFOMANCE__________________________________________________________________________


window.mainloop() #mainloop // kalau mainloop tak ada coding tak jalan
#last try
#pundek punya github
<<<<<<< HEAD
#try
=======
#tambah ayat
#akjsnxkanskjxdnkasjnx
#iman hensem
>>>>>>> acab9d29502aefefa1cef9c31b3cb48fb1f3ec58
