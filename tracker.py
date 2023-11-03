import json
import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import IntVar, StringVar, PhotoImage, ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle

def imgSrc(img, raid: str = "") -> str:
    if getattr(sys, 'frozen', False):
        filepath = os.path.dirname(sys.executable)
    elif __file__:
        filepath, filename = os.path.split(os.path.realpath(__file__))

    return os.path.join(filepath, "img", img) if raid == "" else os.path.join(filepath, "img", raid, img)

def fileSrc(file):
    if getattr(sys, 'frozen', False):
        filepath = os.path.dirname(sys.executable)
    elif __file__:
        filepath, filename = os.path.split(os.path.realpath(__file__))
    return os.path.join(filepath,file)

def resizeImage(img, newWidth, newHeight):
    pilImage = ImageTk.getimage(img).convert("RGBA")
    oldWidth, oldHeight = pilImage.size
    newImg = pilImage.resize((newWidth, newHeight), Image.LANCZOS)
    newPhotoImage = ImageTk.PhotoImage(newImg)
    return newPhotoImage

#load data from json
with open(fileSrc('data.json')) as file:
    drop = json.load(file)

root = tk.Tk()
root.title("Drop Tracker")
root.iconphoto(True, PhotoImage(file=imgSrc("peek.png")))
root.attributes('-topmost', True)

def callBack(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False
vcmd = root.register(callBack)

theme = StringVar(value=drop['settings']['theme'])
style = ThemedStyle(root)
style.set_theme(theme.get())

#tab definition
tabControl = ttk.Notebook(root)

barTab = ttk.Frame(tabControl)
sandTab = ttk.Frame(tabControl)
customTab = ttk.Frame(tabControl)
settingsTab = ttk.Frame(tabControl)

tabControlSand = ttk.Notebook(sandTab)
tabControlBar = ttk.Notebook(barTab)
tabControlCustom = ttk.Notebook(customTab)
tabControlSettings = ttk.Notebook(settingsTab)

pbhlTab = ttk.Frame(tabControlBar)
akashaTab = ttk.Frame(tabControlBar)
gohlTab = ttk.Frame(tabControlBar)
dragonTab = ttk.Frame(tabControlSand)
revansTab = ttk.Frame(tabControlSand)
subhlTab = ttk.Frame(tabControlSand)

custom1Tab = ttk.Frame(tabControlCustom)
custom2Tab = ttk.Frame(tabControlCustom)
custom3Tab = ttk.Frame(tabControlCustom)
custom4Tab = ttk.Frame(tabControlCustom)

tabControlBar.add(pbhlTab, text='PBHL')
tabControlBar.add(akashaTab, text='Akasha')
tabControlBar.add(gohlTab, text='GOHL')

tabControlSand.add(dragonTab, text='Dragons')
tabControlSand.add(revansTab, text='Revans')
tabControlSand.add(subhlTab, text='SUBHL')

tabControlCustom.add(custom1Tab, text='Custom 1')
tabControlCustom.add(custom2Tab, text='Custom 2')
tabControlCustom.add(custom3Tab, text='Custom 3')
tabControlCustom.add(custom4Tab, text='Custom 4')

barImg = ImageTk.PhotoImage((Image.open(imgSrc("goldbar.png"))).resize((20,20),Image.LANCZOS))
sandImg = ImageTk.PhotoImage((Image.open(imgSrc("eternitysand.png"))).resize((20,20),Image.LANCZOS))
customImg = ImageTk.PhotoImage((Image.open(imgSrc("custom.png"))).resize((20,20),Image.LANCZOS))

tabControl.add(barTab, text="Gold Bar", image=barImg, compound="left")
tabControl.add(sandTab, text='Eternity Sand', image=sandImg, compound="left")
tabControl.add(customTab, text='Custom', image=customImg, compound="left")
tabControl.add(settingsTab, text='Settings', image=customImg, compound="left")
tabControl.pack(expand=1, fill="both")
tabControlBar.pack(expand=1, fill="both")
tabControlSand.pack(expand=1, fill="both")
tabControlCustom.pack(expand=1, fill="both")

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

# Tab Dragons
dragonraidCount = IntVar(value=drop['dragon']['raid'])
dragontrashCount = IntVar(value=drop['dragon']['trash'])
dragonearringCount = IntVar(value=drop['dragon']['earring'])
dragonsandCount = IntVar(value=drop['dragon']['sand'])

# Tab Revans
revansraidCount = IntVar(value=drop['revans']['raid'])
revanstrashCount = IntVar(value=drop['revans']['trash'])
revansweaponCount = IntVar(value=drop['revans']['weapon'])
revanssandCount = IntVar(value=drop['revans']['sand'])

# Tab SUBHL
subhlraidCount = IntVar(value=drop['subhl']['raid'])
subhltrashCount = IntVar(value=drop['subhl']['trash'])
subhlsandCount = IntVar(value=drop['subhl']['sand'])

# Tab Custom1
custom1raidCount = IntVar(value=drop['custom1']['raid'])
custom1mat1Count = IntVar(value=drop['custom1']['mat1'])
custom1mat2Count = IntVar(value=drop['custom1']['mat2'])
custom1mat3Count = IntVar(value=drop['custom1']['mat3'])
custom1mat4Count = IntVar(value=drop['custom1']['mat4'])
custom1mat5Count = IntVar(value=drop['custom1']['mat5'])

# Tab Custom2
custom2raidCount = IntVar(value=drop['custom2']['raid'])
custom2mat1Count = IntVar(value=drop['custom2']['mat1'])
custom2mat2Count = IntVar(value=drop['custom2']['mat2'])
custom2mat3Count = IntVar(value=drop['custom2']['mat3'])
custom2mat4Count = IntVar(value=drop['custom2']['mat4'])
custom2mat5Count = IntVar(value=drop['custom2']['mat5'])

# Tab Custom3
custom3raidCount = IntVar(value=drop['custom3']['raid'])
custom3mat1Count = IntVar(value=drop['custom3']['mat1'])
custom3mat2Count = IntVar(value=drop['custom3']['mat2'])
custom3mat3Count = IntVar(value=drop['custom3']['mat3'])
custom3mat4Count = IntVar(value=drop['custom3']['mat4'])
custom3mat5Count = IntVar(value=drop['custom3']['mat5'])

# Tab Custom4
custom4raidCount = IntVar(value=drop['custom4']['raid'])
custom4mat1Count = IntVar(value=drop['custom4']['mat1'])
custom4mat2Count = IntVar(value=drop['custom4']['mat2'])
custom4mat3Count = IntVar(value=drop['custom4']['mat3'])
custom4mat4Count = IntVar(value=drop['custom4']['mat4'])
custom4mat5Count = IntVar(value=drop['custom4']['mat5'])

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

# dragons
if dragonraidCount.get() == 0:
    dragontrashPercentage = StringVar(value="0.0%")
    dragonearringPercentage = StringVar(value="0.0%")
    dragonsandPercentage = StringVar(value="0.0%")
else:
    dragontrashPercentage = StringVar(value=str(round(dragontrashCount.get()/dragonraidCount.get()*100,2)) + "%")
    dragonearringPercentage = StringVar(value=str(round(dragonearringCount.get()/dragonraidCount.get()*100,2)) + "%")
    dragonsandPercentage = StringVar(value=str(round(dragonsandCount.get()/dragonraidCount.get()*100,2)) + "%")

# revans
if revansraidCount.get() == 0:
    revanstrashPercentage = StringVar(value="0.0%")
    revansweaponPercentage = StringVar(value="0.0%")
    revanssandPercentage = StringVar(value="0.0%")
else:
    revanstrashPercentage = StringVar(value=str(round(revanstrashCount.get()/revansraidCount.get()*100,2)) + "%")
    revansweaponPercentage = StringVar(value=str(round(revansweaponCount.get()/revansraidCount.get()*100,2)) + "%")
    revanssandPercentage = StringVar(value=str(round(revanssandCount.get()/revansraidCount.get()*100,2)) + "%")

# subhl
if subhlraidCount.get() == 0:
    subhltrashPercentage = StringVar(value="0.0%")
    subhlsandPercentage = StringVar(value="0.0%")
else:
    subhltrashPercentage = StringVar(value=str(round(subhltrashCount.get()/subhlraidCount.get()*100,2)) + "%")
    subhlsandPercentage = StringVar(value=str(round(subhlsandCount.get()/subhlraidCount.get()*100,2)) + "%")

# custom1
if custom1raidCount.get() == 0:
    custom1mat1Percentage = StringVar(value="0.0%")
    custom1mat2Percentage = StringVar(value="0.0%")
    custom1mat3Percentage = StringVar(value="0.0%")
    custom1mat4Percentage = StringVar(value="0.0%")
    custom1mat5Percentage = StringVar(value="0.0%")
else:
    custom1mat1Percentage = StringVar(value=str(round(custom1mat1Count.get()/custom1raidCount.get()*100,2)) + "%")
    custom1mat2Percentage = StringVar(value=str(round(custom1mat2Count.get()/custom1raidCount.get()*100,2)) + "%")
    custom1mat3Percentage = StringVar(value=str(round(custom1mat3Count.get()/custom1raidCount.get()*100,2)) + "%")
    custom1mat4Percentage = StringVar(value=str(round(custom1mat4Count.get()/custom1raidCount.get()*100,2)) + "%")
    custom1mat5Percentage = StringVar(value=str(round(custom1mat5Count.get()/custom1raidCount.get()*100,2)) + "%")

# custom2
if custom2raidCount.get() == 0:
    custom2mat1Percentage = StringVar(value="0.0%")
    custom2mat2Percentage = StringVar(value="0.0%")
    custom2mat3Percentage = StringVar(value="0.0%")
    custom2mat4Percentage = StringVar(value="0.0%")
    custom2mat5Percentage = StringVar(value="0.0%")
else:
    custom2mat1Percentage = StringVar(value=str(round(custom2mat1Count.get()/custom2raidCount.get()*100,2)) + "%")
    custom2mat2Percentage = StringVar(value=str(round(custom2mat2Count.get()/custom2raidCount.get()*100,2)) + "%")
    custom2mat3Percentage = StringVar(value=str(round(custom2mat3Count.get()/custom2raidCount.get()*100,2)) + "%")
    custom2mat4Percentage = StringVar(value=str(round(custom2mat4Count.get()/custom2raidCount.get()*100,2)) + "%")
    custom2mat5Percentage = StringVar(value=str(round(custom2mat5Count.get()/custom2raidCount.get()*100,2)) + "%")

# custom3
if custom3raidCount.get() == 0:
    custom3mat1Percentage = StringVar(value="0.0%")
    custom3mat2Percentage = StringVar(value="0.0%")
    custom3mat3Percentage = StringVar(value="0.0%")
    custom3mat4Percentage = StringVar(value="0.0%")
    custom3mat5Percentage = StringVar(value="0.0%")
else:
    custom3mat1Percentage = StringVar(value=str(round(custom3mat1Count.get()/custom3raidCount.get()*100,2)) + "%")
    custom3mat2Percentage = StringVar(value=str(round(custom3mat2Count.get()/custom3raidCount.get()*100,2)) + "%")
    custom3mat3Percentage = StringVar(value=str(round(custom3mat3Count.get()/custom3raidCount.get()*100,2)) + "%")
    custom3mat4Percentage = StringVar(value=str(round(custom3mat4Count.get()/custom3raidCount.get()*100,2)) + "%")
    custom3mat5Percentage = StringVar(value=str(round(custom3mat5Count.get()/custom3raidCount.get()*100,2)) + "%")

# custom4
if custom4raidCount.get() == 0:
    custom4mat1Percentage = StringVar(value="0.0%")
    custom4mat2Percentage = StringVar(value="0.0%")
    custom4mat3Percentage = StringVar(value="0.0%")
    custom4mat4Percentage = StringVar(value="0.0%")
    custom4mat5Percentage = StringVar(value="0.0%")
else:
    custom4mat1Percentage = StringVar(value=str(round(custom4mat1Count.get()/custom4raidCount.get()*100,2)) + "%")
    custom4mat2Percentage = StringVar(value=str(round(custom4mat2Count.get()/custom4raidCount.get()*100,2)) + "%")
    custom4mat3Percentage = StringVar(value=str(round(custom4mat3Count.get()/custom4raidCount.get()*100,2)) + "%")
    custom4mat4Percentage = StringVar(value=str(round(custom4mat4Count.get()/custom4raidCount.get()*100,2)) + "%")
    custom4mat5Percentage = StringVar(value=str(round(custom4mat5Count.get()/custom4raidCount.get()*100,2)) + "%")

#save data to json
def saveData():
    #fixed schema def
    drop = {}
    drop['settings'] = {
        'resourceTab':  tabControl.select(),
        'goldTab':  tabControlBar.select(),
        'sandTab':  tabControlSand.select(),
        'customTab':  tabControlCustom.select(),
        'settingsTab':  tabControlSettings.select(),
        'theme': theme.get()
    }
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
    drop['dragon'] = {
        'raid': dragonraidCount.get(),
        'trash': dragontrashCount.get(),
        'earring': dragonearringCount.get(),
        'sand': dragonsandCount.get(),
        'animabefore': dragonAnimaTextBefore.get(),
        'animaafter': dragonAnimaTextAfter.get(),
    }
    drop['revans'] = {
        'raid': revansraidCount.get(),
        'trash': revanstrashCount.get(),
        'weapon': revansweaponCount.get(),
        'sand': revanssandCount.get(),
        'animabefore': revansAnimaTextBefore.get(),
        'animaafter': revansAnimaTextAfter.get(),
    }
    drop['subhl'] = {
        'raid': subhlraidCount.get(),
        'trash': subhltrashCount.get(),
        'sand': subhlsandCount.get(),
        'animabefore': subhlAnimaTextBefore.get(),
        'animaafter': subhlAnimaTextAfter.get(),
    }
    drop['custom1'] = {
        'raid': custom1raidCount.get(),
        'mat1': custom1mat1Count.get(),
        'mat2': custom1mat2Count.get(),
        'mat3': custom1mat3Count.get(),
        'mat4': custom1mat4Count.get(),
        'mat5': custom1mat5Count.get(),
        'animabefore': custom1TextBefore.get(),
        'animaafter': custom1TextAfter.get(),
    }
    drop['custom2'] = {
        'raid': custom2raidCount.get(),
        'mat1': custom2mat1Count.get(),
        'mat2': custom2mat2Count.get(),
        'mat3': custom2mat3Count.get(),
        'mat4': custom2mat4Count.get(),
        'mat5': custom2mat5Count.get(),
        'animabefore': custom2TextBefore.get(),
        'animaafter': custom2TextAfter.get(),
    }
    drop['custom3'] = {
        'raid': custom3raidCount.get(),
        'mat1': custom3mat1Count.get(),
        'mat2': custom3mat2Count.get(),
        'mat3': custom3mat3Count.get(),
        'mat4': custom3mat4Count.get(),
        'mat5': custom3mat5Count.get(),
        'animabefore': custom3TextBefore.get(),
        'animaafter': custom3TextAfter.get(),
    }
    drop['custom4'] = {
        'raid': custom4raidCount.get(),
        'mat1': custom4mat1Count.get(),
        'mat2': custom4mat2Count.get(),
        'mat3': custom4mat3Count.get(),
        'mat4': custom4mat4Count.get(),
        'mat5': custom4mat5Count.get(),
        'animabefore': custom4TextBefore.get(),
        'animaafter': custom4TextAfter.get(),
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

def dragonCallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    dragonraidCount.set(dragonraidCount.get()+1)

    if(item=="trash"):
        dragontrashCount.set(dragontrashCount.get()+1)
    elif(item == "earring"):
        dragonearringCount.set(dragonearringCount.get()+1)
    elif(item == "sand"):
        dragonsandCount.set(dragonsandCount.get()+1)

    dragontrashPercentage.set(str(round(dragontrashCount.get()/dragonraidCount.get()*100,2)) + "%")
    dragonearringPercentage.set(str(round(dragonearringCount.get()/dragonraidCount.get()*100,2)) + "%")
    dragonsandPercentage.set(str(round(dragonsandCount.get()/dragonraidCount.get()*100,2)) + "%")

    saveData()

def revansCallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    revansraidCount.set(revansraidCount.get()+1)

    if(item=="trash"):
        revanstrashCount.set(revanstrashCount.get()+1)
    elif(item == "weapon"):
        revansweaponCount.set(revansweaponCount.get()+1)
    elif(item == "sand"):
        revanssandCount.set(revanssandCount.get()+1)

    revanstrashPercentage.set(str(round(revanstrashCount.get()/revansraidCount.get()*100,2)) + "%")
    revansweaponPercentage.set(str(round(revansweaponCount.get()/revansraidCount.get()*100,2)) + "%")
    revanssandPercentage.set(str(round(revanssandCount.get()/revansraidCount.get()*100,2)) + "%")

    saveData()

def subhlCallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    subhlraidCount.set(subhlraidCount.get()+1)

    if(item=="trash"):
        subhltrashCount.set(subhltrashCount.get()+1)
    elif(item == "sand"):
        subhlsandCount.set(subhlsandCount.get()+1)

    subhltrashPercentage.set(str(round(subhltrashCount.get()/subhlraidCount.get()*100,2)) + "%")
    subhlsandPercentage.set(str(round(subhlsandCount.get()/subhlraidCount.get()*100,2)) + "%")

    saveData()

def custom1CallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    custom1raidCount.set(custom1raidCount.get()+1)

    if (item == "mat1"):
        custom1mat1Count.set(custom1mat1Count.get() + 1)
    elif (item == "mat2"):
        custom1mat2Count.set(custom1mat2Count.get() + 1)
    elif (item == "mat3"):
        custom1mat3Count.set(custom1mat3Count.get() + 1)
    elif (item == "mat4"):
        custom1mat4Count.set(custom1mat4Count.get() + 1)
    elif (item == "mat5"):
        custom1mat5Count.set(custom1mat5Count.get() + 1)

    custom1mat1Percentage.set(str(round(custom1mat1Count.get() / custom1raidCount.get() * 100, 2)) + "%")
    custom1mat2Percentage.set(str(round(custom1mat2Count.get() / custom1raidCount.get() * 100, 2)) + "%")
    custom1mat3Percentage.set(str(round(custom1mat3Count.get() / custom1raidCount.get() * 100, 2)) + "%")
    custom1mat4Percentage.set(str(round(custom1mat4Count.get() / custom1raidCount.get() * 100, 2)) + "%")
    custom1mat5Percentage.set(str(round(custom1mat5Count.get() / custom1raidCount.get() * 100, 2)) + "%")

    saveData()

def custom2CallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    custom2raidCount.set(custom2raidCount.get()+1)

    if (item == "mat1"):
        custom2mat1Count.set(custom2mat1Count.get() + 1)
    elif (item == "mat2"):
        custom2mat2Count.set(custom2mat2Count.get() + 1)
    elif (item == "mat3"):
        custom2mat3Count.set(custom2mat3Count.get() + 1)
    elif (item == "mat4"):
        custom2mat4Count.set(custom2mat4Count.get() + 1)
    elif (item == "mat5"):
        custom2mat5Count.set(custom2mat5Count.get() + 1)

    custom2mat1Percentage.set(str(round(custom2mat1Count.get() / custom2raidCount.get() * 100, 2)) + "%")
    custom2mat2Percentage.set(str(round(custom2mat2Count.get() / custom2raidCount.get() * 100, 2)) + "%")
    custom2mat3Percentage.set(str(round(custom2mat3Count.get() / custom2raidCount.get() * 100, 2)) + "%")
    custom2mat4Percentage.set(str(round(custom2mat4Count.get() / custom2raidCount.get() * 100, 2)) + "%")
    custom2mat5Percentage.set(str(round(custom2mat5Count.get() / custom2raidCount.get() * 100, 2)) + "%")

    saveData()

def custom3CallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    custom3raidCount.set(custom3raidCount.get()+1)

    if (item == "mat1"):
        custom3mat1Count.set(custom3mat1Count.get() + 1)
    elif (item == "mat2"):
        custom3mat2Count.set(custom3mat2Count.get() + 1)
    elif (item == "mat3"):
        custom3mat3Count.set(custom3mat3Count.get() + 1)
    elif (item == "mat4"):
        custom3mat4Count.set(custom3mat4Count.get() + 1)
    elif (item == "mat5"):
        custom3mat5Count.set(custom3mat5Count.get() + 1)

    custom3mat1Percentage.set(str(round(custom3mat1Count.get() / custom3raidCount.get() * 100, 2)) + "%")
    custom3mat2Percentage.set(str(round(custom3mat2Count.get() / custom3raidCount.get() * 100, 2)) + "%")
    custom3mat3Percentage.set(str(round(custom3mat3Count.get() / custom3raidCount.get() * 100, 2)) + "%")
    custom3mat4Percentage.set(str(round(custom3mat4Count.get() / custom3raidCount.get() * 100, 2)) + "%")
    custom3mat5Percentage.set(str(round(custom3mat5Count.get() / custom3raidCount.get() * 100, 2)) + "%")

    saveData()

def custom4CallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    custom4raidCount.set(custom4raidCount.get()+1)

    if (item == "mat1"):
        custom4mat1Count.set(custom4mat1Count.get() + 1)
    elif (item == "mat2"):
        custom4mat2Count.set(custom4mat2Count.get() + 1)
    elif (item == "mat3"):
        custom4mat3Count.set(custom4mat3Count.get() + 1)
    elif (item == "mat4"):
        custom4mat4Count.set(custom4mat4Count.get() + 1)
    elif (item == "mat5"):
        custom4mat5Count.set(custom4mat5Count.get() + 1)

    custom4mat1Percentage.set(str(round(custom4mat1Count.get() / custom4raidCount.get() * 100, 2)) + "%")
    custom4mat2Percentage.set(str(round(custom4mat2Count.get() / custom4raidCount.get() * 100, 2)) + "%")
    custom4mat3Percentage.set(str(round(custom4mat3Count.get() / custom4raidCount.get() * 100, 2)) + "%")
    custom4mat4Percentage.set(str(round(custom4mat4Count.get() / custom4raidCount.get() * 100, 2)) + "%")
    custom4mat5Percentage.set(str(round(custom4mat5Count.get() / custom4raidCount.get() * 100, 2)) + "%")

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

#dragons back action button
def dragonTakeBack(item):
    #messagebox.showinfo(item)
    #print(item)

    if(item=="trash"):
        if dragontrashCount.get() == 0:
            return
        else:
            dragontrashCount.set(dragontrashCount.get()-1)
    elif(item == "earring"):
        if dragonearringCount.get() == 0:
            return
        else:
            dragonearringCount.set(dragonearringCount.get()-1)
    elif(item == "sand"):
        if dragonsandCount.get() == 0:
            return
        else:
            dragonsandCount.set(dragonsandCount.get()-1)

    dragonraidCount.set(dragonraidCount.get() - 1)

    if dragonraidCount.get() == 0:
        dragontrashPercentage.set("0.0%")
        dragonearringPercentage.set("0.0%")
        dragonsandPercentage.set("0.0%")
    else:
        dragontrashPercentage.set(str(round(dragontrashCount.get()/dragonraidCount.get()*100,2)) + "%")
        dragonearringPercentage.set(str(round(dragonearringCount.get()/dragonraidCount.get()*100,2)) + "%")
        dragonsandPercentage.set(str(round(dragonsandCount.get()/dragonraidCount.get()*100,2)) + "%")

    saveData()

#revans back action button
def revansTakeBack(item):
    #messagebox.showinfo(item)
    #print(item)

    if(item=="trash"):
        if revanstrashCount.get() == 0:
            return
        else:
            revanstrashCount.set(revanstrashCount.get()-1)
    elif(item == "weapon"):
        if revansweaponCount.get() == 0:
            return
        else:
            revansweaponCount.set(revansweaponCount.get()-1)
    elif(item == "sand"):
        if revanssandCount.get() == 0:
            return
        else:
            revanssandCount.set(revanssandCount.get()-1)

    revansraidCount.set(revansraidCount.get() - 1)

    if revansraidCount.get() == 0:
        revanstrashPercentage.set("0.0%")
        revansweaponPercentage.set("0.0%")
        revanssandPercentage.set("0.0%")
    else:
        revanstrashPercentage.set(str(round(revanstrashCount.get()/revansraidCount.get()*100,2)) + "%")
        revansweaponPercentage.set(str(round(revansweaponCount.get()/revansraidCount.get()*100,2)) + "%")
        revanssandPercentage.set(str(round(revanssandCount.get()/revansraidCount.get()*100,2)) + "%")

    saveData()

#revans back action button
def subhlTakeBack(item):
    #messagebox.showinfo(item)
    #print(item)

    if(item=="trash"):
        if subhltrashCount.get() == 0:
            return
        else:
            subhltrashCount.set(subhltrashCount.get()-1)
    elif(item == "sand"):
        if subhlsandCount.get() == 0:
            return
        else:
            subhlsandCount.set(subhlsandCount.get()-1)

    subhlraidCount.set(subhlraidCount.get() - 1)

    if subhlraidCount.get() == 0:
        subhltrashPercentage.set("0.0%")
        subhlsandPercentage.set("0.0%")
    else:
        subhltrashPercentage.set(str(round(subhltrashCount.get()/subhlraidCount.get()*100,2)) + "%")
        subhlsandPercentage.set(str(round(subhlsandCount.get()/subhlraidCount.get()*100,2)) + "%")

    saveData()

#custom1 back action button
def custom1TakeBack(item):
    #messagebox.showinfo(item)
    #print(item)

    if(item=="mat1"):
        if custom1mat1Count.get() == 0:
            return
        else:
            custom1mat1Count.set(custom1mat1Count.get()-1)
    elif(item == "mat2"):
        if custom1mat2Count.get() == 0:
            return
        else:
            custom1mat2Count.set(custom1mat2Count.get()-1)
    elif(item == "mat3"):
        if custom1mat3Count.get() == 0:
            return
        else:
            custom1mat3Count.set(custom1mat3Count.get()-1)
    elif(item == "mat4"):
        if custom1mat4Count.get() == 0:
            return
        else:
            custom1mat4Count.set(custom1mat4Count.get()-1)
    elif(item == "mat5"):
        if custom1mat5Count.get() == 0:
            return
        else:
            custom1mat5Count.set(custom1mat5Count.get()-1)

    custom1raidCount.set(custom1raidCount.get() - 1)

    if custom1raidCount.get() == 0:
        custom1mat1Percentage.set("0.0%")
        custom1mat2Percentage.set("0.0%")
        custom1mat3Percentage.set("0.0%")
        custom1mat4Percentage.set("0.0%")
        custom1mat5Percentage.set("0.0%")
    else:
        custom1mat1Percentage.set(str(round(custom1mat1Count.get()/custom1raidCount.get()*100,2)) + "%")
        custom1mat2Percentage.set(str(round(custom1mat2Count.get()/custom1raidCount.get()*100,2)) + "%")
        custom1mat3Percentage.set(str(round(custom1mat3Count.get()/custom1raidCount.get()*100,2)) + "%")
        custom1mat4Percentage.set(str(round(custom1mat4Count.get()/custom1raidCount.get()*100,2)) + "%")
        custom1mat5Percentage.set(str(round(custom1mat5Count.get()/custom1raidCount.get()*100,2)) + "%")

    saveData()

#custom2 back action button
def custom2TakeBack(item):
    #messagebox.showinfo(item)
    #print(item)

    if(item=="mat1"):
        if custom2mat1Count.get() == 0:
            return
        else:
            custom2mat1Count.set(custom2mat1Count.get()-1)
    elif(item == "mat2"):
        if custom2mat2Count.get() == 0:
            return
        else:
            custom2mat2Count.set(custom2mat2Count.get()-1)
    elif(item == "mat3"):
        if custom2mat3Count.get() == 0:
            return
        else:
            custom2mat3Count.set(custom2mat3Count.get()-1)
    elif(item == "mat4"):
        if custom2mat4Count.get() == 0:
            return
        else:
            custom2mat4Count.set(custom2mat4Count.get()-1)
    elif(item == "mat5"):
        if custom2mat5Count.get() == 0:
            return
        else:
            custom2mat5Count.set(custom2mat5Count.get()-1)

    custom2raidCount.set(custom2raidCount.get() - 1)

    if custom2raidCount.get() == 0:
        custom2mat1Percentage.set("0.0%")
        custom2mat2Percentage.set("0.0%")
        custom2mat3Percentage.set("0.0%")
        custom2mat4Percentage.set("0.0%")
        custom2mat5Percentage.set("0.0%")
    else:
        custom2mat1Percentage.set(str(round(custom2mat1Count.get()/custom2raidCount.get()*100,2)) + "%")
        custom2mat2Percentage.set(str(round(custom2mat2Count.get()/custom2raidCount.get()*100,2)) + "%")
        custom2mat3Percentage.set(str(round(custom2mat3Count.get()/custom2raidCount.get()*100,2)) + "%")
        custom2mat4Percentage.set(str(round(custom2mat4Count.get()/custom2raidCount.get()*100,2)) + "%")
        custom2mat5Percentage.set(str(round(custom2mat5Count.get()/custom2raidCount.get()*100,2)) + "%")

    saveData()

#custom3 back action button
def custom3TakeBack(item):
    #messagebox.showinfo(item)
    #print(item)

    if(item=="mat1"):
        if custom3mat1Count.get() == 0:
            return
        else:
            custom3mat1Count.set(custom3mat1Count.get()-1)
    elif(item == "mat2"):
        if custom1mat2Count.get() == 0:
            return
        else:
            custom3mat2Count.set(custom3mat2Count.get()-1)
    elif(item == "mat3"):
        if custom3mat3Count.get() == 0:
            return
        else:
            custom3mat3Count.set(custom3mat3Count.get()-1)
    elif(item == "mat4"):
        if custom3mat4Count.get() == 0:
            return
        else:
            custom3mat4Count.set(custom3mat4Count.get()-1)
    elif(item == "mat5"):
        if custom3mat5Count.get() == 0:
            return
        else:
            custom3mat5Count.set(custom3mat5Count.get()-1)

    custom3raidCount.set(custom3raidCount.get() - 1)

    if custom3raidCount.get() == 0:
        custom3mat1Percentage.set("0.0%")
        custom3mat2Percentage.set("0.0%")
        custom3mat3Percentage.set("0.0%")
        custom3mat4Percentage.set("0.0%")
        custom3mat5Percentage.set("0.0%")
    else:
        custom3mat1Percentage.set(str(round(custom3mat1Count.get()/custom3raidCount.get()*100,2)) + "%")
        custom3mat2Percentage.set(str(round(custom3mat2Count.get()/custom3raidCount.get()*100,2)) + "%")
        custom3mat3Percentage.set(str(round(custom3mat3Count.get()/custom3raidCount.get()*100,2)) + "%")
        custom3mat4Percentage.set(str(round(custom3mat4Count.get()/custom3raidCount.get()*100,2)) + "%")
        custom3mat5Percentage.set(str(round(custom3mat5Count.get()/custom3raidCount.get()*100,2)) + "%")

    saveData()

#custom4 back action button
def custom4TakeBack(item):
    #messagebox.showinfo(item)
    #print(item)

    if(item=="mat1"):
        if custom4mat1Count.get() == 0:
            return
        else:
            custom4mat1Count.set(custom4mat1Count.get()-1)
    elif(item == "mat2"):
        if custom4mat2Count.get() == 0:
            return
        else:
            custom4mat2Count.set(custom4mat2Count.get()-1)
    elif(item == "mat3"):
        if custom4mat3Count.get() == 0:
            return
        else:
            custom4mat3Count.set(custom4mat3Count.get()-1)
    elif(item == "mat4"):
        if custom4mat4Count.get() == 0:
            return
        else:
            custom4mat4Count.set(custom4mat4Count.get()-1)
    elif(item == "mat5"):
        if custom4mat5Count.get() == 0:
            return
        else:
            custom4mat5Count.set(custom4mat5Count.get()-1)

    custom4raidCount.set(custom4raidCount.get() - 1)

    if custom4raidCount.get() == 0:
        custom4mat1Percentage.set("0.0%")
        custom4mat2Percentage.set("0.0%")
        custom4mat3Percentage.set("0.0%")
        custom4mat4Percentage.set("0.0%")
        custom4mat5Percentage.set("0.0%")
    else:
        custom4mat1Percentage.set(str(round(custom4mat1Count.get()/custom4raidCount.get()*100,2)) + "%")
        custom4mat2Percentage.set(str(round(custom4mat2Count.get()/custom4raidCount.get()*100,2)) + "%")
        custom4mat3Percentage.set(str(round(custom4mat3Count.get()/custom4raidCount.get()*100,2)) + "%")
        custom4mat4Percentage.set(str(round(custom4mat4Count.get()/custom4raidCount.get()*100,2)) + "%")
        custom4mat5Percentage.set(str(round(custom4mat5Count.get()/custom4raidCount.get()*100,2)) + "%")

    saveData()

# PBHL reset
def pbhlresetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

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
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        raidCount.set(0)
        hollowkeyCount.set(0)
        coronaringCount.set(0)
        lineageringCount.set(0)
        intricacyringCount.set(0)
        goldbarCount.set(0)
        hollowkeyPercentage.set("0.0%")
        coronaringPercentage.set("0.0%")
        lineageringPercentage.set("0.0%")
        intricacyringPercentage.set("0.0%")
        goldbarPercentage.set("0.0%")
    else:
        return
    saveData()

def gohlresetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        gohlraidCount.set(0)
        azuriteCount.set(0)
        gohlcoronaringCount.set(0)
        gohllineageringCount.set(0)
        gohlintricacyringCount.set(0)
        gohlgoldbarCount.set(0)
        azuritePercentage.set("0.0%")
        gohlcoronaringPercentage.set("0.0%")
        gohllineageringPercentage.set("0.0%")
        gohlintricacyringPercentage.set("0.0%")
        gohlgoldbarPercentage.set("0.0%")
    else:
        return
    saveData()

# dragons reset state
def dragonresetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        dragonraidCount.set(0)
        dragontrashCount.set(0)
        dragonearringCount.set(0)
        dragonsandCount.set(0)
        dragontrashPercentage.set("0.0%")
        dragonearringPercentage.set("0.0%")
        dragonsandPercentage.set("0.0%")
    else:
        return
    saveData()

def revansresetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        revansraidCount.set(0)
        revanstrashCount.set(0)
        revansweaponCount.set(0)
        revanssandCount.set(0)
        revanstrashPercentage.set("0.0%")
        revansweaponPercentage.set("0.0%")
        revanssandPercentage.set("0.0%")
    else:
        return
    saveData()

def subhlresetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        subhlraidCount.set(0)
        subhltrashCount.set(0)
        subhlsandCount.set(0)
        subhltrashPercentage.set("0.0%")
        subhlsandPercentage.set("0.0%")
    else:
        return
    saveData()

def custom1resetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        custom1raidCount.set(0)
        custom1mat1Count.set(0)
        custom1mat2Count.set(0)
        custom1mat3Count.set(0)
        custom1mat4Count.set(0)
        custom1mat5Count.set(0)
        custom1mat1Percentage.set("0.0%")
        custom1mat2Percentage.set("0.0%")
        custom1mat3Percentage.set("0.0%")
        custom1mat4Percentage.set("0.0%")
        custom1mat5Percentage.set("0.0%")
    else:
        return
    saveData()

def custom2resetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        custom2raidCount.set(0)
        custom2mat1Count.set(0)
        custom2mat2Count.set(0)
        custom2mat3Count.set(0)
        custom2mat4Count.set(0)
        custom2mat5Count.set(0)
        custom2mat1Percentage.set("0.0%")
        custom2mat2Percentage.set("0.0%")
        custom2mat3Percentage.set("0.0%")
        custom2mat4Percentage.set("0.0%")
        custom2mat5Percentage.set("0.0%")
    else:
        return
    saveData()

def custom3resetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        custom3raidCount.set(0)
        custom3mat1Count.set(0)
        custom3mat2Count.set(0)
        custom3mat3Count.set(0)
        custom3mat4Count.set(0)
        custom3mat5Count.set(0)
        custom3mat1Percentage.set("0.0%")
        custom3mat2Percentage.set("0.0%")
        custom3mat3Percentage.set("0.0%")
        custom3mat4Percentage.set("0.0%")
        custom3mat5Percentage.set("0.0%")
    else:
        return
    saveData()

def custom4resetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        custom4raidCount.set(0)
        custom4mat1Count.set(0)
        custom4mat2Count.set(0)
        custom4mat3Count.set(0)
        custom4mat4Count.set(0)
        custom4mat5Count.set(0)
        custom4mat1Percentage.set("0.0%")
        custom4mat2Percentage.set("0.0%")
        custom4mat3Percentage.set("0.0%")
        custom4mat4Percentage.set("0.0%")
        custom4mat5Percentage.set("0.0%")
    else:
        return
    saveData()

def themeSetting(themeColor):
    theme.set(themeColor)
    style.set_theme(theme.get())
    saveData()

# GUI Layout / render

# total pbhl raids
pbhlImg = tk.PhotoImage(file=imgSrc("pbhlCount.png", raid="pbhl"))
pbhlImg = resizeImage(pbhlImg, 50, 50)
pbhlLabel = ttk.Label(pbhlTab, image=pbhlImg).grid(column=0,row=1)
pbhlCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlraidCount).grid(column=0, row=2)

# total akasha raids
akashablueImg = tk.PhotoImage(file=imgSrc("akashaBluechest.png", raid="akasha"))
akashablueImg = resizeImage(akashablueImg, 50, 50)
akashablueLabel = ttk.Label(akashaTab, image=akashablueImg).grid(column=0,row=1)
akashablueCounterLabel = ttk.Label(akashaTab, textvariable=raidCount).grid(column=0, row=2)

# total gohl raids
gohlblueImg = tk.PhotoImage(file=imgSrc("gohlBluechest.png", raid="gohl"))
gohlblueImg = resizeImage(gohlblueImg, 50, 50)
gohlblueLabel = ttk.Label(gohlTab, image=gohlblueImg).grid(column=0,row=1)
gohlblueCounterLabel = ttk.Label(gohlTab, textvariable=gohlraidCount).grid(column=0, row=2)

#umikin is stinky, maki too and udder and munching

# no blue chest
noblueImg = tk.PhotoImage(file=imgSrc("pbhlNobluechest.png", raid="pbhl"))
noblueImg = resizeImage(noblueImg, 50, 50)
# hollowkeyLabel = tttk.Label(akashaTab, text="Hollow key").grid(column=0,row=0)
noblueButton = ttk.Button(pbhlTab, image=noblueImg)
noblueButton.grid(column=1,row=1)
noblueCounterLabel = ttk.Label(pbhlTab, textvariable=noblueCount).grid(column=1,row=2)
#nobluePercentageLabel = ttk.Label(pbhlTab, textvariable=nobluePercentage).grid(column=1,row=3)
noblueButton.bind('<Button-1>', lambda event: pbhlCallBack("noblue"))
noblueButton.bind('<Button-2>', lambda event: pbhlTakeBack("noblue"))
noblueButton.bind('<Button-3>', lambda event: pbhlTakeBack("noblue"))

# hollow key
hollowkeyImg = tk.PhotoImage(file=imgSrc("akashaLitter.png", raid="akasha"))
hollowkeyImg = resizeImage(hollowkeyImg, 50, 50)
# hollowkeyLabel = tttk.Label(akashaTab, text="Hollow key").grid(column=0,row=0)
hollowkeyButton = ttk.Button(akashaTab, image=hollowkeyImg)
hollowkeyButton.grid(column=1,row=1)
hollowkeyCounterLabel = ttk.Label(akashaTab, textvariable=hollowkeyCount).grid(column=1,row=2)
hollowkeyPercentageLabel = ttk.Label(akashaTab, textvariable=hollowkeyPercentage).grid(column=1,row=3)
hollowkeyButton.bind('<Button-1>', lambda event: buttonCallBack("hollowkey"))
hollowkeyButton.bind('<Button-2>', lambda event: buttonTakeBack("hollowkey"))
hollowkeyButton.bind('<Button-3>', lambda event: buttonTakeBack("hollowkey"))

# azurite
azuriteImg = tk.PhotoImage(file=imgSrc("gohlLitter.png", raid="gohl"))
azuriteImg = resizeImage(azuriteImg, 50, 50)
# hollowkeyLabel = tttk.Label(akashaTab, text="Hollow key").grid(column=0,row=0)
azuriteButton = ttk.Button(gohlTab, image=azuriteImg)
azuriteButton.grid(column=1,row=1)
azuriteCounterLabel = ttk.Label(gohlTab, textvariable=azuriteCount).grid(column=1,row=2)
azuritePercentageLabel = ttk.Label(gohlTab, textvariable=azuritePercentage).grid(column=1,row=3)
azuriteButton.bind('<Button-1>', lambda event: gohlCallBack("azurite"))
azuriteButton.bind('<Button-2>', lambda event: gohlTakeBack("azurite"))
azuriteButton.bind('<Button-3>', lambda event: gohlTakeBack("azurite"))

# pbhl corona ring
pbhlcoronaringImg = tk.PhotoImage(file=imgSrc("pbhlCoronationring.png", raid="pbhl"))
pbhlcoronaringImg = resizeImage(pbhlcoronaringImg, 50, 50)
# coronaringLabel = tttk.Label(akashaTab, text="Coronation Ring").grid(column=1,row=0)
pbhlcoronaringButton = ttk.Button(pbhlTab, image=pbhlcoronaringImg)
pbhlcoronaringButton.grid(column=2,row=1)
pbhlcoronaringCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlcoronaringCount).grid(column=2,row=2)
pbhlcoronaringPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhlcoronaringPercentage).grid(column=2,row=3)
pbhlcoronaringButton.bind('<Button-1>', lambda event: pbhlCallBack("coronaring"))
pbhlcoronaringButton.bind('<Button-2>', lambda event: pbhlTakeBack("coronaring"))
pbhlcoronaringButton.bind('<Button-3>', lambda event: pbhlTakeBack("coronaring"))

# Akasha corona ring
coronaringImg = tk.PhotoImage(file=imgSrc("akashaCoronationring.png", raid="akasha"))
coronaringImg = resizeImage(coronaringImg, 50, 50)
# coronaringLabel = tttk.Label(akashaTab, text="Coronation Ring").grid(column=1,row=0)
coronaringButton = ttk.Button(akashaTab, image=coronaringImg)
coronaringButton.grid(column=2,row=1)
coronaringCounterLabel = ttk.Label(akashaTab, textvariable=coronaringCount).grid(column=2,row=2)
coronaringPercentageLabel = ttk.Label(akashaTab, textvariable=coronaringPercentage).grid(column=2,row=3)
coronaringButton.bind('<Button-1>', lambda event: buttonCallBack("coronaring"))
coronaringButton.bind('<Button-2>', lambda event: buttonTakeBack("coronaring"))
coronaringButton.bind('<Button-3>', lambda event: buttonTakeBack("coronaring"))

# gohl corona ring
gohlcoronaringImg = tk.PhotoImage(file=imgSrc("gohlCoronationring.png", raid="gohl"))
gohlcoronaringImg = resizeImage(gohlcoronaringImg, 50, 50)
# coronaringLabel = tttk.Label(akashaTab, text="Coronation Ring").grid(column=1,row=0)
gohlcoronaringButton = ttk.Button(gohlTab, image=gohlcoronaringImg)
gohlcoronaringButton.grid(column=2,row=1)
gohlcoronaringCounterLabel = ttk.Label(gohlTab, textvariable=gohlcoronaringCount).grid(column=2,row=2)
gohlcoronaringPercentageLabel = ttk.Label(gohlTab, textvariable=gohlcoronaringPercentage).grid(column=2,row=3)
gohlcoronaringButton.bind('<Button-1>', lambda event: gohlCallBack("coronaring"))
gohlcoronaringButton.bind('<Button-2>', lambda event: gohlTakeBack("coronaring"))
gohlcoronaringButton.bind('<Button-3>', lambda event: gohlTakeBack("coronaring"))

# pbhl lineage ring
pbhllineageringImg = tk.PhotoImage(file=imgSrc("pbhlLineagering.png", raid="pbhl"))
pbhllineageringImg = resizeImage(pbhllineageringImg, 50, 50)
# lineageringLabel = tttk.Label(akashaTab, text="Lineage Ring").grid(column=2,row=0)
pbhllineageringButton = ttk.Button(pbhlTab, image=pbhllineageringImg)
pbhllineageringButton.grid(column=3,row=1)
pbhllineageringCounterLabel = ttk.Label(pbhlTab, textvariable=pbhllineageringCount).grid(column=3,row=2)
pbhllineageringPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhllineageringPercentage).grid(column=3,row=3)
pbhllineageringButton.bind('<Button-1>', lambda event: pbhlCallBack("lineagering"))
pbhllineageringButton.bind('<Button-2>', lambda event: pbhlTakeBack("lineagering"))
pbhllineageringButton.bind('<Button-3>', lambda event: pbhlTakeBack("lineagering"))

# Akasha lineage ring
lineageringImg = tk.PhotoImage(file=imgSrc("akashaLineagering.png", raid="akasha"))
lineageringImg = resizeImage(lineageringImg, 50, 50)
# lineageringLabel = tttk.Label(akashaTab, text="Lineage Ring").grid(column=2,row=0)
lineageringButton = ttk.Button(akashaTab, image=lineageringImg)
lineageringButton.grid(column=3,row=1)
lineageringCounterLabel = ttk.Label(akashaTab, textvariable=lineageringCount).grid(column=3,row=2)
lineageringPercentageLabel = ttk.Label(akashaTab, textvariable=lineageringPercentage).grid(column=3,row=3)
lineageringButton.bind('<Button-1>', lambda event: buttonCallBack("lineagering"))
lineageringButton.bind('<Button-2>', lambda event: buttonTakeBack("lineagering"))
lineageringButton.bind('<Button-3>', lambda event: buttonTakeBack("lineagering"))

# gohl lineage ring
gohllineageringImg = tk.PhotoImage(file=imgSrc("gohlLineagering.png", raid="gohl"))
gohllineageringImg = resizeImage(gohllineageringImg, 50, 50)
# lineageringLabel = tttk.Label(akashaTab, text="Lineage Ring").grid(column=2,row=0)
gohllineageringButton = ttk.Button(gohlTab, image=gohllineageringImg)
gohllineageringButton.grid(column=3,row=1)
gohllineageringCounterLabel = ttk.Label(gohlTab, textvariable=gohllineageringCount).grid(column=3,row=2)
gohllineageringPercentageLabel = ttk.Label(gohlTab, textvariable=gohllineageringPercentage).grid(column=3,row=3)
gohllineageringButton.bind('<Button-1>', lambda event: gohlCallBack("lineagering"))
gohllineageringButton.bind('<Button-2>', lambda event: gohlTakeBack("lineagering"))
gohllineageringButton.bind('<Button-3>', lambda event: gohlTakeBack("lineagering"))

# pbhl intricacy ring
pbhlintricacyringImg = tk.PhotoImage(file=imgSrc("pbhlIntricacyring.png", raid="pbhl"))
pbhlintricacyringImg = resizeImage(pbhlintricacyringImg, 50, 50)
# intricacyringLabel = tttk.Label(akashaTab, text="Intricacy Ring").grid(column=3,row=0)
# intricacyringButton = ttk.Button(akashaTab, image=intricacyringImg, command=lambda:buttonCallBack("intricacyring")).grid(column=4,row=1)
pbhlintricacyringButton = ttk.Button(pbhlTab, image=pbhlintricacyringImg)
pbhlintricacyringButton.grid(column=4,row=1)
pbhlintricacyringCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlintricacyringCount).grid(column=4,row=2)
pbhlintricacyringPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhlintricacyringPercentage).grid(column=4,row=3)
pbhlintricacyringButton.bind('<Button-1>', lambda event: pbhlCallBack("intricacyring"))
pbhlintricacyringButton.bind('<Button-2>', lambda event: pbhlTakeBack("intricacyring"))
pbhlintricacyringButton.bind('<Button-3>', lambda event: pbhlTakeBack("intricacyring"))

# Akasha intricacy ring
intricacyringImg = tk.PhotoImage(file=imgSrc("akashaIntricacyring.png", raid="akasha"))
intricacyringImg = resizeImage(intricacyringImg, 50, 50)
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
gohlintricacyringImg = tk.PhotoImage(file=imgSrc("gohlIntricacyring.png", raid="gohl"))
gohlintricacyringImg = resizeImage(gohlintricacyringImg, 50, 50)
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
pbhlgoldbarImg = tk.PhotoImage(file=imgSrc("pbhlGoldbar.png", raid="pbhl"))
pbhlgoldbarImg = resizeImage(pbhlgoldbarImg, 50, 50)
# goldbarLabel = tttk.Label(akashaTab, text="Gold Bar").grid(column=4,row=0)
pbhlgoldbarButton = ttk.Button(pbhlTab, image=pbhlgoldbarImg)
pbhlgoldbarButton.grid(column=5,row=1)
pbhlgoldbarCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlgoldbarCount).grid(column=5,row=2)
pbhlgoldbarPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhlgoldbarPercentage).grid(column=5,row=3)
pbhlgoldbarButton.bind('<Button-1>', lambda event: pbhlCallBack("goldbar"))
pbhlgoldbarButton.bind('<Button-2>', lambda event: pbhlTakeBack("goldbar"))
pbhlgoldbarButton.bind('<Button-3>', lambda event: pbhlTakeBack("goldbar"))

# Akasha gold bar
goldbarImg = tk.PhotoImage(file=imgSrc("akashaGoldbar.png", raid="akasha"))
goldbarImg = resizeImage(goldbarImg, 50, 50)
# goldbarLabel = tttk.Label(akashaTab, text="Gold Bar").grid(column=4,row=0)
goldbarButton = ttk.Button(akashaTab, image=goldbarImg)
goldbarButton.grid(column=5,row=1)
goldbarCounterLabel = ttk.Label(akashaTab, textvariable=goldbarCount).grid(column=5,row=2)
goldbarPercentageLabel = ttk.Label(akashaTab, textvariable=goldbarPercentage).grid(column=5,row=3)
goldbarButton.bind('<Button-1>', lambda event: buttonCallBack("goldbar"))
goldbarButton.bind('<Button-2>', lambda event: buttonTakeBack("goldbar"))
goldbarButton.bind('<Button-3>', lambda event: buttonTakeBack("goldbar"))

# gohl gold bar
gohlgoldbarImg = tk.PhotoImage(file=imgSrc("gohlGoldbar.png", raid="gohl"))
gohlgoldbarImg = resizeImage(gohlgoldbarImg, 50, 50)
# goldbarLabel = tttk.Label(akashaTab, text="Gold Bar").grid(column=4,row=0)
gohlgoldbarButton = ttk.Button(gohlTab, image=gohlgoldbarImg)
gohlgoldbarButton.grid(column=5,row=1)
gohlgoldbarCounterLabel = ttk.Label(gohlTab, textvariable=gohlgoldbarCount).grid(column=5,row=2)
gohlgoldbarPercentageLabel = ttk.Label(gohlTab, textvariable=gohlgoldbarPercentage).grid(column=5,row=3)
gohlgoldbarButton.bind('<Button-1>', lambda event: gohlCallBack("goldbar"))
gohlgoldbarButton.bind('<Button-2>', lambda event: gohlTakeBack("goldbar"))
gohlgoldbarButton.bind('<Button-3>', lambda event: gohlTakeBack("goldbar"))

# total dragons raids
dragonCountImg = tk.PhotoImage(file=imgSrc("dragonCount.png", raid="dragon"))
dragonCountImg = resizeImage(dragonCountImg, 50, 50)
dragonCountLabel = ttk.Label(dragonTab, image=dragonCountImg).grid(column=0,row=1)
dragonCounterLabel = ttk.Label(dragonTab, textvariable=dragonraidCount).grid(column=0, row=2)

# dragon trash
dragontrashImg = tk.PhotoImage(file=imgSrc("dragonLitter.png", raid="dragon"))
dragontrashImg = resizeImage(dragontrashImg, 50, 50)
dragontrashButton = ttk.Button(dragonTab, image=dragontrashImg)
dragontrashButton.grid(column=1,row=1)
dragontrashCounterLabel = ttk.Label(dragonTab, textvariable=dragontrashCount).grid(column=1,row=2)
dragontrashPercentageLabel = ttk.Label(dragonTab, textvariable=dragontrashPercentage).grid(column=1,row=3)
dragontrashButton.bind('<Button-1>', lambda event: dragonCallBack("trash"))
dragontrashButton.bind('<Button-2>', lambda event: dragonTakeBack("trash"))
dragontrashButton.bind('<Button-3>', lambda event: dragonTakeBack("trash"))

# dragon earring
dragonearringImg = tk.PhotoImage(file=imgSrc("dragonEarring.png", raid="dragon"))
dragonearringImg = resizeImage(dragonearringImg, 50, 50)
dragonearringButton = ttk.Button(dragonTab, image=dragonearringImg)
dragonearringButton.grid(column=2,row=1)
dragonearringCounterLabel = ttk.Label(dragonTab, textvariable=dragonearringCount).grid(column=2,row=2)
dragonearringPercentageLabel = ttk.Label(dragonTab, textvariable=dragonearringPercentage).grid(column=2,row=3)
dragonearringButton.bind('<Button-1>', lambda event: dragonCallBack("earring"))
dragonearringButton.bind('<Button-2>', lambda event: dragonTakeBack("earring"))
dragonearringButton.bind('<Button-3>', lambda event: dragonTakeBack("earring"))

# dragon sand
dragonsandImg = tk.PhotoImage(file=imgSrc("dragonSand.png", raid="dragon"))
dragonsandImg = resizeImage(dragonsandImg, 50, 50)
dragonsandButton = ttk.Button(dragonTab, image=dragonsandImg)
dragonsandButton.grid(padx= [15,0], column=5,row=1)
dragonsandCounterLabel = ttk.Label(dragonTab, textvariable=dragonsandCount).grid(padx= [15,0], column=5,row=2)
dragonsandPercentageLabel = ttk.Label(dragonTab, textvariable=dragonsandPercentage).grid(padx= [15,0], column=5,row=3)
dragonsandButton.bind('<Button-1>', lambda event: dragonCallBack("sand"))
dragonsandButton.bind('<Button-2>', lambda event: dragonTakeBack("sand"))
dragonsandButton.bind('<Button-3>', lambda event: dragonTakeBack("sand"))

# dragon reset button
dragonresetButton = ttk.Button(dragonTab, text="Reset", command=lambda:dragonresetCount(), width=12).grid(padx= [45,0], column=6, row=5)

# Dragon Anima Count
if drop['dragon']['animabefore'] == "" and drop['dragon']['animaafter'] =="":
    dragonAnimaSinceLabel = StringVar(value="Mats since:" + "\n" + "0")
elif drop['dragon']['animabefore'] == "":
    dragonAnimaSinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['dragon']['animaafter']))))
elif drop['dragon']['animaafter'] == "":
    dragonAnimaSinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['dragon']['animabefore']))))
else:
    dragonAnimaSinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['dragon']['animabefore'])-int(drop['dragon']['animaafter']))))

def dragonAnimaDifference(e):
    if dragonAnimaTextAfter.get() == "" and dragonAnimaTextBefore.get() == "":
        dragonAnimaSinceLabel.set("Mats since:" + "\n" + "0")
    elif dragonAnimaTextAfter.get() == "":
        dragonAnimaSinceLabel.set("Mats since:" + "\n" + str(abs(int(dragonAnimaTextBefore.get()))))
    elif dragonAnimaTextBefore.get() == "":
        dragonAnimaSinceLabel.set("Mats since:" + "\n" + str(abs(int(dragonAnimaTextAfter.get()))))
    else:
        dragonAnimaSinceLabel.set("Mats since:" + "\n" + str(abs(int(dragonAnimaTextBefore.get()) - int(dragonAnimaTextAfter.get()))))

    saveData()

dragonanimaImg = tk.PhotoImage(file=imgSrc("dragonAnima.png", raid="dragon"))
dragonanimaImg = resizeImage(dragonanimaImg, 25, 25)
dragonanimaImgLabel = ttk.Label(dragonTab, image=dragonanimaImg)
dragonanimaImgLabel.grid(column=0, row=4, sticky= tk.W)

dragonAnimaText = ttk.Label(dragonTab, textvariable=dragonAnimaSinceLabel, justify="left")
dragonAnimaText.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

dragonAnimaTextBefore = ttk.Entry(dragonTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
dragonAnimaTextBefore.grid(column=1, columnspan=2, row=4)
dragonAnimaTextBefore.insert(0, drop['dragon']['animabefore'])
dragonAnimaTextBefore.bind("<KeyRelease>", dragonAnimaDifference)

dragonAnimaTextAfter = ttk.Entry(dragonTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
dragonAnimaTextAfter.grid(column=1, columnspan=2, row=5)
dragonAnimaTextAfter.insert(0, drop['dragon']['animaafter'])
dragonAnimaTextAfter.bind("<KeyRelease>", dragonAnimaDifference)

# total revans raids
revansCountImg = tk.PhotoImage(file=imgSrc("revansCount.png", raid="revans"))
revansCountImg = resizeImage(revansCountImg, 50, 50)
revansCountLabel = ttk.Label(revansTab, image=revansCountImg).grid(column=0,row=1)
revansCounterLabel = ttk.Label(revansTab, textvariable=revansraidCount).grid(column=0, row=2)

# revans trash
revanstrashImg = tk.PhotoImage(file=imgSrc("revansLitter.png", raid="revans"))
revanstrashImg = resizeImage(revanstrashImg, 50, 50)
revanstrashButton = ttk.Button(revansTab, image=revanstrashImg)
revanstrashButton.grid(column=1,row=1)
revanstrashCounterLabel = ttk.Label(revansTab, textvariable=revanstrashCount).grid(column=1,row=2)
revanstrashPercentageLabel = ttk.Label(revansTab, textvariable=revanstrashPercentage).grid(column=1,row=3)
revanstrashButton.bind('<Button-1>', lambda event: revansCallBack("trash"))
revanstrashButton.bind('<Button-2>', lambda event: revansTakeBack("trash"))
revanstrashButton.bind('<Button-3>', lambda event: revansTakeBack("trash"))

# revans weapon
revansweaponImg = tk.PhotoImage(file=imgSrc("revansWeapon.png", raid="revans"))
revansweaponImg = resizeImage(revansweaponImg, 50, 50)
revansweaponButton = ttk.Button(revansTab, image=revansweaponImg)
revansweaponButton.grid(column=2,row=1)
revansweaponCounterLabel = ttk.Label(revansTab, textvariable=revansweaponCount).grid(column=2,row=2)
revansweaponPercentageLabel = ttk.Label(revansTab, textvariable=revansweaponPercentage).grid(column=2,row=3)
revansweaponButton.bind('<Button-1>', lambda event: revansCallBack("weapon"))
revansweaponButton.bind('<Button-2>', lambda event: revansTakeBack("weapon"))
revansweaponButton.bind('<Button-3>', lambda event: revansTakeBack("weapon"))

# revans sand
revanssandImg = tk.PhotoImage(file=imgSrc("revansSand.png", raid="revans"))
revanssandImg = resizeImage(revanssandImg, 50, 50)
revanssandButton = ttk.Button(revansTab, image=revanssandImg)
revanssandButton.grid(padx= [15,0],column=5,row=1)
revanssandCounterLabel = ttk.Label(revansTab, textvariable=revanssandCount).grid(padx= [15,0],column=5,row=2)
revanssandPercentageLabel = ttk.Label(revansTab, textvariable=revanssandPercentage).grid(padx= [15,0],column=5,row=3)
revanssandButton.bind('<Button-1>', lambda event: revansCallBack("sand"))
revanssandButton.bind('<Button-2>', lambda event: revansTakeBack("sand"))
revanssandButton.bind('<Button-3>', lambda event: revansTakeBack("sand"))

# revans reset button
revansresetButton = ttk.Button(revansTab, text="Reset", command=lambda:revansresetCount(), width=12).grid(padx= [45,0],column=6, row=5)

# revans Anima Count
if drop['revans']['animabefore'] == "" and drop['revans']['animaafter'] =="":
    revansAnimaSinceLabel = StringVar(value="Mats since:" + "\n" + "0")
elif drop['revans']['animabefore'] == "":
    revansAnimaSinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['revans']['animaafter']))))
elif drop['revans']['animaafter'] == "":
    revansAnimaSinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['revans']['animabefore']))))
else:
    revansAnimaSinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['revans']['animabefore'])-int(drop['revans']['animaafter']))))

def revansAnimaDifference(e):
    if revansAnimaTextAfter.get() == "" and revansAnimaTextBefore.get() == "":
        revansAnimaSinceLabel.set("Mats since:" + "\n" + "0")
    elif revansAnimaTextAfter.get() == "":
        revansAnimaSinceLabel.set("Mats since:" + "\n" + str(abs(int(revansAnimaTextBefore.get()))))
    elif revansAnimaTextBefore.get() == "":
        revansAnimaSinceLabel.set("Mats since:" + "\n" + str(abs(int(revansAnimaTextAfter.get()))))
    else:
        revansAnimaSinceLabel.set("Mats since:" + "\n" + str(abs(int(revansAnimaTextBefore.get()) - int(revansAnimaTextAfter.get()))))

    saveData()

revansanimaImg = tk.PhotoImage(file=imgSrc("revansAnima.png", raid="revans"))
revansanimaImg = resizeImage(revansanimaImg, 25, 25)
revansanimaImgLabel = ttk.Label(revansTab, image=revansanimaImg)
revansanimaImgLabel.grid(column=0, row=4, sticky= tk.W)

revansAnimaText = ttk.Label(revansTab, textvariable=revansAnimaSinceLabel, justify="left")
revansAnimaText.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

revansAnimaTextBefore = ttk.Entry(revansTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
revansAnimaTextBefore.grid(column=1, columnspan=2, row=4)
revansAnimaTextBefore.insert(0, drop['revans']['animabefore'])
revansAnimaTextBefore.bind("<KeyRelease>", revansAnimaDifference)

revansAnimaTextAfter = ttk.Entry(revansTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
revansAnimaTextAfter.grid(column=1, columnspan=2, row=5)
revansAnimaTextAfter.insert(0, drop['revans']['animaafter'])
revansAnimaTextAfter.bind("<KeyRelease>", revansAnimaDifference)

# total subhl raids
subhlCountImg = tk.PhotoImage(file=imgSrc("subhlCount.png", raid="subhl"))
subhlCountImg = resizeImage(subhlCountImg, 50, 50)
subhlCountLabel = ttk.Label(subhlTab, image=subhlCountImg).grid(column=0,row=1)
subhlCounterLabel = ttk.Label(subhlTab, textvariable=subhlraidCount).grid(column=0, row=2)

# subhl trash
subhltrashImg = tk.PhotoImage(file=imgSrc("subhlLitter.png", raid="subhl"))
subhltrashImg = resizeImage(subhltrashImg, 50, 50)
subhltrashButton = ttk.Button(subhlTab, image=subhltrashImg)
subhltrashButton.grid(column=1,row=1)
subhltrashCounterLabel = ttk.Label(subhlTab, textvariable=subhltrashCount).grid(column=1,row=2)
subhltrashPercentageLabel = ttk.Label(subhlTab, textvariable=subhltrashPercentage).grid(column=1,row=3)
subhltrashButton.bind('<Button-1>', lambda event: subhlCallBack("trash"))
subhltrashButton.bind('<Button-2>', lambda event: subhlTakeBack("trash"))
subhltrashButton.bind('<Button-3>', lambda event: subhlTakeBack("trash"))

# subhl sand
subhlsandImg = tk.PhotoImage(file=imgSrc("subhlSand.png", raid="subhl"))
subhlsandImg = resizeImage(subhlsandImg, 50, 50)
subhlsandButton = ttk.Button(subhlTab, image=subhlsandImg)
subhlsandButton.grid(column=3,row=1)
subhlsandCounterLabel = ttk.Label(subhlTab, textvariable=subhlsandCount).grid(column=3,row=2)
subhlsandPercentageLabel = ttk.Label(subhlTab, textvariable=subhlsandPercentage).grid(column=3,row=3)
subhlsandButton.bind('<Button-1>', lambda event: subhlCallBack("sand"))
subhlsandButton.bind('<Button-2>', lambda event: subhlTakeBack("sand"))
subhlsandButton.bind('<Button-3>', lambda event: subhlTakeBack("sand"))

# subhl reset button
subhlresetButton = ttk.Button(subhlTab, text="Reset", command=lambda:subhlresetCount(), width=12).grid(padx= [102,0], column=4, row=5)

# subhl Anima Count
if drop['subhl']['animabefore'] == "" and drop['subhl']['animaafter'] =="":
    subhlAnimaSinceLabel = StringVar(value="Prisms:" + "\n" + "0")
elif drop['subhl']['animabefore'] == "":
    subhlAnimaSinceLabel = StringVar(value="Prisms:" + "\n" + str(abs(int(drop['subhl']['animaafter']))))
elif drop['subhl']['animaafter'] == "":
    subhlAnimaSinceLabel = StringVar(value="Prisms:" + "\n" + str(abs(int(drop['subhl']['animabefore']))))
else:
    subhlAnimaSinceLabel = StringVar(value="Prisms:" + "\n" + str(abs(int(drop['subhl']['animabefore'])-int(drop['subhl']['animaafter']))))

def subhlAnimaDifference(e):
    if subhlAnimaTextAfter.get() == "" and subhlAnimaTextBefore.get() == "":
        subhlAnimaSinceLabel.set("Prisms:" + "\n" + "0")
    elif subhlAnimaTextAfter.get() == "":
        subhlAnimaSinceLabel.set("Prisms:" + "\n" + str(abs(int(subhlAnimaTextBefore.get()))))
    elif subhlAnimaTextBefore.get() == "":
        subhlAnimaSinceLabel.set("Prisms:" + "\n" + str(abs(int(subhlAnimaTextAfter.get()))))
    else:
        subhlAnimaSinceLabel.set("Prisms:" + "\n" + str(abs(int(subhlAnimaTextBefore.get()) - int(subhlAnimaTextAfter.get()))))

    saveData()

subhlanimaImg = tk.PhotoImage(file=imgSrc("subhlAnima.png", raid="subhl"))
subhlanimaImg = resizeImage(subhlanimaImg, 25, 25)
subhlanimaImgLabel = ttk.Label(subhlTab, image=subhlanimaImg)
subhlanimaImgLabel.grid(column=0, row=4, sticky= tk.W)

subhlAnimaText = ttk.Label(subhlTab, textvariable=subhlAnimaSinceLabel, justify="left")
subhlAnimaText.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

subhlAnimaTextBefore = ttk.Entry(subhlTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
subhlAnimaTextBefore.grid(column=1, columnspan=2, row=4)
subhlAnimaTextBefore.insert(0, drop['subhl']['animabefore'])
subhlAnimaTextBefore.bind("<KeyRelease>", subhlAnimaDifference)

subhlAnimaTextAfter = ttk.Entry(subhlTab, width=12, validate='key', validatecommand=(vcmd, '%P'))
subhlAnimaTextAfter.grid(column=1, columnspan=2, row=5)
subhlAnimaTextAfter.insert(0, drop['subhl']['animaafter'])
subhlAnimaTextAfter.bind("<KeyRelease>", subhlAnimaDifference)

# total custom1 raids
custom1CountImg = tk.PhotoImage(file=imgSrc("custom1count.png", raid="custom1"))
custom1CountImg = resizeImage(custom1CountImg, 50, 50)
custom1CountLabel = ttk.Label(custom1Tab, image=custom1CountImg).grid(column=0,row=1)
custom1CounterLabel = ttk.Label(custom1Tab, textvariable=custom1raidCount).grid(column=0, row=2)

# custom1mat1
custom1mat1Img = tk.PhotoImage(file=imgSrc("custom1mat1.png", raid="custom1"))
custom1mat1Img = resizeImage(custom1mat1Img, 50, 50)
custom1mat1Button = ttk.Button(custom1Tab, image=custom1mat1Img)
custom1mat1Button.grid(column=1,row=1)
custom1mat1CounterLabel = ttk.Label(custom1Tab, textvariable=custom1mat1Count).grid(column=1,row=2)
custom1mat1PercentageLabel = ttk.Label(custom1Tab, textvariable=custom1mat1Percentage).grid(column=1,row=3)
custom1mat1Button.bind('<Button-1>', lambda event: custom1CallBack("mat1"))
custom1mat1Button.bind('<Button-2>', lambda event: custom1TakeBack("mat1"))
custom1mat1Button.bind('<Button-3>', lambda event: custom1TakeBack("mat1"))

# custom1mat2
custom1mat2Img = tk.PhotoImage(file=imgSrc("custom1mat2.png", raid="custom1"))
custom1mat2Img = resizeImage(custom1mat2Img, 50, 50)
custom1mat2Button = ttk.Button(custom1Tab, image=custom1mat2Img)
custom1mat2Button.grid(column=2,row=1)
custom1mat2CounterLabel = ttk.Label(custom1Tab, textvariable=custom1mat2Count).grid(column=2,row=2)
custom1mat2PercentageLabel = ttk.Label(custom1Tab, textvariable=custom1mat2Percentage).grid(column=2,row=3)
custom1mat2Button.bind('<Button-1>', lambda event: custom1CallBack("mat2"))
custom1mat2Button.bind('<Button-2>', lambda event: custom1TakeBack("mat2"))
custom1mat2Button.bind('<Button-3>', lambda event: custom1TakeBack("mat2"))

# custom1mat3
custom1mat3Img = tk.PhotoImage(file=imgSrc("custom1mat3.png", raid="custom1"))
custom1mat3Img = resizeImage(custom1mat3Img, 50, 50)
custom1mat3Button = ttk.Button(custom1Tab, image=custom1mat3Img)
custom1mat3Button.grid(column=3,row=1)
custom1mat3CounterLabel = ttk.Label(custom1Tab, textvariable=custom1mat3Count).grid(column=3,row=2)
custom1mat3PercentageLabel = ttk.Label(custom1Tab, textvariable=custom1mat3Percentage).grid(column=3,row=3)
custom1mat3Button.bind('<Button-1>', lambda event: custom1CallBack("mat3"))
custom1mat3Button.bind('<Button-2>', lambda event: custom1TakeBack("mat3"))
custom1mat3Button.bind('<Button-3>', lambda event: custom1TakeBack("mat3"))

# custom1mat4
custom1mat4Img = tk.PhotoImage(file=imgSrc("custom1mat4.png", raid="custom1"))
custom1mat4Img = resizeImage(custom1mat4Img, 50, 50)
custom1mat4Button = ttk.Button(custom1Tab, image=custom1mat4Img)
custom1mat4Button.grid(column=4,row=1)
custom1mat4CounterLabel = ttk.Label(custom1Tab, textvariable=custom1mat4Count).grid(column=4,row=2)
custom1mat4PercentageLabel = ttk.Label(custom1Tab, textvariable=custom1mat4Percentage).grid(column=4,row=3)
custom1mat4Button.bind('<Button-1>', lambda event: custom1CallBack("mat4"))
custom1mat4Button.bind('<Button-2>', lambda event: custom1TakeBack("mat4"))
custom1mat4Button.bind('<Button-3>', lambda event: custom1TakeBack("mat4"))

# custom1mat5
custom1mat5Img = tk.PhotoImage(file=imgSrc("custom1mat5.png", raid="custom1"))
custom1mat5Img = resizeImage(custom1mat5Img, 50, 50)
custom1mat5Button = ttk.Button(custom1Tab, image=custom1mat5Img)
custom1mat5Button.grid(column=5,row=1)
custom1mat5CounterLabel = ttk.Label(custom1Tab, textvariable=custom1mat5Count).grid(column=5,row=2)
custom1mat5PercentageLabel = ttk.Label(custom1Tab, textvariable=custom1mat5Percentage).grid(column=5,row=3)
custom1mat5Button.bind('<Button-1>', lambda event: custom1CallBack("mat5"))
custom1mat5Button.bind('<Button-2>', lambda event: custom1TakeBack("mat5"))
custom1mat5Button.bind('<Button-3>', lambda event: custom1TakeBack("mat5"))

# custom1 reset button
custom1resetButton = ttk.Button(custom1Tab, text="Reset", command=lambda:custom1resetCount(), width=12).grid(column=5, row=5)

# custom1 Mat Count
if drop['custom1']['animabefore'] == "" and drop['custom1']['animaafter'] =="":
    custom1SinceLabel = StringVar(value="Mats since:" + "\n" + "0")
elif drop['custom1']['animabefore'] == "":
    custom1SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom1']['animaafter']))))
elif drop['custom1']['animaafter'] == "":
    custom1SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom1']['animabefore']))))
else:
    custom1SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom1']['animabefore'])-int(drop['custom1']['animaafter']))))

def custom1MatsDifference(e):
    if custom1TextAfter.get() == "" and custom1TextBefore.get() == "":
        custom1SinceLabel.set("Mats since:" + "\n" + "0")
    elif custom1TextAfter.get() == "":
        custom1SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom1TextBefore.get()))))
    elif custom1TextBefore.get() == "":
        custom1SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom1TextAfter.get()))))
    else:
        custom1SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom1TextBefore.get()) - int(custom1TextAfter.get()))))

    saveData()

custom1Img = tk.PhotoImage(file=imgSrc("custom1anima.png", raid="custom1"))
custom1Img = resizeImage(custom1Img, 25, 25)
custom1ImgLabel = ttk.Label(custom1Tab, image=custom1Img)
custom1ImgLabel.grid(column=0, row=4, sticky= tk.W)

custom1Text = ttk.Label(custom1Tab, textvariable=custom1SinceLabel, justify="left")
custom1Text.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

custom1TextBefore = ttk.Entry(custom1Tab, width=12, validate='key', validatecommand=(vcmd, '%P'))
custom1TextBefore.grid(column=1, columnspan=2, row=4)
custom1TextBefore.insert(0, drop['custom1']['animabefore'])
custom1TextBefore.bind("<KeyRelease>", custom1MatsDifference)

custom1TextAfter = ttk.Entry(custom1Tab, width=12, validate='key', validatecommand=(vcmd, '%P'))
custom1TextAfter.grid(column=1, columnspan=2, row=5)
custom1TextAfter.insert(0, drop['custom1']['animaafter'])
custom1TextAfter.bind("<KeyRelease>", custom1MatsDifference)

# total custom2 raids
custom2CountImg = tk.PhotoImage(file=imgSrc("custom2count.png", raid="custom2"))
custom2CountImg = resizeImage(custom2CountImg, 50, 50)
custom2CountLabel = ttk.Label(custom2Tab, image=custom2CountImg).grid(column=0,row=1)
custom2CounterLabel = ttk.Label(custom2Tab, textvariable=custom2raidCount).grid(column=0, row=2)

# custom2mat1
custom2mat1Img = tk.PhotoImage(file=imgSrc("custom2mat1.png", raid="custom2"))
custom2mat1Img = resizeImage(custom2mat1Img, 50, 50)
custom2mat1Button = ttk.Button(custom2Tab, image=custom2mat1Img)
custom2mat1Button.grid(column=1,row=1)
custom2mat1CounterLabel = ttk.Label(custom2Tab, textvariable=custom2mat1Count).grid(column=1,row=2)
custom2mat1PercentageLabel = ttk.Label(custom2Tab, textvariable=custom2mat1Percentage).grid(column=1,row=3)
custom2mat1Button.bind('<Button-1>', lambda event: custom2CallBack("mat1"))
custom2mat1Button.bind('<Button-2>', lambda event: custom2TakeBack("mat1"))
custom2mat1Button.bind('<Button-3>', lambda event: custom2TakeBack("mat1"))

# custom2mat2
custom2mat2Img = tk.PhotoImage(file=imgSrc("custom2mat2.png", raid="custom2"))
custom2mat2Img = resizeImage(custom2mat2Img, 50, 50)
custom2mat2Button = ttk.Button(custom2Tab, image=custom2mat2Img)
custom2mat2Button.grid(column=2,row=1)
custom2mat2CounterLabel = ttk.Label(custom2Tab, textvariable=custom2mat2Count).grid(column=2,row=2)
custom2mat2PercentageLabel = ttk.Label(custom2Tab, textvariable=custom2mat2Percentage).grid(column=2,row=3)
custom2mat2Button.bind('<Button-1>', lambda event: custom2CallBack("mat2"))
custom2mat2Button.bind('<Button-2>', lambda event: custom2TakeBack("mat2"))
custom2mat2Button.bind('<Button-3>', lambda event: custom2TakeBack("mat2"))

# custom2mat3
custom2mat3Img = tk.PhotoImage(file=imgSrc("custom2mat3.png", raid="custom2"))
custom2mat3Img = resizeImage(custom2mat3Img, 50, 50)
custom2mat3Button = ttk.Button(custom2Tab, image=custom2mat3Img)
custom2mat3Button.grid(column=3,row=1)
custom2mat3CounterLabel = ttk.Label(custom2Tab, textvariable=custom2mat3Count).grid(column=3,row=2)
custom2mat3PercentageLabel = ttk.Label(custom2Tab, textvariable=custom2mat3Percentage).grid(column=3,row=3)
custom2mat3Button.bind('<Button-1>', lambda event: custom2CallBack("mat3"))
custom2mat3Button.bind('<Button-2>', lambda event: custom2TakeBack("mat3"))
custom2mat3Button.bind('<Button-3>', lambda event: custom2TakeBack("mat3"))

# custom2mat4
custom2mat4Img = tk.PhotoImage(file=imgSrc("custom2mat4.png", raid="custom2"))
custom2mat4Img = resizeImage(custom2mat4Img, 50, 50)
custom2mat4Button = ttk.Button(custom2Tab, image=custom2mat4Img)
custom2mat4Button.grid(column=4,row=1)
custom2mat4CounterLabel = ttk.Label(custom2Tab, textvariable=custom2mat4Count).grid(column=4,row=2)
custom2mat4PercentageLabel = ttk.Label(custom2Tab, textvariable=custom2mat4Percentage).grid(column=4,row=3)
custom2mat4Button.bind('<Button-1>', lambda event: custom2CallBack("mat4"))
custom2mat4Button.bind('<Button-2>', lambda event: custom2TakeBack("mat4"))
custom2mat4Button.bind('<Button-3>', lambda event: custom2TakeBack("mat4"))

# custom2mat5
custom2mat5Img = tk.PhotoImage(file=imgSrc("custom2mat5.png", raid="custom2"))
custom2mat5Img = resizeImage(custom2mat5Img, 50, 50)
custom2mat5Button = ttk.Button(custom2Tab, image=custom2mat5Img)
custom2mat5Button.grid(column=5,row=1)
custom2mat5CounterLabel = ttk.Label(custom2Tab, textvariable=custom2mat5Count).grid(column=5,row=2)
custom2mat5PercentageLabel = ttk.Label(custom2Tab, textvariable=custom2mat5Percentage).grid(column=5,row=3)
custom2mat5Button.bind('<Button-1>', lambda event: custom2CallBack("mat5"))
custom2mat5Button.bind('<Button-2>', lambda event: custom2TakeBack("mat5"))
custom2mat5Button.bind('<Button-3>', lambda event: custom2TakeBack("mat5"))

# custom2 reset button
custom2resetButton = ttk.Button(custom2Tab, text="Reset", command=lambda:custom2resetCount(), width=12).grid(column=5, row=5)

# custom2 Mat Count
if drop['custom2']['animabefore'] == "" and drop['custom2']['animaafter'] =="":
    custom2SinceLabel = StringVar(value="Mats since:" + "\n" + "0")
elif drop['custom2']['animabefore'] == "":
    custom2SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom2']['animaafter']))))
elif drop['custom2']['animaafter'] == "":
    custom2SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom2']['animabefore']))))
else:
    custom2SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom2']['animabefore'])-int(drop['custom2']['animaafter']))))

def custom2MatsDifference(e):
    if custom2TextAfter.get() == "" and custom2TextBefore.get() == "":
        custom2SinceLabel.set("Mats since:" + "\n" + "0")
    elif custom2TextAfter.get() == "":
        custom2SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom2TextBefore.get()))))
    elif custom2TextBefore.get() == "":
        custom2SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom2TextAfter.get()))))
    else:
        custom2SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom2TextBefore.get()) - int(custom2TextAfter.get()))))

    saveData()

custom2Img = tk.PhotoImage(file=imgSrc("custom2anima.png", raid="custom2"))
custom2Img = resizeImage(custom2Img, 25, 25)
custom2ImgLabel = ttk.Label(custom2Tab, image=custom2Img)
custom2ImgLabel.grid(column=0, row=4, sticky= tk.W)

custom2Text = ttk.Label(custom2Tab, textvariable=custom2SinceLabel, justify="left")
custom2Text.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

custom2TextBefore = ttk.Entry(custom2Tab, width=12, validate='key', validatecommand=(vcmd, '%P'))
custom2TextBefore.grid(column=1, columnspan=2, row=4)
custom2TextBefore.insert(0, drop['custom2']['animabefore'])
custom2TextBefore.bind("<KeyRelease>", custom2MatsDifference)

custom2TextAfter = ttk.Entry(custom2Tab, width=12, validate='key', validatecommand=(vcmd, '%P'))
custom2TextAfter.grid(column=1, columnspan=2, row=5)
custom2TextAfter.insert(0, drop['custom2']['animaafter'])
custom2TextAfter.bind("<KeyRelease>", custom2MatsDifference)

# total custom3 raids
custom3CountImg = tk.PhotoImage(file=imgSrc("custom3count.png", raid="custom3"))
custom3CountImg = resizeImage(custom3CountImg, 50, 50)
custom3CountLabel = ttk.Label(custom3Tab, image=custom3CountImg).grid(column=0,row=1)
custom3CounterLabel = ttk.Label(custom3Tab, textvariable=custom3raidCount).grid(column=0, row=2)

# custom3mat1
custom3mat1Img = tk.PhotoImage(file=imgSrc("custom3mat1.png", raid="custom3"))
custom3mat1Img = resizeImage(custom3mat1Img, 50, 50)
custom3mat1Button = ttk.Button(custom3Tab, image=custom3mat1Img)
custom3mat1Button.grid(column=1,row=1)
custom3mat1CounterLabel = ttk.Label(custom3Tab, textvariable=custom3mat1Count).grid(column=1,row=2)
custom3mat1PercentageLabel = ttk.Label(custom3Tab, textvariable=custom3mat1Percentage).grid(column=1,row=3)
custom3mat1Button.bind('<Button-1>', lambda event: custom3CallBack("mat1"))
custom3mat1Button.bind('<Button-2>', lambda event: custom3TakeBack("mat1"))
custom3mat1Button.bind('<Button-3>', lambda event: custom3TakeBack("mat1"))

# custom3mat2
custom3mat2Img = tk.PhotoImage(file=imgSrc("custom3mat2.png", raid="custom3"))
custom3mat2Img = resizeImage(custom3mat2Img, 50, 50)
custom3mat2Button = ttk.Button(custom3Tab, image=custom3mat2Img)
custom3mat2Button.grid(column=2,row=1)
custom3mat2CounterLabel = ttk.Label(custom3Tab, textvariable=custom3mat2Count).grid(column=2,row=2)
custom3mat2PercentageLabel = ttk.Label(custom3Tab, textvariable=custom3mat2Percentage).grid(column=2,row=3)
custom3mat2Button.bind('<Button-1>', lambda event: custom3CallBack("mat2"))
custom3mat2Button.bind('<Button-2>', lambda event: custom3TakeBack("mat2"))
custom3mat2Button.bind('<Button-3>', lambda event: custom3TakeBack("mat2"))

# custom3mat3
custom3mat3Img = tk.PhotoImage(file=imgSrc("custom3mat3.png", raid="custom3"))
custom3mat3Img = resizeImage(custom3mat3Img, 50, 50)
custom3mat3Button = ttk.Button(custom3Tab, image=custom3mat3Img)
custom3mat3Button.grid(column=3,row=1)
custom3mat3CounterLabel = ttk.Label(custom3Tab, textvariable=custom3mat3Count).grid(column=3,row=2)
custom3mat3PercentageLabel = ttk.Label(custom3Tab, textvariable=custom3mat3Percentage).grid(column=3,row=3)
custom3mat3Button.bind('<Button-1>', lambda event: custom3CallBack("mat3"))
custom3mat3Button.bind('<Button-2>', lambda event: custom3TakeBack("mat3"))
custom3mat3Button.bind('<Button-3>', lambda event: custom3TakeBack("mat3"))

# custom3mat4
custom3mat4Img = tk.PhotoImage(file=imgSrc("custom3mat4.png", raid="custom3"))
custom3mat4Img = resizeImage(custom3mat4Img, 50, 50)
custom3mat4Button = ttk.Button(custom3Tab, image=custom3mat4Img)
custom3mat4Button.grid(column=4,row=1)
custom3mat4CounterLabel = ttk.Label(custom3Tab, textvariable=custom3mat4Count).grid(column=4,row=2)
custom3mat4PercentageLabel = ttk.Label(custom3Tab, textvariable=custom3mat4Percentage).grid(column=4,row=3)
custom3mat4Button.bind('<Button-1>', lambda event: custom3CallBack("mat4"))
custom3mat4Button.bind('<Button-2>', lambda event: custom3TakeBack("mat4"))
custom3mat4Button.bind('<Button-3>', lambda event: custom3TakeBack("mat4"))

# custom3mat5
custom3mat5Img = tk.PhotoImage(file=imgSrc("custom3mat5.png", raid="custom3"))
custom3mat5Img = resizeImage(custom3mat5Img, 50, 50)
custom3mat5Button = ttk.Button(custom3Tab, image=custom3mat5Img)
custom3mat5Button.grid(column=5,row=1)
custom3mat5CounterLabel = ttk.Label(custom3Tab, textvariable=custom3mat5Count).grid(column=5,row=2)
custom3mat5PercentageLabel = ttk.Label(custom3Tab, textvariable=custom3mat5Percentage).grid(column=5,row=3)
custom3mat5Button.bind('<Button-1>', lambda event: custom3CallBack("mat5"))
custom3mat5Button.bind('<Button-2>', lambda event: custom3TakeBack("mat5"))
custom3mat5Button.bind('<Button-3>', lambda event: custom3TakeBack("mat5"))

# custom3 reset button
custom3resetButton = ttk.Button(custom3Tab, text="Reset", command=lambda:custom3resetCount(), width=12).grid(column=5, row=5)

# custom3 Mat Count
if drop['custom3']['animabefore'] == "" and drop['custom3']['animaafter'] =="":
    custom3SinceLabel = StringVar(value="Mats since:" + "\n" + "0")
elif drop['custom3']['animabefore'] == "":
    custom3SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom3']['animaafter']))))
elif drop['custom3']['animaafter'] == "":
    custom3SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom3']['animabefore']))))
else:
    custom3SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom3']['animabefore'])-int(drop['custom3']['animaafter']))))

def custom3MatsDifference(e):
    if custom3TextAfter.get() == "" and custom3TextBefore.get() == "":
        custom3SinceLabel.set("Mats since:" + "\n" + "0")
    elif custom3TextAfter.get() == "":
        custom3SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom3TextBefore.get()))))
    elif custom3TextBefore.get() == "":
        custom3SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom3TextAfter.get()))))
    else:
        custom3SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom3TextBefore.get()) - int(custom3TextAfter.get()))))

    saveData()

custom3Img = tk.PhotoImage(file=imgSrc("custom3anima.png", raid="custom3"))
custom3Img = resizeImage(custom3Img, 25, 25)
custom3ImgLabel = ttk.Label(custom3Tab, image=custom3Img)
custom3ImgLabel.grid(column=0, row=4, sticky= tk.W)

custom3Text = ttk.Label(custom3Tab, textvariable=custom3SinceLabel, justify="left")
custom3Text.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

custom3TextBefore = ttk.Entry(custom3Tab, width=12, validate='key', validatecommand=(vcmd, '%P'))
custom3TextBefore.grid(column=1, columnspan=2, row=4)
custom3TextBefore.insert(0, drop['custom3']['animabefore'])
custom3TextBefore.bind("<KeyRelease>", custom3MatsDifference)

custom3TextAfter = ttk.Entry(custom3Tab, width=12, validate='key', validatecommand=(vcmd, '%P'))
custom3TextAfter.grid(column=1, columnspan=2, row=5)
custom3TextAfter.insert(0, drop['custom3']['animaafter'])
custom3TextAfter.bind("<KeyRelease>", custom3MatsDifference)

# total custom4 raids
custom4CountImg = tk.PhotoImage(file=imgSrc("custom4count.png", raid="custom4"))
custom4CountImg = resizeImage(custom4CountImg, 50, 50)
custom4CountLabel = ttk.Label(custom4Tab, image=custom4CountImg).grid(column=0,row=1)
custom4CounterLabel = ttk.Label(custom4Tab, textvariable=custom4raidCount).grid(column=0, row=2)

# custom4mat1
custom4mat1Img = tk.PhotoImage(file=imgSrc("custom4mat1.png", raid="custom4"))
custom4mat1Img = resizeImage(custom4mat1Img, 50, 50)
custom4mat1Button = ttk.Button(custom4Tab, image=custom4mat1Img)
custom4mat1Button.grid(column=1,row=1)
custom4mat1CounterLabel = ttk.Label(custom4Tab, textvariable=custom4mat1Count).grid(column=1,row=2)
custom4mat1PercentageLabel = ttk.Label(custom4Tab, textvariable=custom4mat1Percentage).grid(column=1,row=3)
custom4mat1Button.bind('<Button-1>', lambda event: custom4CallBack("mat1"))
custom4mat1Button.bind('<Button-2>', lambda event: custom4TakeBack("mat1"))
custom4mat1Button.bind('<Button-3>', lambda event: custom4TakeBack("mat1"))

# custom4mat2
custom4mat2Img = tk.PhotoImage(file=imgSrc("custom4mat2.png", raid="custom4"))
custom4mat2Img = resizeImage(custom4mat2Img, 50, 50)
custom4mat2Button = ttk.Button(custom4Tab, image=custom4mat2Img)
custom4mat2Button.grid(column=2,row=1)
custom4mat2CounterLabel = ttk.Label(custom4Tab, textvariable=custom4mat2Count).grid(column=2,row=2)
custom4mat2PercentageLabel = ttk.Label(custom4Tab, textvariable=custom4mat2Percentage).grid(column=2,row=3)
custom4mat2Button.bind('<Button-1>', lambda event: custom4CallBack("mat2"))
custom4mat2Button.bind('<Button-2>', lambda event: custom4TakeBack("mat2"))
custom4mat2Button.bind('<Button-3>', lambda event: custom4TakeBack("mat2"))

# custom4mat3
custom4mat3Img = tk.PhotoImage(file=imgSrc("custom4mat3.png", raid="custom4"))
custom4mat3Img = resizeImage(custom4mat3Img, 50, 50)
custom4mat3Button = ttk.Button(custom4Tab, image=custom4mat3Img)
custom4mat3Button.grid(column=3,row=1)
custom4mat3CounterLabel = ttk.Label(custom4Tab, textvariable=custom4mat3Count).grid(column=3,row=2)
custom4mat3PercentageLabel = ttk.Label(custom4Tab, textvariable=custom4mat3Percentage).grid(column=3,row=3)
custom4mat3Button.bind('<Button-1>', lambda event: custom4CallBack("mat3"))
custom4mat3Button.bind('<Button-2>', lambda event: custom4TakeBack("mat3"))
custom4mat3Button.bind('<Button-3>', lambda event: custom4TakeBack("mat3"))

# custom4mat4
custom4mat4Img = tk.PhotoImage(file=imgSrc("custom4mat4.png", raid="custom4"))
custom4mat4Img = resizeImage(custom4mat4Img, 50, 50)
custom4mat4Button = ttk.Button(custom4Tab, image=custom4mat4Img)
custom4mat4Button.grid(column=4,row=1)
custom4mat4CounterLabel = ttk.Label(custom4Tab, textvariable=custom4mat4Count).grid(column=4,row=2)
custom4mat4PercentageLabel = ttk.Label(custom4Tab, textvariable=custom4mat4Percentage).grid(column=4,row=3)
custom4mat4Button.bind('<Button-1>', lambda event: custom4CallBack("mat4"))
custom4mat4Button.bind('<Button-2>', lambda event: custom4TakeBack("mat4"))
custom4mat4Button.bind('<Button-3>', lambda event: custom4TakeBack("mat4"))

# custom4mat5
custom4mat5Img = tk.PhotoImage(file=imgSrc("custom4mat5.png", raid="custom4"))
custom4mat5Img = resizeImage(custom4mat5Img, 50, 50)
custom4mat5Button = ttk.Button(custom4Tab, image=custom4mat5Img)
custom4mat5Button.grid(column=5,row=1)
custom4mat5CounterLabel = ttk.Label(custom4Tab, textvariable=custom4mat5Count).grid(column=5,row=2)
custom4mat5PercentageLabel = ttk.Label(custom4Tab, textvariable=custom4mat5Percentage).grid(column=5,row=3)
custom4mat5Button.bind('<Button-1>', lambda event: custom4CallBack("mat5"))
custom4mat5Button.bind('<Button-2>', lambda event: custom4TakeBack("mat5"))
custom4mat5Button.bind('<Button-3>', lambda event: custom4TakeBack("mat5"))

# custom4 reset button
custom4resetButton = ttk.Button(custom4Tab, text="Reset", command=lambda:custom4resetCount(), width=12).grid(column=5, row=5)

# custom4 Mat Count
if drop['custom4']['animabefore'] == "" and drop['custom4']['animaafter'] =="":
    custom4SinceLabel = StringVar(value="Mats since:" + "\n" + "0")
elif drop['custom4']['animabefore'] == "":
    custom4SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom4']['animaafter']))))
elif drop['custom4']['animaafter'] == "":
    custom4SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom4']['animabefore']))))
else:
    custom4SinceLabel = StringVar(value="Mats since:" + "\n" + str(abs(int(drop['custom4']['animabefore'])-int(drop['custom4']['animaafter']))))

def custom4MatsDifference(e):
    if custom4TextAfter.get() == "" and custom4TextBefore.get() == "":
        custom4SinceLabel.set("Mats since:" + "\n" + "0")
    elif custom4TextAfter.get() == "":
        custom4SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom4TextBefore.get()))))
    elif custom4TextBefore.get() == "":
        custom4SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom4TextAfter.get()))))
    else:
        custom4SinceLabel.set("Mats since:" + "\n" + str(abs(int(custom4TextBefore.get()) - int(custom4TextAfter.get()))))

    saveData()

custom4Img = tk.PhotoImage(file=imgSrc("custom4anima.png", raid="custom4"))
custom4Img = resizeImage(custom4Img, 25, 25)
custom4ImgLabel = ttk.Label(custom4Tab, image=custom4Img)
custom4ImgLabel.grid(column=0, row=4, sticky= tk.W)

custom4Text = ttk.Label(custom4Tab, textvariable=custom4SinceLabel, justify="left")
custom4Text.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

custom4TextBefore = ttk.Entry(custom4Tab, width=12, validate='key', validatecommand=(vcmd, '%P'))
custom4TextBefore.grid(column=1, columnspan=2, row=4)
custom4TextBefore.insert(0, drop['custom4']['animabefore'])
custom4TextBefore.bind("<KeyRelease>", custom4MatsDifference)

custom4TextAfter = ttk.Entry(custom4Tab, width=12, validate='key', validatecommand=(vcmd, '%P'))
custom4TextAfter.grid(column=1, columnspan=2, row=5)
custom4TextAfter.insert(0, drop['custom4']['animaafter'])
custom4TextAfter.bind("<KeyRelease>", custom4MatsDifference)

# pbhl reset button
pbhlresetButton = ttk.Button(pbhlTab, text="Reset", command=lambda:pbhlresetCount(), width=12).grid(column=5, row=5)

# akasha reset button
resetButton = ttk.Button(akashaTab, text="Reset", command=lambda:resetCount(), width=12).grid(column=5, row=5)

# gohl reset button
gohlresetButton = ttk.Button(gohlTab, text="Reset", command=lambda:gohlresetCount(), width=12).grid(column=5, row=5)

# pbhl blue chest count/percentage
pbhlblueImg = tk.PhotoImage(file=imgSrc("pbhlBluechest.png", raid="pbhl"))
pbhlblueImg = resizeImage(pbhlblueImg, 25, 25)
pbhlblueLabel = ttk.Label(pbhlTab, image=pbhlblueImg)
pbhlblueLabel.grid(column=0,row=4, sticky= tk.W)

pbhlblueTextLabel = ttk.Label(pbhlTab, textvariable=pbhlblueText, justify="left")
pbhlblueTextLabel.grid(column=0, columnspan=2, row=5, sticky=tk.W)

#pbhlbluePercentLabel = ttk.Label(pbhlTab, textvariable=pbhlbluePercent)
#pbhlbluePercentLabel.grid(column=0, row=5, sticky=tk.NE)

# NEW STUFF

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
pbhlhornImg = tk.PhotoImage(file=imgSrc("pbhlhorn.png", raid="pbhl"))
pbhlhornImg = resizeImage(pbhlhornImg, 25, 25)
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


keyImg = tk.PhotoImage(file=imgSrc("akashaHollowkey.png", raid="akasha"))
keyImg = resizeImage(keyImg, 25, 25)
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


azuriteImg2 = tk.PhotoImage(file=imgSrc("gohlAzurite.png", raid="gohl"))
azuriteImg2 = resizeImage(azuriteImg2, 25, 25)
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

# settings tab
themeString = StringVar(value="Theme")
themeStringLight = StringVar(value="Light Theme")
themeStringDark = StringVar(value="Dark Theme")

settingsThemeTitle = ttk.Label(settingsTab, textvariable=themeString, justify="left")
settingsThemeTitle.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

settingsThemeLightButton = ttk.Button(settingsTab, textvariable=themeStringLight)
settingsThemeLightButton.bind('<Button-1>', lambda event: themeSetting("arc"))
settingsThemeLightButton.grid(column=0, columnspan=2, row=6, sticky= tk.NW)

settingsThemeLightButton = ttk.Button(settingsTab, textvariable=themeStringDark)
settingsThemeLightButton.bind('<Button-1>', lambda event: themeSetting("black"))
settingsThemeLightButton.grid(column=3, columnspan=2, row=6, sticky= tk.NW)

tabControl.select(drop["settings"]["resourceTab"])
if drop["settings"]["resourceTab"] == ".!notebook.!frame":
    tabControlBar.select(drop["settings"]["goldTab"])
elif drop["settings"]["resourceTab"] == ".!notebook.!frame2":
    tabControlSand.select(drop["settings"]["sandTab"])
else:
    tabControlCustom.select(drop["settings"]["customTab"])

root.mainloop()
