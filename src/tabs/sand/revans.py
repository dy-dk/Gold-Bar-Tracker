import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.ttk import Notebook
from tabs.item import ButtonItem, Item
from tabs.raid import Raid
from utils import image_search, resize_image

class Revans(Raid):
    def __init__ (self, parent:Notebook):
        super().__init__(raid_name="revans",parent=parent)
        self.render_frame()
    
    def render_frame(self):
        # total count
        self.total_raid_image = resize_image(img=tk.PhotoImage(file=image_search("revansCount.png", raid=self.raid_name)),
                                             newWidth=50,
                                             newHeight=50)
        self.total_raid_label = ttk.Label(self.frame, image=self.total_raid_image).grid(column=0,row=1)
        self.total_raid_count_label = ttk.Label(self.frame, textvariable=self.total_raid.count).grid(column=0, row=2)

        # trash
        self.trash = ButtonItem(frame=self.frame, 
                          image=tk.PhotoImage(file=image_search("revansLitter.png", raid=self.raid_name)), 
                          name="trash")

        self.trash.button.grid(column=1,row=1)
        self.trash.button.bind('<Button-1>', lambda e : self.add_counter(self.trash))
        self.trash.button.bind('<Button-2>', lambda e : self.subtract_counter(self.trash))
        self.trash.button.bind('<Button-3>', lambda e : self.subtract_counter(self.trash))

        self.trash.count_label.grid(column=1,row=2)
        self.trash.percentage_label.grid(column=1,row=3)

        # weapon
        self.weapon = ButtonItem(frame=self.frame, 
                           image=tk.PhotoImage(file=image_search("revansWeapon.png", raid=self.raid_name)), 
                           name="weapon")

        self.weapon.button.grid(column=2,row=1)
        self.weapon.button.bind('<Button-1>', lambda e : self.add_counter(self.weapon))
        self.weapon.button.bind('<Button-2>', lambda e : self.subtract_counter(self.weapon))
        self.weapon.button.bind('<Button-3>', lambda e : self.subtract_counter(self.weapon))

        self.weapon.count_label.grid(column=2,row=2)
        self.weapon.percentage_label.grid(column=2,row=3)

        # sand
        self.sand = ButtonItem(frame=self.frame, 
                         image=tk.PhotoImage(file=image_search("revansSand.png", raid=self.raid_name)), 
                         name="sand")
        
        self.sand.button.grid(padx= [15,0], column=5,row=1)
        self.sand.button.bind('<Button-1>', lambda e : self.add_counter(self.sand))
        self.sand.button.bind('<Button-2>', lambda e : self.subtract_counter(self.sand))
        self.sand.button.bind('<Button-3>', lambda e : self.subtract_counter(self.sand))
        
        self.sand.count_label.grid(padx= [15,0],column=5,row=2)
        self.sand.percentage_label.grid(padx= [15,0],column=5,row=3)
        
        # add all drop items -> determine which item contribute to total count
        self.add_items(self.trash,self.weapon,self.sand)

        # reset button
        self.reset_button = ttk.Button(self.frame, text="Reset", command=lambda:self.reset_count(), width=12).grid(padx= [45,0], column=6, row=5)

        # anima count
        self.anima_image = resize_image(img=tk.PhotoImage(file=image_search("revansAnima.png", raid=self.raid_name)),
                                        newWidth=25,
                                        newHeight=25)
        self.anima_image_label = ttk.Label(self.frame, image=self.anima_image).grid(column=0, row=4, sticky= tk.W)

        self.anima_before = Item(name="animabefore")
        self.load_data(self.anima_before)

        self.anima_after = Item(name="animaafter")
        self.load_data(self.anima_after)

        self.anima_since_label = StringVar(value=self.get_item_difference_label(self.anima_before.count.get(),self.anima_after.count.get()))     

        self.anima_text = ttk.Label(self.frame, textvariable=self.anima_since_label, justify="left")
        self.anima_text.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

        self.anima_before_input = ttk.Entry(self.frame, width=12, validate='key', validatecommand=(self.validate_command, '%P'))
        self.anima_before_input.grid(column=1, columnspan=2, row=4)
        self.anima_before_input.insert(0,self.anima_before.count.get())
        self.anima_before_input.bind("<KeyRelease>", self.set_item_difference_label)

        self.anima_after_input = ttk.Entry(self.frame, width=12, validate='key', validatecommand=(self.validate_command, '%P'))
        self.anima_after_input.grid(column=1, columnspan=2, row=5)
        self.anima_after_input.insert(0,self.anima_after.count.get())
        self.anima_after_input.bind("<KeyRelease>", self.set_item_difference_label)
    
    def get_item_difference_label(self,before:int, after:int) -> str:
        return f"Mats since:\n{str(abs(int(before) - int(after)))}"

    def set_item_difference_label(self,e):
        self.anima_before.count.set(self.anima_before_input.get() if self.anima_before_input.get().isdigit() else 0)
        self.anima_after.count.set(self.anima_after_input.get() if self.anima_after_input.get().isdigit() else 0)
        self.anima_since_label.set(value=self.get_item_difference_label(self.anima_before.count.get(),self.anima_after.count.get()))     
        self.save_data(self.anima_before,self.anima_after)
        