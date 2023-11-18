import tkinter as tk
from tkinter import IntVar, StringVar, ttk

from utils import resize_image

class Item():
    def __init__ (self,name:str,count:int=0 ):        
        self.name = name
        self.count:IntVar = IntVar(value=count)        
        self.count_percentage:StringVar = StringVar(value="0.0%")

    def set_total_count(self, total:int) -> None:
        self.count_percentage.set(self.__get_percentage_label(total_count=total,count=self.count.get()))

    def __get_percentage_label(self,total_count:int,count:int) -> str :
        return f"{round((total_count and count/total_count)*100,2)}%"
    
    def add_count(self) -> None:
        self.count.set(value=self.count.get()+1)

    def subtract_count(self) -> bool:
        if self.count.get() > 0:
            self.count.set(value=self.count.get()-1); 
            return True
        else:
            return False

class ButtonItem(Item):
    def __init__ (self, frame: ttk.Frame, name:str, image:tk.PhotoImage=None, count:int=0 ):
        super().__init__(name,count)
        self.frame = frame

        self.image = image
        if(image is not None):
            self.image:tk.PhotoImage = resize_image(image, 50, 50) 
   
        self.count_label = ttk.Label(self.frame, textvariable=self.count)
        self.percentage_label = ttk.Label(self.frame, textvariable=self.count_percentage)        
        self.button = ttk.Button(self.frame, image=self.image)    