import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.ttk import Notebook
from tabs.item import ButtonItem, Item
from tabs.raid import Raid
from utils import image_search, resize_image

class GOHL(Raid):
    def __init__ (self, parent:Notebook):
        super().__init__(raid_name="gohl",parent=parent)
        self.render_frame()
    
    def render_frame(self):
        # total count
        self.total_raid_image = resize_image(img=tk.PhotoImage(file=image_search("gohlBluechest.png", raid=self.raid_name)),
                                             newWidth=50, 
                                             newHeight=50)
        self.total_raid_label = ttk.Label(self.frame, image=self.total_raid_image).grid(column=0,row=1)
        self.total_raid_count_label = ttk.Label(self.frame, textvariable=self.total_raid.count).grid(column=0, row=2)

        # azurite
        self.azurite = ButtonItem(frame=self.frame,
                          image=tk.PhotoImage(file=image_search("gohlLitter.png", raid=self.raid_name)), 
                          name="azurite")

        self.azurite.button.grid(column=1,row=1)
        self.azurite.button.bind('<Button-1>', lambda e : self.add_counter(self.azurite))
        self.azurite.button.bind('<Button-2>', lambda e : self.subtract_counter(self.azurite))
        self.azurite.button.bind('<Button-3>', lambda e : self.subtract_counter(self.azurite))

        self.azurite.count_label.grid(column=1,row=2)
        self.azurite.percentage_label.grid(column=1,row=3)

        # corona ring
        self.coronaring = ButtonItem(frame=self.frame, 
                               image=tk.PhotoImage(file=image_search("gohlCoronationring.png", raid=self.raid_name)), 
                               name="coronaring")

        self.coronaring.button.grid(column=2,row=1)
        self.coronaring.button.bind('<Button-1>', lambda e : self.add_counter(self.coronaring))
        self.coronaring.button.bind('<Button-2>', lambda e : self.subtract_counter(self.coronaring))
        self.coronaring.button.bind('<Button-3>', lambda e : self.subtract_counter(self.coronaring))

        self.coronaring.count_label.grid(column=2,row=2)
        self.coronaring.percentage_label.grid(column=2,row=3)

        # lineage ring
        self.lineagering = ButtonItem(frame=self.frame, 
                                image=tk.PhotoImage(file=image_search("gohlLineagering.png", raid=self.raid_name)), 
                                name="lineagering")

        self.lineagering.button.grid(column=3,row=1)
        self.lineagering.button.bind('<Button-1>', lambda e : self.add_counter(self.lineagering))
        self.lineagering.button.bind('<Button-2>', lambda e : self.subtract_counter(self.lineagering))
        self.lineagering.button.bind('<Button-3>', lambda e : self.subtract_counter(self.lineagering))

        self.lineagering.count_label.grid(column=3,row=2)
        self.lineagering.percentage_label.grid(column=3,row=3)

        # intricacy ring        
        self.intricacyring = ButtonItem(frame=self.frame, 
                                  image=tk.PhotoImage(file=image_search("gohlIntricacyring.png", raid=self.raid_name)), 
                                  name="intricacyring")

        self.intricacyring.button.grid(column=4,row=1)
        self.intricacyring.button.bind('<Button-1>', lambda e : self.add_counter(self.intricacyring))
        self.intricacyring.button.bind('<Button-2>', lambda e : self.subtract_counter(self.intricacyring))
        self.intricacyring.button.bind('<Button-3>', lambda e : self.subtract_counter(self.intricacyring))

        self.intricacyring.count_label.grid(column=4,row=2)
        self.intricacyring.percentage_label.grid(column=4,row=3)

        # gold bar
        self.goldbar = ButtonItem(frame=self.frame, 
                            image=tk.PhotoImage(file=image_search("gohlGoldbar.png", raid=self.raid_name)), 
                            name="goldbar")
        
        self.goldbar.button.grid(column=5,row=1)
        self.goldbar.button.bind('<Button-1>', lambda e : self.add_counter(self.goldbar))
        self.goldbar.button.bind('<Button-2>', lambda e : self.subtract_counter(self.goldbar))
        self.goldbar.button.bind('<Button-3>', lambda e : self.subtract_counter(self.goldbar))
        
        self.goldbar.count_label.grid(column=5,row=2)
        self.goldbar.percentage_label.grid(column=5,row=3)
        
        # add all drop items -> determine which item contribute to total count
        self.add_items(self.azurite,self.coronaring,self.lineagering,self.intricacyring,self.goldbar)

        # reset button
        self.reset_button = ttk.Button(self.frame, text="Reset", command=lambda:self.reset_count(), width=12).grid(column=5, row=5)

        # azurite count
        self.azurite_image = resize_image(img=tk.PhotoImage(file=image_search("gohlAzurite.png", raid=self.raid_name)),
                               newWidth=25,
                               newHeight=25)
        self.azurite_image_label = ttk.Label(self.frame,image=self.azurite_image).grid(column=0, row=4, sticky= tk.W)

        self.azurite_before = Item(name="azuritebefore")
        self.load_data(self.azurite_before)

        self.azurite_after = Item(name="azuriteafter")
        self.load_data(self.azurite_after)

        self.azurite_since_label = StringVar(value=self.get_item_difference_label(self.azurite_before.count.get(),self.azurite_after.count.get()))     

        self.azurite_text = ttk.Label(self.frame, textvariable=self.azurite_since_label, justify="left")
        self.azurite_text.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

        self.azurite_before_input = ttk.Entry(self.frame, width=12, validate='key', validatecommand=(self.validate_command, '%P'))
        self.azurite_before_input.grid(column=1, columnspan=2, row=4)
        self.azurite_before_input.insert(0,self.azurite_before.count.get())
        self.azurite_before_input.bind("<KeyRelease>", self.set_item_difference_label)

        self.azurite_after_input = ttk.Entry(self.frame, width=12, validate='key', validatecommand=(self.validate_command, '%P'))
        self.azurite_after_input.grid(column=1, columnspan=2, row=5)        
        self.azurite_after_input.insert(0,self.azurite_after.count.get())
        self.azurite_after_input.bind("<KeyRelease>", self.set_item_difference_label)
    
    def get_item_difference_label(self,before:int, after:int) -> str:
        return f"Azurite since:\n{str(abs(int(before) - int(after)))}"

    def set_item_difference_label(self,e):
        self.azurite_before.count.set(self.azurite_before_input.get() if self.azurite_before_input.get().isdigit() else 0)
        self.azurite_after.count.set(self.azurite_after_input.get() if self.azurite_after_input.get().isdigit() else 0)
        self.azurite_since_label.set(value=self.get_item_difference_label(self.azurite_before.count.get(),self.azurite_after.count.get()))
        self.save_data(self.azurite_before,self.azurite_after)
        