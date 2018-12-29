import time
import tkinter as tk

tkWindow = tk.Tk()
tkWindow.geometry("250x500")
tkWindow.title("Digital Time")
font = ("Ariel",20)

cetString = tk.StringVar() #CET
estString = tk.StringVar() #CET -6
cstString = tk.StringVar() #CET -7
pstString = tk.StringVar() #CET -9
jstString = tk.StringVar() #CET +8
istString = tk.StringVar() #CET +4:30
chstString = tk.StringVar() #CET +7
awstString = tk.StringVar() #CET +7
acwstString = tk.StringVar() #CET +7:45
acstString = tk.StringVar() #CET +8:30
aestString = tk.StringVar() #CET +9
acdtString = tk.StringVar() #CET +9:30
aedtString = tk.StringVar() #CET +10

tkCET = tk.Label(tkWindow,textvariable=cetString,font=font)
tkEST = tk.Label(tkWindow,textvariable=estString,font=font)
tkCST = tk.Label(tkWindow,textvariable=cstString,font=font)
tkPST = tk.Label(tkWindow,textvariable=pstString,font=font)
tkJST = tk.Label(tkWindow,textvariable=jstString,font=font)
tkIST = tk.Label(tkWindow,textvariable=istString,font=font)
tkCHST = tk.Label(tkWindow,textvariable=chstString,font=font)
tkAWST = tk.Label(tkWindow,textvariable=awstString,font=font)
tkACWST = tk.Label(tkWindow,textvariable=acwstString,font=font)
tkACST = tk.Label(tkWindow,textvariable=acstString,font=font)
tkAEST = tk.Label(tkWindow,textvariable=aestString,font=font)
tkACDT = tk.Label(tkWindow,textvariable=acdtString,font=font)
tkAEDT = tk.Label(tkWindow,textvariable=aedtString,font=font)

tkCETtext = tk.Label(tkWindow,text=' CET: ',font=font)
tkESTtext = tk.Label(tkWindow,text=' EST: ',font=font)
tkCSTtext = tk.Label(tkWindow,text=' CST: ',font=font)
tkPSTtext = tk.Label(tkWindow,text=' PST: ',font=font)
tkJSTtext = tk.Label(tkWindow,text=' JST: ',font=font)
tkISTtext = tk.Label(tkWindow,text=' IST: ',font=font)
tkCHSTtext = tk.Label(tkWindow,text=' CHST: ',font=font)
tkAWSTtext = tk.Label(tkWindow,text=' AWST: ',font=font)
tkACWSTtext = tk.Label(tkWindow,text=' ACWST: ',font=font)
tkACSTtext = tk.Label(tkWindow,text=' ACST: ',font=font)
tkAESTtext = tk.Label(tkWindow,text=' AEST: ',font=font)
tkACDTtext = tk.Label(tkWindow,text=' ACDT: ',font=font)
tkAEDTtext = tk.Label(tkWindow,text=' AEDT: ',font=font)

tkCETtext.grid(column=1, row=1)
tkPSTtext.grid(column=1, row=2)
tkCSTtext.grid(column=1, row=3)
tkESTtext.grid(column=1, row=4)
tkJSTtext.grid(column=1, row=5)
tkISTtext.grid(column=1, row=6)
tkCHSTtext.grid(column=1, row=7)
tkAWSTtext.grid(column=1, row=8)
tkACWSTtext.grid(column=1, row=9)
tkACSTtext.grid(column=1, row=10)
tkAESTtext.grid(column=1, row=11)
tkACDTtext.grid(column=1, row=12)
tkAEDTtext.grid(column=1, row=13)

tkCET.grid(column=2, row=1)
tkPST.grid(column=2, row=2)
tkCST.grid(column=2, row=3)
tkEST.grid(column=2, row=4)
tkJST.grid(column=2, row=5)
tkIST.grid(column=2, row=6)
tkCHST.grid(column=2, row=7)
tkAWST.grid(column=2, row=8)
tkACWST.grid(column=2, row=9)
tkACST.grid(column=2, row=10)
tkAEST.grid(column=2, row=11)
tkACDT.grid(column=2, row=12)
tkAEDT.grid(column=2, row=13)

while True:
    CET = time.time() + 60*60 #CET
    EST = CET - 60*60*6 #CET -6
    CST = CET - 60*60*7 #CET -7
    PST = CET - 60*60*9 #CET -9
    JST = CET + 60*60*8 #CET +8
    IST = CET + 60*60*4.5 #CET +4:30
    CHST = CET + 60*60*7 #CET +7
    AWST = CET + 60*60*7 #CET +7
    ACWST = CET + 60*60*7.75 #CET +7:45
    ACST = CET + 60*60*8.5 #CET +8:30
    AEST = CET + 60*60*9 #CET +9
    ACDT = CET + 60*60*9.5 #CET +9:30
    AEDT = CET + 60*60*10  #CET +10
    
    CET = time.gmtime(CET)
    PST = time.gmtime(PST)
    CST = time.gmtime(CST)
    EST = time.gmtime(EST)
    JST = time.gmtime(JST)
    IST = time.gmtime(IST)
    CHST = time.gmtime(CHST)
    AWST = time.gmtime(AWST)
    ACWST = time.gmtime(ACWST)
    ACST = time.gmtime(ACST)
    AEST = time.gmtime(AEST)
    ACDT = time.gmtime(ACDT)
    AEDT = time.gmtime(AEDT)
    
    CET = time.strftime("%H:%M:%S", CET)
    PST = time.strftime("%H:%M:%S", PST)
    CST = time.strftime("%H:%M:%S", CST)
    EST = time.strftime("%H:%M:%S", EST)
    JST = time.strftime("%H:%M:%S", JST)
    IST = time.strftime("%H:%M:%S", IST)
    CHST = time.strftime("%H:%M:%S", CHST)
    AWST = time.strftime("%H:%M:%S", AWST)
    ACWST = time.strftime("%H:%M:%S", ACWST)
    ACST = time.strftime("%H:%M:%S", ACST)
    AEST = time.strftime("%H:%M:%S", AEST)
    ACDT = time.strftime("%H:%M:%S", ACDT)
    AEDT = time.strftime("%H:%M:%S", AEDT)
    
    cetString.set(CET)
    estString.set(PST)
    cstString.set(CST)
    pstString.set(EST)
    jstString.set(JST)
    istString.set(IST)
    chstString.set(CHST)
    awstString.set(AWST)
    acwstString.set(ACWST)
    acstString.set(ACST)
    aestString.set(AEST)
    acdtString.set(ACDT)
    aedtString.set(AEDT)
    
    tkWindow.update()
    tkWindow.update_idletasks()