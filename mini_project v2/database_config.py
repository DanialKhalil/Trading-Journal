from re import X
import sqlite3

def journalData():
    con=sqlite3.connect("journal.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS journal(id INTEGER PRIMARY KEY,instrument text, marketposition text, lotsize text, risk text,reward text, profit text,loss text,setup text, time text)")
    con.commit()
    con.close()

def addStdRec(instrument, marketposition, lotsize , risk ,reward, profit, loss, setup,time):
    con = sqlite3.connect("journal.db")
    cur = con.cursor()
    cur.execute("INSERT INTO journal VALUES (NULL,?,?,?,?,?,?,?,?,?) ", (instrument, marketposition, lotsize , risk ,reward, profit, loss, setup,time))
    con.commit()
    con.close()
    
def viewData():
    con = sqlite3.connect("journal.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM journal")
    rows = cur.fetchall()
    con.close()
    return rows
    
def deleteRec(id):
    con = sqlite3.connect("journal.db")
    cur = con.cursor()
    cur.execute("DELETE FROM journal WHERE id=?",(id,))
    con.commit()
    con.close()
    
def searchData(instrument="", marketposition="", lotsize="",risk="", reward="", profit="", loss="", setup="",time=""):
    con = sqlite3.connect("journal.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM journal WHERE instrument=? OR marketposition=? OR lotsize=? OR risk=? OR reward=? OR profit=? OR loss=? OR setup=? OR time=?",(instrument, marketposition, lotsize , risk ,reward, profit, loss, setup,time))
    rows = cur.fetchall()
    con.close()
    return rows
    
def dataUpdate(id,instrument="", marketposition="", lotsize="",risk="", reward="", profit="", loss="", setup=""):
    con = sqlite3.connect("journal.db")
    cur = con.cursor()
    cur.execute("UPDATE journal SET instrument=?, marketposition=?, lotsize=?,risk=?,reward=?,profit=?,loss=?,setup=?,WHERE id=?", (instrument, marketposition, lotsize , risk ,reward, profit, loss, setup,id))
    con.commit()
    con.close()

def sum():
    con = sqlite3.connect("journal.db")
    cur = con.cursor()

    
    cur.execute("select sum(profit) from journal")
    
    my_result=cur.fetchone()
    print("The total score profit is:")
    print(my_result[0])
    x=my_result[0]
    con.close()
    if x==None:
        return(0)
    else :
        return(x)

def sumofloss():
    con = sqlite3.connect("journal.db")
    cur = con.cursor()

    
    cur.execute("select sum(loss) from journal")
    
    my_result=cur.fetchone()
    print("The total score loss is :")
    print(my_result[0])
    x=my_result[0]
    con.close()
    if x==None:
        return(0)
    else:
        return(x)

def cleardatabase ():
    con = sqlite3.connect("journal.db")
    cur = con.cursor()
    cur.execute("DELETE from journal")
    con.commit()

journalData()
