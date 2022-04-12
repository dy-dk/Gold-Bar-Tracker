import json
import os
import sys
import tkinter as tk                    
from tkinter import IntVar, StringVar, PhotoImage, ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle


def imgSrc(img):
    if getattr(sys, 'frozen', False):
        filepath = os.path.dirname(sys.executable)
    elif __file__:
        filepath, filename = os.path.split(os.path.realpath(__file__))
    
    return os.path.join(filepath,"img",img) 

def fileSrc(file):
    if getattr(sys, 'frozen', False):
        filepath = os.path.dirname(sys.executable)
    elif __file__:
        filepath, filename = os.path.split(os.path.realpath(__file__))
    return os.path.join(filepath,file) 
  
root = tk.Tk()
root.title("Drop Tracker")
root.iconphoto(True, PhotoImage(file=imgSrc("peek.png")))
root.attributes('-topmost', True)

style = ThemedStyle(root)
style.set_theme("black")

#tab definition
tabControl = ttk.Notebook(root)  

pbhlTab = ttk.Frame(tabControl)
akashaTab = ttk.Frame(tabControl)
gohlTab = ttk.Frame(tabControl)
  
tabControl.add(pbhlTab, text='PBHL')
tabControl.add(akashaTab, text='Akasha')
tabControl.add(gohlTab, text='GOHL')
tabControl.pack(expand=1, fill="both")


#load data from json
with open(fileSrc('data.json')) as file:
    drop = json.load(file)

# counter var def

# Tab PBHL
pbhlraidCount = IntVar(value=drop['pbhl']['raid'])
noblueCount = IntVar(value=drop['pbhl']['noblue'])
pbhlcoronaringCount = IntVar(value=drop['pbhl']['coronaring'])
pbhllineageringCount = IntVar(value=drop['pbhl']['lineagering'])
pbhlintricacyringCount = IntVar(value=drop['pbhl']['intricacyring'])
pbhlgoldbarCount = IntVar(value=drop['pbhl']['goldbar'])
pbhlblueCount = IntVar(value=pbhlraidCount.get()-noblueCount.get())
pbhlbluePercent = StringVar(value="Dokkan")
pbhlblueText = StringVar(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))

# Tab Akasha
raidCount = IntVar(value=drop['akasha']['raid'])
hollowkeyCount = IntVar(value=drop['akasha']['hollowkey'])
coronaringCount = IntVar(value=drop['akasha']['coronaring'])
lineageringCount = IntVar(value=drop['akasha']['lineagering'])
intricacyringCount = IntVar(value=drop['akasha']['intricacyring'])
goldbarCount = IntVar(value=drop['akasha']['goldbar'])

# Tab GOHL
gohlraidCount = IntVar(value=drop['gohl']['raid'])
azuriteCount = IntVar(value=drop['gohl']['azurite'])
gohlcoronaringCount = IntVar(value=drop['gohl']['coronaring'])
gohllineageringCount = IntVar(value=drop['gohl']['lineagering'])
gohlintricacyringCount = IntVar(value=drop['gohl']['intricacyring'])
gohlgoldbarCount = IntVar(value=drop['gohl']['goldbar'])

# PBHL
if pbhlblueCount.get() == 0:
    nobluePercentage = StringVar(value="0.0%")
    pbhlcoronaringPercentage = StringVar(value="0.0%")
    pbhllineageringPercentage = StringVar(value="0.0%")
    pbhlintricacyringPercentage = StringVar(value="0.0%")
    pbhlgoldbarPercentage = StringVar(value="0.0%")
    pbhlbluePercent = StringVar(value="0.0%")
else:
    nobluePercentage = StringVar(value=str(round(noblueCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhlcoronaringPercentage = StringVar(value=str(round(pbhlcoronaringCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhllineageringPercentage = StringVar(value=str(round(pbhllineageringCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhlintricacyringPercentage = StringVar(value=str(round(pbhlintricacyringCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhlgoldbarPercentage = StringVar(value=str(round(pbhlgoldbarCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhlbluePercent = StringVar(value=str(round(pbhlblueCount.get()/pbhlraidCount.get()*100,2)) + "%")

pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))

# akasha
if raidCount.get() == 0:
    hollowkeyPercentage = StringVar(value="0.0%")
    coronaringPercentage = StringVar(value="0.0%")
    lineageringPercentage = StringVar(value="0.0%")
    intricacyringPercentage = StringVar(value="0.0%")
    goldbarPercentage = StringVar(value="0.0%")
else:
    hollowkeyPercentage = StringVar(value=str(round(hollowkeyCount.get()/raidCount.get()*100,2)) + "%")
    coronaringPercentage = StringVar(value=str(round(coronaringCount.get()/raidCount.get()*100,2)) + "%")
    lineageringPercentage = StringVar(value=str(round(lineageringCount.get()/raidCount.get()*100,2)) + "%")
    intricacyringPercentage = StringVar(value=str(round(intricacyringCount.get()/raidCount.get()*100,2)) + "%")
    goldbarPercentage = StringVar(value=str(round(goldbarCount.get()/raidCount.get()*100,2)) + "%")

# gohl
if gohlraidCount.get() == 0:
    azuritePercentage = StringVar(value="0.0%")
    gohlcoronaringPercentage = StringVar(value="0.0%")
    gohllineageringPercentage = StringVar(value="0.0%")
    gohlintricacyringPercentage = StringVar(value="0.0%")
    gohlgoldbarPercentage = StringVar(value="0.0%")
else:
    azuritePercentage = StringVar(value=str(round(azuriteCount.get()/gohlraidCount.get()*100,2)) + "%")
    gohlcoronaringPercentage = StringVar(value=str(round(gohlcoronaringCount.get()/gohlraidCount.get()*100,2)) + "%")
    gohllineageringPercentage = StringVar(value=str(round(gohllineageringCount.get()/gohlraidCount.get()*100,2)) + "%")
    gohlintricacyringPercentage = StringVar(value=str(round(gohlintricacyringCount.get()/gohlraidCount.get()*100,2)) + "%")
    gohlgoldbarPercentage = StringVar(value=str(round(gohlgoldbarCount.get()/gohlraidCount.get()*100,2)) + "%")



#save data to json
def saveData():
    #fixed schema def
    drop = {}
    drop['pbhl'] = {
        'raid': pbhlraidCount.get(),
        'noblue': noblueCount.get(),
        'coronaring': pbhlcoronaringCount.get(),
        'lineagering': pbhllineageringCount.get(),
        'intricacyring': pbhlintricacyringCount.get(),
        'goldbar': pbhlgoldbarCount.get(),
        'hornbefore':pbhlHornLastBarEntry.get(),
        'hornafter':pbhlCurrentHornEntry.get()
    }
    drop['akasha'] = {
        'raid': raidCount.get(),
        'hollowkey': hollowkeyCount.get(),
        'coronaring': coronaringCount.get(),
        'lineagering': lineageringCount.get(),
        'intricacyring': intricacyringCount.get(),
        'goldbar': goldbarCount.get(),
        'keybefore': keyTextBefore.get(),
        'keyafter': keyTextAfter.get(),
    }
    drop['gohl'] = {
        'raid': gohlraidCount.get(),
        'azurite': azuriteCount.get(),
        'coronaring': gohlcoronaringCount.get(),
        'lineagering': gohllineageringCount.get(),
        'intricacyring': gohlintricacyringCount.get(),
        'goldbar': gohlgoldbarCount.get(),
        'azuritebefore': azuriteTextBefore.get(),
        'azuriteafter': azuriteTextAfter.get(),
    }

    with open(fileSrc('data.json'),'w') as file:
        json.dump(drop,file, indent=4)


#pbhl left mouse button
def pbhlCallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    pbhlraidCount.set(pbhlraidCount.get()+1)

    if(item=="noblue"):
        noblueCount.set(noblueCount.get()+1)
    elif(item == "coronaring"):
        pbhlcoronaringCount.set(pbhlcoronaringCount.get()+1)
        pbhlblueCount.set(pbhlblueCount.get()+1)
    elif(item == "lineagering"):
        pbhllineageringCount.set(pbhllineageringCount.get()+1)
        pbhlblueCount.set(pbhlblueCount.get() + 1)
    elif(item == "intricacyring"):
        pbhlintricacyringCount.set(pbhlintricacyringCount.get()+1)
        pbhlblueCount.set(pbhlblueCount.get() + 1)
    elif(item == "goldbar"):
        pbhlgoldbarCount.set(pbhlgoldbarCount.get()+1)
        pbhlblueCount.set(pbhlblueCount.get() + 1)

    pbhlbluePercent.set(value=str(round(pbhlblueCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
    pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))

    if pbhlblueCount.get() == 0:
        pbhlcoronaringPercentage.set("0.0%")
        pbhllineageringPercentage.set("0.0%")
        pbhlintricacyringPercentage.set("0.0%")
        pbhlgoldbarPercentage.set("0.0%")
    else:
        pbhlcoronaringPercentage.set(str(round(pbhlcoronaringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhllineageringPercentage.set(str(round(pbhllineageringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlintricacyringPercentage.set(str(round(pbhlintricacyringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlgoldbarPercentage.set(str(round(pbhlgoldbarCount.get()/pbhlblueCount.get()*100,2)) + "%")

    saveData()


#call back action button
def buttonCallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    raidCount.set(raidCount.get()+1)

    if(item=="hollowkey"):
        hollowkeyCount.set(hollowkeyCount.get()+1)
    elif(item == "coronaring"):
        coronaringCount.set(coronaringCount.get()+1) 
    elif(item == "lineagering"):
        lineageringCount.set(lineageringCount.get()+1)
    elif(item == "intricacyring"):
        intricacyringCount.set(intricacyringCount.get()+1)  
    elif(item == "goldbar"):
        goldbarCount.set(goldbarCount.get()+1) 

    hollowkeyPercentage.set(str(round(hollowkeyCount.get()/raidCount.get()*100,2)) + "%")
    coronaringPercentage.set(str(round(coronaringCount.get()/raidCount.get()*100,2)) + "%") 
    lineageringPercentage.set(str(round(lineageringCount.get()/raidCount.get()*100,2)) + "%")
    intricacyringPercentage.set(str(round(intricacyringCount.get()/raidCount.get()*100,2)) + "%")
    goldbarPercentage.set(str(round(goldbarCount.get()/raidCount.get()*100,2)) + "%")      

    saveData()

#gohl callback button
def gohlCallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    gohlraidCount.set(gohlraidCount.get()+1)

    if(item=="azurite"):
        azuriteCount.set(azuriteCount.get()+1)
    elif(item == "coronaring"):
        gohlcoronaringCount.set(gohlcoronaringCount.get()+1)
    elif(item == "lineagering"):
        gohllineageringCount.set(gohllineageringCount.get()+1)
    elif(item == "intricacyring"):
        gohlintricacyringCount.set(gohlintricacyringCount.get()+1)
    elif(item == "goldbar"):
        gohlgoldbarCount.set(gohlgoldbarCount.get()+1)

    azuritePercentage.set(str(round(azuriteCount.get()/gohlraidCount.get()*100,2)) + "%")
    gohlcoronaringPercentage.set(str(round(gohlcoronaringCount.get()/gohlraidCount.get()*100,2)) + "%")
    gohllineageringPercentage.set(str(round(gohllineageringCount.get()/gohlraidCount.get()*100,2)) + "%")
    gohlintricacyringPercentage.set(str(round(gohlintricacyringCount.get()/gohlraidCount.get()*100,2)) + "%")
    gohlgoldbarPercentage.set(str(round(gohlgoldbarCount.get()/gohlraidCount.get()*100,2)) + "%")

    saveData()

#pbhl back action button
def pbhlTakeBack(item):
    #messagebox.showinfo(item)
    #print(item)


    if(item=="noblue"):
        if noblueCount.get() == 0:
            return
        else:
            noblueCount.set(noblueCount.get()-1)
    elif(item == "coronaring"):
        if pbhlcoronaringCount.get() == 0:
            return
        else:
            pbhlcoronaringCount.set(pbhlcoronaringCount.get()-1)
            pbhlblueCount.set(pbhlblueCount.get() - 1)
    elif(item == "lineagering"):
        if pbhllineageringCount.get() == 0:
            return
        else:
            pbhllineageringCount.set(pbhllineageringCount.get()-1)
            pbhlblueCount.set(pbhlblueCount.get() - 1)
    elif(item == "intricacyring"):
        if pbhlintricacyringCount.get() == 0:
            return
        else:
            pbhlintricacyringCount.set(pbhlintricacyringCount.get()-1)
            pbhlblueCount.set(pbhlblueCount.get() - 1)
    elif(item == "goldbar"):
        if pbhlgoldbarCount.get() == 0:
            return
        else:
            pbhlgoldbarCount.set(pbhlgoldbarCount.get()-1)
            pbhlblueCount.set(pbhlblueCount.get() - 1)

    pbhlraidCount.set(pbhlraidCount.get() - 1)
    #pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))

    if pbhlraidCount.get() == 0 or pbhlblueCount.get() == 0:
        nobluePercentage.set("0.0%")
        pbhlcoronaringPercentage.set("0.0%")
        pbhllineageringPercentage.set("0.0%")
        pbhlintricacyringPercentage.set("0.0%")
        pbhlgoldbarPercentage.set("0.0%")
        pbhlbluePercent.set("0.0%")
        pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))
    else:
        pbhlbluePercent.set(value=str(round(pbhlblueCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
        pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))
        nobluePercentage.set(str(round(noblueCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlcoronaringPercentage.set(str(round(pbhlcoronaringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhllineageringPercentage.set(str(round(pbhllineageringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlintricacyringPercentage.set(str(round(pbhlintricacyringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlgoldbarPercentage.set(str(round(pbhlgoldbarCount.get()/pbhlblueCount.get()*100,2)) + "%")

    saveData()


#akasha back action button
def buttonTakeBack(item):
    #messagebox.showinfo(item)
    #print(item)


    if(item=="hollowkey"):
        if hollowkeyCount.get() == 0:
            return
        else:
            hollowkeyCount.set(hollowkeyCount.get()-1)
    elif(item == "coronaring"):
        if coronaringCount.get() == 0:
            return
        else:
            coronaringCount.set(coronaringCount.get()-1)
    elif(item == "lineagering"):
        if lineageringCount.get() == 0:
            return
        else:
            lineageringCount.set(lineageringCount.get()-1)
    elif(item == "intricacyring"):
        if intricacyringCount.get() == 0:
            return
        else:
            intricacyringCount.set(intricacyringCount.get()-1)
    elif(item == "goldbar"):
        if goldbarCount.get() == 0:
            return
        else:
            goldbarCount.set(goldbarCount.get()-1)

    raidCount.set(raidCount.get() - 1)

    if raidCount.get() == 0:
        hollowkeyPercentage.set("0.0%")
        coronaringPercentage.set("0.0%")
        lineageringPercentage.set("0.0%")
        intricacyringPercentage.set("0.0%")
        goldbarPercentage.set("0.0%")
    else:
        hollowkeyPercentage.set(str(round(hollowkeyCount.get()/raidCount.get()*100,2)) + "%")
        coronaringPercentage.set(str(round(coronaringCount.get()/raidCount.get()*100,2)) + "%")
        lineageringPercentage.set(str(round(lineageringCount.get()/raidCount.get()*100,2)) + "%")
        intricacyringPercentage.set(str(round(intricacyringCount.get()/raidCount.get()*100,2)) + "%")
        goldbarPercentage.set(str(round(goldbarCount.get()/raidCount.get()*100,2)) + "%")

    saveData()

#gohl take back button
def gohlTakeBack(item):
    #messagebox.showinfo(item)
    #print(item)


    if(item=="azurite"):
        if azuriteCount.get() == 0:
            return
        else:
            azuriteCount.set(azuriteCount.get()-1)
    elif(item == "coronaring"):
        if gohlcoronaringCount.get() == 0:
            return
        else:
            gohlcoronaringCount.set(gohlcoronaringCount.get()-1)
    elif(item == "lineagering"):
        if gohllineageringCount.get() == 0:
            return
        else:
            gohllineageringCount.set(gohllineageringCount.get()-1)
    elif(item == "intricacyring"):
        if gohlintricacyringCount.get() == 0:
            return
        else:
            gohlintricacyringCount.set(gohlintricacyringCount.get()-1)
    elif(item == "goldbar"):
        if gohlgoldbarCount.get() == 0:
            return
        else:
            gohlgoldbarCount.set(gohlgoldbarCount.get()-1)

    gohlraidCount.set(gohlraidCount.get() - 1)

    if gohlraidCount.get() == 0:
        azuritePercentage.set("0.0%")
        gohlcoronaringPercentage.set("0.0%")
        gohllineageringPercentage.set("0.0%")
        gohlintricacyringPercentage.set("0.0%")
        gohlgoldbarPercentage.set("0.0%")
    else:
        azuritePercentage.set(str(round(azuriteCount.get() / gohlraidCount.get() * 100, 2)) + "%")
        gohlcoronaringPercentage.set(str(round(gohlcoronaringCount.get() / gohlraidCount.get() * 100, 2)) + "%")
        gohllineageringPercentage.set(str(round(gohllineageringCount.get() / gohlraidCount.get() * 100, 2)) + "%")
        gohlintricacyringPercentage.set(str(round(gohlintricacyringCount.get() / gohlraidCount.get() * 100, 2)) + "%")
        gohlgoldbarPercentage.set(str(round(gohlgoldbarCount.get() / gohlraidCount.get() * 100, 2)) + "%")

    saveData()

# PBHL reset
def pbhlresetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset?")

    if messageboxChoice == 'yes':
        pbhlraidCount.set(0)
        noblueCount.set(0)
        pbhlcoronaringCount.set(0)
        pbhllineageringCount.set(0)
        pbhlintricacyringCount.set(0)
        pbhlgoldbarCount.set(0)
        pbhlblueCount.set(0)

        if pbhlraidCount.get() == 0:
            nobluePercentage.set("0.0%")
            pbhlcoronaringPercentage.set("0.0%")
            pbhllineageringPercentage.set("0.0%")
            pbhlintricacyringPercentage.set("0.0%")
            pbhlgoldbarPercentage.set("0.0%")
            pbhlbluePercent.set("0.0%")
        else:
            pbhlbluePercent.set(value=str(round(pbhlblueCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))
            nobluePercentage.set(str(round(noblueCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhlcoronaringPercentage.set(str(round(pbhlcoronaringCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhllineageringPercentage.set(str(round(pbhllineageringCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhlintricacyringPercentage.set(str(round(pbhlintricacyringCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhlgoldbarPercentage.set(str(round(pbhlgoldbarCount.get() / pbhlraidCount.get() * 100, 2)) + "%")

        pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))
    else:
        return
    saveData()


# reset state
def resetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset?")

    if messageboxChoice == 'yes':
        raidCount.set(0)
        hollowkeyCount.set(0)
        coronaringCount.set(0)
        lineageringCount.set(0)
        intricacyringCount.set(0)
        goldbarCount.set(0)

        if raidCount.get() == 0:
            hollowkeyPercentage.set("0.0%")
            coronaringPercentage.set("0.0%")
            lineageringPercentage.set("0.0%")
            intricacyringPercentage.set("0.0%")
            goldbarPercentage.set("0.0%")
        else:
            hollowkeyPercentage.set(str(round(hollowkeyCount.get() / raidCount.get() * 100, 2)) + "%")
            coronaringPercentage.set(str(round(coronaringCount.get() / raidCount.get() * 100, 2)) + "%")
            lineageringPercentage.set(str(round(lineageringCount.get() / raidCount.get() * 100, 2)) + "%")
            intricacyringPercentage.set(str(round(intricacyringCount.get() / raidCount.get() * 100, 2)) + "%")
            goldbarPercentage.set(str(round(goldbarCount.get() / raidCount.get() * 100, 2)) + "%")
    else:
        return
    saveData()

def gohlresetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset?")

    if messageboxChoice == 'yes':
        gohlraidCount.set(0)
        azuriteCount.set(0)
        gohlcoronaringCount.set(0)
        gohllineageringCount.set(0)
        gohlintricacyringCount.set(0)
        gohlgoldbarCount.set(0)

        if gohlraidCount.get() == 0:
            azuritePercentage.set("0.0%")
            gohlcoronaringPercentage.set("0.0%")
            gohllineageringPercentage.set("0.0%")
            gohlintricacyringPercentage.set("0.0%")
            gohlgoldbarPercentage.set("0.0%")
        else:
            hollowkeyPercentage.set(str(round(azuriteCount.get() / gohlraidCount.get() * 100, 2)) + "%")
            coronaringPercentage.set(str(round(gohlcoronaringCount.get() / gohlraidCount.get() * 100, 2)) + "%")
            lineageringPercentage.set(str(round(gohllineageringCount.get() / gohlraidCount.get() * 100, 2)) + "%")
            intricacyringPercentage.set(str(round(gohlintricacyringCount.get() / gohlraidCount.get() * 100, 2)) + "%")
            goldbarPercentage.set(str(round(gohlgoldbarCount.get() / gohlraidCount.get() * 100, 2)) + "%")
    else:
        return
    saveData()

# GUI Layout / render

# total pbhl raids
pbhlImg = tk.PhotoImage(file=imgSrc("pbhlhorn.png"))
pbhlLabel = ttk.Label(pbhlTab, image=pbhlImg).grid(column=0,row=1)
pbhlCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlraidCount).grid(column=0, row=2)

# total akasha raids
akashablueImg = tk.PhotoImage(file=imgSrc("bluechest.png"))
akashablueLabel = ttk.Label(akashaTab, image=akashablueImg).grid(column=0,row=1)
akashablueCounterLabel = ttk.Label(akashaTab, textvariable=raidCount).grid(column=0, row=2)

# total gohl raids
gohlblueImg = tk.PhotoImage(file=imgSrc("bluechest.png"))
gohlblueLabel = ttk.Label(gohlTab, image=gohlblueImg).grid(column=0,row=1)
gohlblueCounterLabel = ttk.Label(gohlTab, textvariable=gohlraidCount).grid(column=0, row=2)

#umikin is stinky, maki too and udder and munching

# no blue chest
noblueImg = tk.PhotoImage(file=imgSrc("nobluechest.png"))
# hollowkeyLabel = tttk.Label(akashaTab, text="Hollow key").grid(column=0,row=0)
noblueButton = ttk.Button(pbhlTab, image=noblueImg)
noblueButton.grid(column=1,row=1)
noblueCounterLabel = ttk.Label(pbhlTab, textvariable=noblueCount).grid(column=1,row=2)
#nobluePercentageLabel = ttk.Label(pbhlTab, textvariable=nobluePercentage).grid(column=1,row=3)
noblueButton.bind('<Button-1>', lambda event: pbhlCallBack("noblue"))
noblueButton.bind('<Button-2>', lambda event: pbhlTakeBack("noblue"))
noblueButton.bind('<Button-3>', lambda event: pbhlTakeBack("noblue"))

# hollow key
hollowkeyImg = tk.PhotoImage(file=imgSrc("litter.png"))
# hollowkeyLabel = tttk.Label(akashaTab, text="Hollow key").grid(column=0,row=0)
hollowkeyButton = ttk.Button(akashaTab, image=hollowkeyImg)
hollowkeyButton.grid(column=1,row=1)
hollowkeyCounterLabel = ttk.Label(akashaTab, textvariable=hollowkeyCount).grid(column=1,row=2)
hollowkeyPercentageLabel = ttk.Label(akashaTab, textvariable=hollowkeyPercentage).grid(column=1,row=3)
hollowkeyButton.bind('<Button-1>', lambda event: buttonCallBack("hollowkey"))
hollowkeyButton.bind('<Button-2>', lambda event: buttonTakeBack("hollowkey"))
hollowkeyButton.bind('<Button-3>', lambda event: buttonTakeBack("hollowkey"))

# azurite
azuriteImg = tk.PhotoImage(file=imgSrc("litter.png"))
# hollowkeyLabel = tttk.Label(akashaTab, text="Hollow key").grid(column=0,row=0)
azuriteButton = ttk.Button(gohlTab, image=azuriteImg)
azuriteButton.grid(column=1,row=1)
azuriteCounterLabel = ttk.Label(gohlTab, textvariable=azuriteCount).grid(column=1,row=2)
azuritePercentageLabel = ttk.Label(gohlTab, textvariable=azuritePercentage).grid(column=1,row=3)
azuriteButton.bind('<Button-1>', lambda event: gohlCallBack("azurite"))
azuriteButton.bind('<Button-2>', lambda event: gohlTakeBack("azurite"))
azuriteButton.bind('<Button-3>', lambda event: gohlTakeBack("azurite"))

# pbhl corona ring
pbhlcoronaringImg = tk.PhotoImage(file=imgSrc("coronationring.png"))
# coronaringLabel = tttk.Label(akashaTab, text="Coronation Ring").grid(column=1,row=0)
pbhlcoronaringButton = ttk.Button(pbhlTab, image=pbhlcoronaringImg)
pbhlcoronaringButton.grid(column=2,row=1)
pbhlcoronaringCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlcoronaringCount).grid(column=2,row=2)
pbhlcoronaringPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhlcoronaringPercentage).grid(column=2,row=3)
pbhlcoronaringButton.bind('<Button-1>', lambda event: pbhlCallBack("coronaring"))
pbhlcoronaringButton.bind('<Button-2>', lambda event: pbhlTakeBack("coronaring"))
pbhlcoronaringButton.bind('<Button-3>', lambda event: pbhlTakeBack("coronaring"))

# corona ring
coronaringImg = tk.PhotoImage(file=imgSrc("coronationring.png"))
# coronaringLabel = tttk.Label(akashaTab, text="Coronation Ring").grid(column=1,row=0)
coronaringButton = ttk.Button(akashaTab, image=coronaringImg)
coronaringButton.grid(column=2,row=1)
coronaringCounterLabel = ttk.Label(akashaTab, textvariable=coronaringCount).grid(column=2,row=2)
coronaringPercentageLabel = ttk.Label(akashaTab, textvariable=coronaringPercentage).grid(column=2,row=3)
coronaringButton.bind('<Button-1>', lambda event: buttonCallBack("coronaring"))
coronaringButton.bind('<Button-2>', lambda event: buttonTakeBack("coronaring"))
coronaringButton.bind('<Button-3>', lambda event: buttonTakeBack("coronaring"))

# gohl corona ring
gohlcoronaringImg = tk.PhotoImage(file=imgSrc("coronationring.png"))
# coronaringLabel = tttk.Label(akashaTab, text="Coronation Ring").grid(column=1,row=0)
gohlcoronaringButton = ttk.Button(gohlTab, image=gohlcoronaringImg)
gohlcoronaringButton.grid(column=2,row=1)
gohlcoronaringCounterLabel = ttk.Label(gohlTab, textvariable=gohlcoronaringCount).grid(column=2,row=2)
gohlcoronaringPercentageLabel = ttk.Label(gohlTab, textvariable=gohlcoronaringPercentage).grid(column=2,row=3)
gohlcoronaringButton.bind('<Button-1>', lambda event: gohlCallBack("coronaring"))
gohlcoronaringButton.bind('<Button-2>', lambda event: gohlTakeBack("coronaring"))
gohlcoronaringButton.bind('<Button-3>', lambda event: gohlTakeBack("coronaring"))

# pbhl lineage ring
pbhllineageringImg = tk.PhotoImage(file=imgSrc("lineagering.png"))
# lineageringLabel = tttk.Label(akashaTab, text="Lineage Ring").grid(column=2,row=0)
pbhllineageringButton = ttk.Button(pbhlTab, image=pbhllineageringImg)
pbhllineageringButton.grid(column=3,row=1)
pbhllineageringCounterLabel = ttk.Label(pbhlTab, textvariable=pbhllineageringCount).grid(column=3,row=2)
pbhllineageringPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhllineageringPercentage).grid(column=3,row=3)
pbhllineageringButton.bind('<Button-1>', lambda event: pbhlCallBack("lineagering"))
pbhllineageringButton.bind('<Button-2>', lambda event: pbhlTakeBack("lineagering"))
pbhllineageringButton.bind('<Button-3>', lambda event: pbhlTakeBack("lineagering"))

# lineage ring
lineageringImg = tk.PhotoImage(file=imgSrc("lineagering.png"))
# lineageringLabel = tttk.Label(akashaTab, text="Lineage Ring").grid(column=2,row=0)
lineageringButton = ttk.Button(akashaTab, image=lineageringImg)
lineageringButton.grid(column=3,row=1)
lineageringCounterLabel = ttk.Label(akashaTab, textvariable=lineageringCount).grid(column=3,row=2)
lineageringPercentageLabel = ttk.Label(akashaTab, textvariable=lineageringPercentage).grid(column=3,row=3)
lineageringButton.bind('<Button-1>', lambda event: buttonCallBack("lineagering"))
lineageringButton.bind('<Button-2>', lambda event: buttonTakeBack("lineagering"))
lineageringButton.bind('<Button-3>', lambda event: buttonTakeBack("lineagering"))

# gohl lineage ring
gohllineageringImg = tk.PhotoImage(file=imgSrc("lineagering.png"))
# lineageringLabel = tttk.Label(akashaTab, text="Lineage Ring").grid(column=2,row=0)
gohllineageringButton = ttk.Button(gohlTab, image=gohllineageringImg)
gohllineageringButton.grid(column=3,row=1)
gohllineageringCounterLabel = ttk.Label(gohlTab, textvariable=gohllineageringCount).grid(column=3,row=2)
gohllineageringPercentageLabel = ttk.Label(gohlTab, textvariable=gohllineageringPercentage).grid(column=3,row=3)
gohllineageringButton.bind('<Button-1>', lambda event: gohlCallBack("lineagering"))
gohllineageringButton.bind('<Button-2>', lambda event: gohlTakeBack("lineagering"))
gohllineageringButton.bind('<Button-3>', lambda event: gohlTakeBack("lineagering"))

# pbhl intricacy ring
pbhlintricacyringImg = tk.PhotoImage(file=imgSrc("intricacyring.png"))
# intricacyringLabel = tttk.Label(akashaTab, text="Intricacy Ring").grid(column=3,row=0)
# intricacyringButton = ttk.Button(akashaTab, image=intricacyringImg, command=lambda:buttonCallBack("intricacyring")).grid(column=4,row=1)
pbhlintricacyringButton = ttk.Button(pbhlTab, image=pbhlintricacyringImg)
pbhlintricacyringButton.grid(column=4,row=1)
pbhlintricacyringCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlintricacyringCount).grid(column=4,row=2)
pbhlintricacyringPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhlintricacyringPercentage).grid(column=4,row=3)
pbhlintricacyringButton.bind('<Button-1>', lambda event: pbhlCallBack("intricacyring"))
pbhlintricacyringButton.bind('<Button-2>', lambda event: pbhlTakeBack("intricacyring"))
pbhlintricacyringButton.bind('<Button-3>', lambda event: pbhlTakeBack("intricacyring"))

# intricacy ring
intricacyringImg = tk.PhotoImage(file=imgSrc("intricacyring.png"))
# intricacyringLabel = tttk.Label(akashaTab, text="Intricacy Ring").grid(column=3,row=0)
# intricacyringButton = ttk.Button(akashaTab, image=intricacyringImg, command=lambda:buttonCallBack("intricacyring")).grid(column=4,row=1)
intricacyringButton = ttk.Button(akashaTab, image=intricacyringImg)
intricacyringButton.grid(column=4,row=1)
intricacyringCounterLabel = ttk.Label(akashaTab, textvariable=intricacyringCount).grid(column=4,row=2)
intricacyringPercentageLabel = ttk.Label(akashaTab, textvariable=intricacyringPercentage).grid(column=4,row=3)
intricacyringButton.bind('<Button-1>', lambda event: buttonCallBack("intricacyring"))
intricacyringButton.bind('<Button-2>', lambda event: buttonTakeBack("intricacyring"))
intricacyringButton.bind('<Button-3>', lambda event: buttonTakeBack("intricacyring"))

# gohl intricacy ring
gohlintricacyringImg = tk.PhotoImage(file=imgSrc("intricacyring.png"))
# intricacyringLabel = tttk.Label(akashaTab, text="Intricacy Ring").grid(column=3,row=0)
# intricacyringButton = ttk.Button(akashaTab, image=intricacyringImg, command=lambda:buttonCallBack("intricacyring")).grid(column=4,row=1)
gohlintricacyringButton = ttk.Button(gohlTab, image=gohlintricacyringImg)
gohlintricacyringButton.grid(column=4,row=1)
gohlintricacyringCounterLabel = ttk.Label(gohlTab, textvariable=gohlintricacyringCount).grid(column=4,row=2)
gohlintricacyringPercentageLabel = ttk.Label(gohlTab, textvariable=gohlintricacyringPercentage).grid(column=4,row=3)
gohlintricacyringButton.bind('<Button-1>', lambda event: gohlCallBack("intricacyring"))
gohlintricacyringButton.bind('<Button-2>', lambda event: gohlTakeBack("intricacyring"))
gohlintricacyringButton.bind('<Button-3>', lambda event: gohlTakeBack("intricacyring"))

# pbhl gold bar
pbhlgoldbarImg = tk.PhotoImage(file=imgSrc("Yoink.png"))
# goldbarLabel = tttk.Label(akashaTab, text="Gold Bar").grid(column=4,row=0)
pbhlgoldbarButton = ttk.Button(pbhlTab, image=pbhlgoldbarImg)
pbhlgoldbarButton.grid(column=5,row=1)
pbhlgoldbarCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlgoldbarCount).grid(column=5,row=2)
pbhlgoldbarPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhlgoldbarPercentage).grid(column=5,row=3)
pbhlgoldbarButton.bind('<Button-1>', lambda event: pbhlCallBack("goldbar"))
pbhlgoldbarButton.bind('<Button-2>', lambda event: pbhlTakeBack("goldbar"))
pbhlgoldbarButton.bind('<Button-3>', lambda event: pbhlTakeBack("goldbar"))

# gold bar
goldbarImg = tk.PhotoImage(file=imgSrc("Yoink.png"))
# goldbarLabel = tttk.Label(akashaTab, text="Gold Bar").grid(column=4,row=0)
goldbarButton = ttk.Button(akashaTab, image=goldbarImg)
goldbarButton.grid(column=5,row=1)
goldbarCounterLabel = ttk.Label(akashaTab, textvariable=goldbarCount).grid(column=5,row=2)
goldbarPercentageLabel = ttk.Label(akashaTab, textvariable=goldbarPercentage).grid(column=5,row=3)
goldbarButton.bind('<Button-1>', lambda event: buttonCallBack("goldbar"))
goldbarButton.bind('<Button-2>', lambda event: buttonTakeBack("goldbar"))
goldbarButton.bind('<Button-3>', lambda event: buttonTakeBack("goldbar"))

# gohl gold bar
gohlgoldbarImg = tk.PhotoImage(file=imgSrc("Yoink.png"))
# goldbarLabel = tttk.Label(akashaTab, text="Gold Bar").grid(column=4,row=0)
gohlgoldbarButton = ttk.Button(gohlTab, image=gohlgoldbarImg)
gohlgoldbarButton.grid(column=5,row=1)
gohlgoldbarCounterLabel = ttk.Label(gohlTab, textvariable=gohlgoldbarCount).grid(column=5,row=2)
gohlgoldbarPercentageLabel = ttk.Label(gohlTab, textvariable=gohlgoldbarPercentage).grid(column=5,row=3)
gohlgoldbarButton.bind('<Button-1>', lambda event: gohlCallBack("goldbar"))
gohlgoldbarButton.bind('<Button-2>', lambda event: gohlTakeBack("goldbar"))
gohlgoldbarButton.bind('<Button-3>', lambda event: gohlTakeBack("goldbar"))

# pbhl reset button
pbhlresetButton = ttk.Button(pbhlTab, text="Reset", command=lambda:pbhlresetCount(), width=12).grid(column=5, row=5)

# akasha reset button
resetButton = ttk.Button(akashaTab, text="Reset", command=lambda:resetCount(), width=12).grid(column=5, row=5)

# gohl reset button
gohlresetButton = ttk.Button(gohlTab, text="Reset", command=lambda:gohlresetCount(), width=12).grid(column=5, row=5)

# pbhl blue chest count/percentage
pbhlblueImg = tk.PhotoImage(file=imgSrc("bluechest25.png"))
pbhlblueLabel = ttk.Label(pbhlTab, image=pbhlblueImg)
pbhlblueLabel.grid(column=0,row=4, sticky= tk.W)

pbhlblueTextLabel = ttk.Label(pbhlTab, textvariable=pbhlblueText, justify="left")
pbhlblueTextLabel.grid(column=0, columnspan=2, row=5, sticky=tk.W)

#pbhlbluePercentLabel = ttk.Label(pbhlTab, textvariable=pbhlbluePercent)
#pbhlbluePercentLabel.grid(column=0, row=5, sticky=tk.NE)

# NEW STUFF


def callBack(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False

vcmd = root.register(callBack)

#pbhlHornsDifference = StringVar(value="Dokkan")

if drop['pbhl']['hornbefore'] == "" and drop['pbhl']['hornafter'] =="":
    pbhlHornsSinceLabel = StringVar(value="Horns since:" + "\n" + "0")
elif drop['pbhl']['hornbefore'] == "":
    pbhlHornsSinceLabel = StringVar(value="Horns since:" + "\n" + str(abs(int(drop['pbhl']['hornafter']))))
elif drop['pbhl']['hornafter'] == "":
    pbhlHornsSinceLabel = StringVar(value="Horns since:" + "\n" + str(abs(int(drop['pbhl']['hornbefore']))))
else:
    pbhlHornsSinceLabel = StringVar(value="Horns since:" + "\n" + str(abs(int(drop['pbhl']['hornbefore'])-int(drop['pbhl']['hornafter']))))

def hornsDifference(e):
    if pbhlHornLastBarEntry.get() == "" and pbhlCurrentHornEntry.get() == "":
        pbhlHornsSinceLabel.set("Horns since:" + "\n" + "0")
    elif pbhlHornLastBarEntry.get() == "":
        pbhlHornsSinceLabel.set("Horns since:" + "\n" + str(abs(int(pbhlCurrentHornEntry.get()))))
    elif pbhlCurrentHornEntry.get() == "":
        pbhlHornsSinceLabel.set("Horns since:" + "\n" + str(abs(int(pbhlHornLastBarEntry.get()))))
    else:
        pbhlHornsSinceLabel.set("Horns since:" + "\n" + str(abs(int(pbhlHornLastBarEntry.get()) - int(pbhlCurrentHornEntry.get()))))

    saveData()

# Horn Count
pbhlhornImg = tk.PhotoImage(file=imgSrc("pbhlhorn2.png"))
pbhlhornLabel = ttk.Label(pbhlTab, image=pbhlhornImg)
pbhlhornLabel.grid(column=2, row=4, sticky= tk.W)

pbhlHornText = ttk.Label(pbhlTab, textvariable=pbhlHornsSinceLabel, justify="left")
pbhlHornText.grid(column=2, columnspan=2, row=5, sticky= tk.NW)

pbhlHornLastBarEntry = ttk.Entry(pbhlTab, width=15, validate='key', validatecommand=(vcmd, '%P'))
pbhlHornLastBarEntry.grid(column=3, columnspan=2, row=4)
pbhlHornLastBarEntry.insert(0, drop['pbhl']['hornbefore'])
pbhlHornLastBarEntry.bind("<KeyRelease>", hornsDifference)

pbhlCurrentHornEntry = ttk.Entry(pbhlTab, width=15, validate='key', validatecommand=(vcmd, '%P'))
pbhlCurrentHornEntry.grid(column=3, columnspan=2, row=5)
pbhlCurrentHornEntry.insert(0, drop['pbhl']['hornafter'])
pbhlCurrentHornEntry.bind("<KeyRelease>", hornsDifference)

# Key Count
if drop['akasha']['keybefore'] == "" and drop['akasha']['keyafter'] =="":
    keysSinceLabel = StringVar(value="Keys since:" + "\n" + "0")
elif drop['akasha']['keybefore'] == "":
    keysSinceLabel = StringVar(value="Keys since:" + "\n" + str(abs(int(drop['akasha']['keyafter']))))
elif drop['akasha']['keyafter'] == "":
    keysSinceLabel = StringVar(value="Keys since:" + "\n" + str(abs(int(drop['akasha']['keybefore']))))
else:
    keysSinceLabel = StringVar(value="Keys since:" + "\n" + str(abs(int(drop['akasha']['keybefore'])-int(drop['akasha']['keyafter']))))


def keysDifference(e):
    if keyTextAfter.get() == "" and keyTextBefore.get() == "":
        keysSinceLabel.set("Keys since:" + "\n" + "0")
    elif keyTextAfter.get() == "":
        keysSinceLabel.set("Keys since:" + "\n" + str(abs(int(keyTextBefore.get()))))
    elif keyTextBefore.get() == "":
        keysSinceLabel.set("Keys since:" + "\n" + str(abs(int(keyTextAfter.get()))))
    else:
        keysSinceLabel.set("Keys since:" + "\n" + str(abs(int(keyTextBefore.get()) - int(keyTextAfter.get()))))

    saveData()


keyImg = tk.PhotoImage(file=imgSrc("hollowkey.png"))
keyImgLabel = ttk.Label(akashaTab, image=keyImg)
keyImgLabel.grid(column=0, row=4, sticky= tk.W)

keyText = ttk.Label(akashaTab, textvariable=keysSinceLabel, justify="left")
keyText.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

keyTextBefore = ttk.Entry(akashaTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
keyTextBefore.grid(column=1, columnspan=2, row=4)
keyTextBefore.insert(0, drop['akasha']['keybefore'])
keyTextBefore.bind("<KeyRelease>", keysDifference)

keyTextAfter = ttk.Entry(akashaTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
keyTextAfter.grid(column=1, columnspan=2, row=5)
keyTextAfter.insert(0, drop['akasha']['keyafter'])
keyTextAfter.bind("<KeyRelease>", keysDifference)

# Azurite Count
if drop['gohl']['azuritebefore'] == "" and drop['gohl']['azuriteafter'] =="":
    azuriteSinceLabel = StringVar(value="Azurite since:" + "\n" + "0")
elif drop['gohl']['azuritebefore'] == "":
    azuriteSinceLabel = StringVar(value="Azurite since:" + "\n" + str(abs(int(drop['gohl']['azuriteafter']))))
elif drop['gohl']['azuriteafter'] == "":
    azuriteSinceLabel = StringVar(value="Azurite since:" + "\n" + str(abs(int(drop['gohl']['azuritebefore']))))
else:
    azuriteSinceLabel = StringVar(value="Azurite since:" + "\n" + str(abs(int(drop['gohl']['azuritebefore'])-int(drop['gohl']['azuriteafter']))))


def azuriteDifference(e):
    if azuriteTextAfter.get() == "" and azuriteTextBefore.get() == "":
        azuriteSinceLabel.set("Azurite since:" + "\n" + "0")
    elif azuriteTextAfter.get() == "":
        azuriteSinceLabel.set("Azurite since:" + "\n" + str(abs(int(azuriteTextBefore.get()))))
    elif azuriteTextBefore.get() == "":
        azuriteSinceLabel.set("Azurite since:" + "\n" + str(abs(int(azuriteTextAfter.get()))))
    else:
        azuriteSinceLabel.set("Azurite since:" + "\n" + str(abs(int(azuriteTextBefore.get()) - int(azuriteTextAfter.get()))))

    saveData()


azuriteImg2 = tk.PhotoImage(file=imgSrc("azurite.png"))
azuriteImgLabel = ttk.Label(gohlTab, image=azuriteImg2)
azuriteImgLabel.grid(column=0, row=4, sticky= tk.W)

azuriteText = ttk.Label(gohlTab, textvariable=azuriteSinceLabel, justify="left")
azuriteText.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

azuriteTextBefore = ttk.Entry(gohlTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
azuriteTextBefore.grid(column=1, columnspan=2, row=4)
azuriteTextBefore.insert(0, drop['gohl']['azuritebefore'])
azuriteTextBefore.bind("<KeyRelease>", azuriteDifference)

azuriteTextAfter = ttk.Entry(gohlTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
azuriteTextAfter.grid(column=1, columnspan=2, row=5)
azuriteTextAfter.insert(0, drop['gohl']['azuriteafter'])
azuriteTextAfter.bind("<KeyRelease>", azuriteDifference)


root.mainloop()
