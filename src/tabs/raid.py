import dataconn as dc
import tkinter as tk
from tkinter import IntVar, ttk, messagebox
from tkinter.ttk import Notebook
from tabs.item import Item

class Raid:
    def __init__(self,raid_name:str,parent:Notebook):
        self.raid_name = raid_name
        self.notebook = parent
        self.frame = ttk.Frame(self.notebook)        
        self.drops = []
        
        self.validate_command = self.frame.register(self.validate_number_input)

        self.total_raid = Item("raid")
        self.total_raid.count = IntVar(value=int(dc.get_data(self.raid_name,"raid")))

    def load_data(self, item:Item):
        try:
            value = int(dc.get_data(self.raid_name,item.name))
        except ValueError:
            if(dc.get_data(self.raid_name,item.name) == ""):
                value = 0
            
        item.count.set(value=value)

    def save_data(self, *item:Item):
        dc.save_data(self.raid_name,*item)

    def add_counter(self,item:Item,callback=None) -> None:        
        self.total_raid.count.set(self.total_raid.count.get()+1)    # probably better to get from total item than seperate counter
        item.add_count()

        for i in self.drops:
            i.set_total_count(self.total_raid.count.get())

        self.save_data(item,self.total_raid)

        if(callback is not None):
            callback()
    
    def subtract_counter(self,item:Item,callback=None) -> None:
        is_subtracted = item.subtract_count()

        if(is_subtracted):           
            self.total_raid.count.set(self.total_raid.count.get()-1)

        for i in self.drops:
            i.set_total_count(self.total_raid.count.get())
        
        self.save_data(item,self.total_raid)

        if(callback is not None):
            callback()
            
    def add_items(self,*items:Item)-> None:
        for item in items:
            self.load_data(item)            
            item.set_total_count(self.total_raid.count.get())
            self.drops.append(item)
            
    def reset_count(self,callback=None)->None:
        messageboxChoice = messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

        if messageboxChoice == 'yes':
            self.total_raid.count.set(0)
            for item in self.drops:
                item.count.set(0)
                item.set_total_count(0)
        else:
            return
        
        self.save_data(*self.drops,self.total_raid)

        if(callable is not None):
            callback()

    def validate_number_input(self, input:str)-> bool:
        if input.isdigit():
            return True
        elif input == "":
            return True
        else:
            return False