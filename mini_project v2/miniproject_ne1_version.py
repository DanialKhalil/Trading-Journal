#frontend
from cProfile import label
from cgitb import text
from tkinter import *
import tkinter.messagebox
from tkinter.tix import Select
import database_config
import time



class journal:

    def __init__(self,root):
        self.root =root
        self.root.title("TRADING JOURNAL")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="gray50")

        instrument = StringVar()
        market_position = StringVar()
        lot_size = StringVar()
        risk = StringVar()
        reward = StringVar()
        profit = StringVar()
        loss = StringVar()
        setup = StringVar()
# --------------------------------------FUNCTIONS-------------------------------------------------------------------
        def reload():
            label_d_PROFIT.config(text=database_config.sum())
            label_d_loss.config(text=database_config.sumofloss())
            label_d_totalprofitloss.config(text=database_config.sum()-database_config.sumofloss())

        
        def iExit():
            iExit = tkinter.messagebox.askyesno("trading journal Database Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def clearData():
            self.txtinstrument.delete(0, END)
            self.txtmarket_position.delete(0, END)
            self.txtLOT_SIZE.delete(0, END)
            self.txtRISK.delete(0, END)
            self.txtREWARD.delete(0, END)
            self.txtPROFIT.delete(0, END)
            self.txtLOSS.delete(0, END)
            self.txtSETUP.delete(0, END)
        def addData():
            if instrument.get() !="" and market_position.get()!="" and lot_size.get() !="" and risk.get() !="" and reward.get() !="" and profit.get() !="" and loss.get()!="" and setup.get()!="":
                L=market_position.get()
                if L.upper()=='BUY' or L.upper()=="SELL" :
                    if(len(instrument.get())!=0):
                        database_config.addStdRec(instrument.get(), market_position.get(), lot_size.get() , risk.get() ,reward.get(), profit.get(), loss.get(), setup.get())
                        journal.delete(0, END)
                        journal.insert(END, (instrument.get(), market_position.get(), lot_size.get(), risk.get(), reward.get(), profit.get(), loss.get(), setup.get()))
                else:
                    tkinter.messagebox.showerror(title="Warning!", message="input position only 'buy' or 'sell'")
            else :
                tkinter.messagebox.showerror(title="Warning!", message="please fill all")
            reload()
        def DisplayData():
            journal.delete(0,END)
            for row in database_config.viewData():
                journal.insert(END, row, str(""))
            reload()

        def JOURNALRec(event):
            global sd
            searchStd= journal.curselection()[0]
            sd = journal.get(searchStd)

            self.txtinstrument.delete(0, END)
            self.txtinstrument.insert(END, sd[1])
            self.txtmarket_position.delete(0, END)
            self.txtmarket_position.insert(END, sd[2])
            self.txtLOT_SIZE.delete(0, END)
            self.txtLOT_SIZE.insert(END, sd[3])
            self.txtRISK.delete(0, END)
            self.txtRISK.insert(END, sd[4])
            self.txtREWARD.delete(0, END)
            self.txtREWARD.insert(END, sd[5])
            self.txtPROFIT.delete(0, END)
            self.txtPROFIT.insert(END, sd[6])
            self.txtLOSS.delete(0, END)
            self.txtLOSS.insert(END, sd[7])
            self.txtSETUP.delete(0, END)
            self.txtSETUP.insert(END, sd[8])
            reload()
        def DeleteData():
            if(len(instrument.get())!=0):
                database_config.deleteRec(sd[0])
                clearData()
                DisplayData()
            reload()
        def searchDatabase():
            journal.delete(0,END)
            for row in database_config.searchData(instrument.get(), market_position.get(), lot_size.get() , risk.get() ,reward.get(), profit.get(), loss.get(), setup.get()):
                journal.insert(END, row, str(""))
            
        def update():
            if instrument.get() !="" and market_position.get()!="" and lot_size.get() !="" and risk.get() !="" and reward.get() !="" and profit.get() !="" and loss.get()!="" and setup.get()!="":
                if (len(market_position.get()) != 0):
                    database_config.deleteRec(sd[0])
                if (len(market_position.get()) != 0):
                    database_config.addStdRec(instrument.get(), market_position.get(), lot_size.get(), risk.get(), reward.get(), profit.get(),loss.get(), setup.get())
                    journal.delete(0, END)
                    journal.insert(END, (instrument.get(), market_position.get(), lot_size.get(), risk.get(), reward.get(), profit.get(), loss.get(), setup.get()))
            else :
                tkinter.messagebox.showwarning(title="Warning!", message="please fill all")
        # start clock config________________________________________

        text_font= ("Boulder", 18, 'bold')
        background = "steel blue"
        foreground= "#363529"
        border_width = 1

        def digital_clock(): 
            time_live = time.strftime("%H:%M:%S %p \n%A %x")
            clock.config(text=time_live) 
            clock.after(2000, digital_clock)

        # END clock config________________________________________

        def cleardatabase():
            icleardatabase = tkinter.messagebox.askyesno("trading journal Database Systems", "Confirm if you want to clear database")
            if icleardatabase > 0:
                database_config.cleardatabase()
                reload()
                clearData()
                journal.delete(0, END)
                return
            
            

#--------------------------------------Frames-----------------------------------------------------------------------__________________________________________________________
        MainFrame = Frame(self.root, bg="gray50")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=54,pady=8, bg="steel blue", relief=RIDGE)
        TitFrame.grid(row=0,column=0)
        self.lblTit = Label(TitFrame ,font=('times new roman',48,'bold'),text="TRADING JOURNAL IKAN BILIS FX",bg="gray50")
        self.lblTit.grid(row=0,column=0)
        ButtonFrame =Frame(MainFrame,bd=2,width=1350,height=70,padx=19,pady=8,bg="gray50",relief =RIDGE)
        ButtonFrame.grid(row=2,column=0)
        DataFrame = Frame(MainFrame, bd=1, width=1500, height=800, padx=20, pady=20, relief=RIDGE,bg="gray50")
        DataFrame.grid(row=1,column=0)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=190,relief=RIDGE,bg="steel blue", font=('times new roman',36,'bold'),text="\tADD JOURNAL\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=400, height=250, padx=140, pady=3, relief=RIDGE,bg="steel blue",font=('times new roman',28,'bold'),text="\t\tJOURNAL\n")
        DataFrameRIGHT.pack(side=RIGHT)

        
        # START FRAME DASHBOARDPERFOMANCE________________________________________________________________________

        FRAMEPERFOMANCE = LabelFrame(MainFrame, highlightbackground="snow", highlightthickness=1,text='DASH BOARDPERFOMANCE',bg='steel blue')
        FRAMEPERFOMANCE.grid(row=3,column=0,padx=10)    # Frame for PERFOMANCE BOARDDASH

            #clock
        clock = Label(FRAMEPERFOMANCE, font=text_font, bg=background, fg=foreground, bd=border_width) 
        clock.pack()

            #total profit_______________________________________
        labelPROFIT=Label(FRAMEPERFOMANCE,text='TOTAL PROFIT',width=50,font=25,bg='steel blue')
        labelPROFIT.pack()

        data_totalprofit=database_config.sum()
        label_d_PROFIT=Label(FRAMEPERFOMANCE,text=data_totalprofit,width=50,font=25,bg='steel blue')
        label_d_PROFIT.pack()
        

            #total loss_______________________________________
        labelLOSS=Label(FRAMEPERFOMANCE,text='TOTAL LOSS',font=25,bg='steel blue')
        labelLOSS.pack()

        data_totalloss=database_config.sumofloss()
        label_d_loss=Label(FRAMEPERFOMANCE,text=data_totalloss,width=50,font=25,bg='steel blue')
        label_d_loss.pack()
            #___________________________________________________


            #total profit - loss_______________________________________
        labelTPL=Label(FRAMEPERFOMANCE,text='TOTAL PROFIT - LOSS ',font=25,bg='steel blue')
        labelTPL.pack()

        data_totalprofit_loss=data_totalprofit-data_totalloss
        label_d_totalprofitloss=Label(FRAMEPERFOMANCE,text=data_totalprofit_loss,width=50,font=25,bg='steel blue')
        label_d_totalprofitloss.pack()
            #___________________________________________________


        SPACE=Label(FRAMEPERFOMANCE,text=" US DOLLAR $ ",font=('ARIAL',10),bg='steel blue')
        SPACE.pack()


        comment='currency in USD'
        label_comment=Label(FRAMEPERFOMANCE,text=comment)
        label_comment.pack(side=LEFT)
            #___________________________________________________

#--------------------------------entries-------------------------------------------------------------------------------------------------
        self.lblinstrument = Label(DataFrameLEFT, font=('times new roman', 10, 'bold'), text="INSTRUMENT:",padx=2,pady=2,bg="Ghost White")
        self.lblinstrument.grid(row=0,column=0,sticky=W)
        self.txtinstrument = Entry(DataFrameLEFT, font=('times new roman', 10, 'bold'), textvariable=instrument, width=39)
        self.txtinstrument.grid(row=0, column=1)

        self.lblmarket_position = Label(DataFrameLEFT, font=('times new roman', 10, 'bold'), text="POSITION:", padx=2, pady=2,bg="Ghost White")
        self.lblmarket_position.grid(row=1, column=0, sticky=W)
        self.txtmarket_position = Entry(DataFrameLEFT, font=('times new roman', 10, 'bold'), textvariable=market_position, width=39)
        self.txtmarket_position.grid(row=1, column=1)

        self.lblLOT_SIZE = Label(DataFrameLEFT, font=('times new roman', 10, 'bold'), text="LOT_SIZE:", padx=2, pady=2,bg="Ghost White")
        self.lblLOT_SIZE.grid(row=2, column=0, sticky=W)
        self.txtLOT_SIZE = Entry(DataFrameLEFT, font=('times new roman', 10, 'bold'), textvariable=lot_size, width=39)
        self.txtLOT_SIZE.grid(row=2, column=1)

        self.lblRISK = Label(DataFrameLEFT, font=('times new roman', 10, 'bold'), text="RISK:", padx=2, pady=2,bg="Ghost White")
        self.lblRISK.grid(row=3, column=0, sticky=W)
        self.txtRISK = Entry(DataFrameLEFT, font=('times new roman', 10, 'bold'), textvariable=risk, width=39)
        self.txtRISK.grid(row=3, column=1)

        self.lblREWARD = Label(DataFrameLEFT, font=('times new roman', 10, 'bold'), text="REWARD:", padx=2, pady=2,bg="Ghost White")
        self.lblREWARD.grid(row=4, column=0, sticky=W)
        self.txtREWARD = Entry(DataFrameLEFT, font=('times new roman', 10, 'bold'), textvariable=reward, width=39)
        self.txtREWARD.grid(row=4, column=1)

        self.lblPROFIT = Label(DataFrameLEFT, font=('times new roman', 10, 'bold'), text="PROFIT:", padx=2, pady=2,bg="Ghost White")
        self.lblPROFIT.grid(row=5, column=0, sticky=W)
        self.txtPROFIT = Entry(DataFrameLEFT, font=('times new roman', 10, 'bold'), textvariable=profit, width=39)
        self.txtPROFIT.grid(row=5, column=1)

        self.lblLOSS = Label(DataFrameLEFT, font=('times new roman', 10, 'bold'), text="LOSS:", padx=2, pady=2,bg="Ghost White")
        self.lblLOSS.grid(row=6, column=0, sticky=W)
        self.txtLOSS = Entry(DataFrameLEFT, font=('times new roman', 10, 'bold'), textvariable=loss, width=39)
        self.txtLOSS.grid(row=6, column=1)

        self.lblSETUP = Label(DataFrameLEFT, font=('times new roman', 10, 'bold'), text="SETUP:", padx=2, pady=2,bg="Ghost White")
        self.lblSETUP.grid(row=7, column=0, sticky=W)
        self.txtSETUP = Entry(DataFrameLEFT, font=('times new roman', 10, 'bold'), textvariable=setup, width=39)
        self.txtSETUP.grid(row=7, column=1)
#--------------------------------------scroll bar and list box----------------------------------------------------------------------------
        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        journal = Listbox(DataFrameRIGHT, width=40, height=10, font=('times new roman', 12, 'bold'),yscrollcommand=scrollbar.set)
        journal.bind('<<ListboxSelect>>',JOURNALRec)
        journal.grid(row=0, column=0, padx=2)
        scrollbar.config(command=journal.yview)
#--------------------------------------buttons-----------------------------------------------------------------------------------------------------------
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 10, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column =0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('times new roman', 10, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('times new roman', 10, 'bold'), height=1, width=10, bd=4,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('times new roman', 10, 'bold'), height=1, width=10, bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('times new roman', 10, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('times new roman', 10, 'bold'), height=1, width=10, bd=4,command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('times new roman', 10, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)

        self.btnExit = Button(ButtonFrame, text="clear database", font=('times new roman', 10, 'bold'), height=1, width=15, bd=4, command=cleardatabase)
        self.btnExit.grid(row=0, column=7)


        digital_clock()
        



root = Tk()
application = journal(root)

root.mainloop()




