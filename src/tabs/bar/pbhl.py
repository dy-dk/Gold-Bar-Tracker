import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.ttk import Notebook
from tabs.item import ButtonItem, Item
from tabs.raid import Raid
from utils import image_search, resize_image

class PBHL(Raid):
    def __init__ (self, parent:Notebook):
        super().__init__(raid_name="pbhl",parent=parent)
        self.render_frame()
    
    def render_frame(self):
        # total count
        self.total_raid_image = resize_image(img=tk.PhotoImage(file=image_search("pbhlCount.png", raid=self.raid_name)),
                                             newWidth=50, 
                                             newHeight=50)
        self.total_raid_label = ttk.Label(self.frame, image=self.total_raid_image).grid(column=0,row=1)
        self.total_raid_count_label = ttk.Label(self.frame, textvariable=self.total_raid.count).grid(column=0, row=2)

        # no blue chest
        self.nobluechest = ButtonItem(frame=self.frame,
                          image=tk.PhotoImage(file=image_search("pbhlNobluechest.png", raid=self.raid_name)), 
                          name="noblue")

        self.nobluechest.button.grid(column=1,row=1)
        self.nobluechest.button.bind('<Button-1>', lambda e : self.add_counter(self.nobluechest,callback=self.update_bluechest))
        self.nobluechest.button.bind('<Button-2>', lambda e : self.subtract_counter(self.nobluechest,callback=self.update_bluechest))
        self.nobluechest.button.bind('<Button-3>', lambda e : self.subtract_counter(self.nobluechest,callback=self.update_bluechest))

        self.nobluechest.count_label.grid(column=1,row=2)

        # corona ring
        self.coronaring = ButtonItem(frame=self.frame, 
                               image=tk.PhotoImage(file=image_search("pbhlCoronationring.png", raid=self.raid_name)), 
                               name="coronaring")

        self.coronaring.button.grid(column=2,row=1)
        self.coronaring.button.bind('<Button-1>', lambda e : self.add_counter(self.coronaring,callback=self.add_bluechest_count))
        self.coronaring.button.bind('<Button-2>', lambda e : self.subtract_counter(self.coronaring,callback=self.subtract_bluechest_count))
        self.coronaring.button.bind('<Button-3>', lambda e : self.subtract_counter(self.coronaring,callback=self.subtract_bluechest_count))

        self.coronaring.count_label.grid(column=2,row=2)
        self.coronaring.percentage_label.grid(column=2,row=3)

        # lineage ring
        self.lineagering = ButtonItem(frame=self.frame, 
                                image=tk.PhotoImage(file=image_search("pbhlLineagering.png", raid=self.raid_name)), 
                                name="lineagering")

        self.lineagering.button.grid(column=3,row=1)
        self.lineagering.button.bind('<Button-1>', lambda e : self.add_counter(self.lineagering,callback=self.add_bluechest_count))
        self.lineagering.button.bind('<Button-2>', lambda e : self.subtract_counter(self.lineagering,callback=self.subtract_bluechest_count))
        self.lineagering.button.bind('<Button-3>', lambda e : self.subtract_counter(self.lineagering,callback=self.subtract_bluechest_count))

        self.lineagering.count_label.grid(column=3,row=2)
        self.lineagering.percentage_label.grid(column=3,row=3)

        # intricacy ring        
        self.intricacyring = ButtonItem(frame=self.frame, 
                                  image=tk.PhotoImage(file=image_search("pbhlIntricacyring.png", raid=self.raid_name)), 
                                  name="intricacyring")

        self.intricacyring.button.grid(column=4,row=1)
        self.intricacyring.button.bind('<Button-1>', lambda e : self.add_counter(self.intricacyring,callback=self.add_bluechest_count))
        self.intricacyring.button.bind('<Button-2>', lambda e : self.subtract_counter(self.intricacyring,callback=self.subtract_bluechest_count))
        self.intricacyring.button.bind('<Button-3>', lambda e : self.subtract_counter(self.intricacyring,callback=self.subtract_bluechest_count))

        self.intricacyring.count_label.grid(column=4,row=2)
        self.intricacyring.percentage_label.grid(column=4,row=3)

        # gold bar
        self.goldbar = ButtonItem(frame=self.frame, 
                            image=tk.PhotoImage(file=image_search("pbhlGoldbar.png", raid=self.raid_name)), 
                            name="goldbar")
        
        self.goldbar.button.grid(column=5,row=1)
        self.goldbar.button.bind('<Button-1>', lambda e : self.add_counter(self.goldbar,callback=self.add_bluechest_count))
        self.goldbar.button.bind('<Button-2>', lambda e : self.subtract_counter(self.goldbar,callback=self.subtract_bluechest_count))
        self.goldbar.button.bind('<Button-3>', lambda e : self.subtract_counter(self.goldbar,callback=self.subtract_bluechest_count))
        
        self.goldbar.count_label.grid(column=5,row=2)
        self.goldbar.percentage_label.grid(column=5,row=3)
        
        # add all drop items -> determine which item contribute to total count
        self.add_items(self.nobluechest,self.coronaring,self.lineagering,self.intricacyring,self.goldbar)

        # reset button
        self.reset_button = ttk.Button(self.frame, text="Reset", command=lambda:self.reset_count(callback=self.reset_bluechest_count), width=12).grid(column=5, row=5)

        # pbhl blue chest count/percentage
        self.bluechest = Item(name="bluechest")
        self.bluechest.count.set(value=self.total_raid.count.get()-self.nobluechest.count.get())  

        self.bluechest_image = resize_image(img=tk.PhotoImage(file=image_search("pbhlBluechest.png", raid=self.raid_name)),
                                            newWidth=25,
                                            newHeight=25)      
        self.bluechest_image_label = ttk.Label(self.frame, 
                                               image=self.bluechest_image).grid(column=0,row=4, sticky= tk.W)        
        self.bluechest_droprate_text = StringVar(value=self.get_bluechest_droprate_text())
        self.bluechest_label = ttk.Label(self.frame, 
                                         textvariable=self.bluechest_droprate_text, 
                                         justify="left").grid(column=0, columnspan=2, row=5, sticky=tk.W)
        self.update_bluechest()

        # horn count
        self.horn_image = resize_image(img=tk.PhotoImage(file=image_search("pbhlhorn.png", raid=self.raid_name)),
                               newWidth=25,
                               newHeight=25)
        self.horn_image_label = ttk.Label(self.frame,image=self.horn_image).grid(column=2, row=4, sticky= tk.W)

        self.horn_before = Item(name="hornbefore")
        self.load_data(self.horn_before)

        self.horn_after = Item(name="hornafter")
        self.load_data(self.horn_after)

        self.horn_since_label = StringVar(value=self.get_item_difference_label(self.horn_before.count.get(),self.horn_after.count.get()))     

        self.horn_text = ttk.Label(self.frame, textvariable=self.horn_since_label, justify="left")
        self.horn_text.grid(column=2, columnspan=2, row=5, sticky= tk.NW)

        self.horn_before_input = ttk.Entry(self.frame, width=15, validate='key', validatecommand=(self.validate_command, '%P'))
        self.horn_before_input.grid(column=3, columnspan=2, row=4)
        self.horn_before_input.insert(0,self.horn_before.count.get())
        self.horn_before_input.bind("<KeyRelease>", self.set_item_difference_label)

        self.horn_after_input = ttk.Entry(self.frame, width=15, validate='key', validatecommand=(self.validate_command, '%P'))
        self.horn_after_input.grid(column=3, columnspan=2, row=5)
        self.horn_after_input.insert(0,self.horn_after.count.get())
        self.horn_after_input.bind("<KeyRelease>", self.set_item_difference_label)
    
    def get_item_difference_label(self,before:int, after:int) -> str:
        return f"Horns since:\n{str(abs(int(before) - int(after)))}"

    def set_item_difference_label(self,e):        
        self.horn_before.count.set(self.horn_before_input.get() if self.horn_before_input.get().isdigit() else 0)
        self.horn_after.count.set(self.horn_after_input.get() if self.horn_after_input.get().isdigit() else 0)
        self.horn_since_label.set(value=self.get_item_difference_label(self.horn_before.count.get(),self.horn_after.count.get()))
        self.save_data(self.horn_before,self.horn_after)

    def get_bluechest_droprate_text(self):
        return f"Total: {self.bluechest.count.get()}\nDrop Rate: {self.bluechest.count_percentage.get()}"  
    
    def update_bluechest(self):        
        self.bluechest.set_total_count(self.total_raid.count.get())
        self.bluechest_droprate_text.set(value=self.get_bluechest_droprate_text())

        for i in self.drops:
            i.set_total_count(self.bluechest.count.get())

    def add_bluechest_count(self):
        self.bluechest.add_count()
        self.update_bluechest()
    
    def subtract_bluechest_count(self):
        self.bluechest.subtract_count()
        self.update_bluechest()  
    
    def reset_bluechest_count(self):
        self.bluechest.count.set(0)
        self.update_bluechest()
        
        