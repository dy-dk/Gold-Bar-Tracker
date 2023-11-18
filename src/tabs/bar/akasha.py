import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.ttk import Notebook
from tabs.item import ButtonItem, Item 
from tabs.raid import Raid
from utils import image_search, resize_image

class Akasha(Raid):
    def __init__ (self, parent:Notebook):
        super().__init__(raid_name="akasha",parent=parent)
        self.render_frame()
    
    def render_frame(self):
        # total count
        self.total_raid_image = resize_image(img=tk.PhotoImage(file=image_search("akashaBluechest.png", raid=self.raid_name)),
                                             newWidth=50, 
                                             newHeight=50)
        self.total_raid_label = ttk.Label(self.frame, image=self.total_raid_image).grid(column=0,row=1)
        self.total_raid_count_label = ttk.Label(self.frame, textvariable=self.total_raid.count).grid(column=0, row=2)

        # hollow key
        self.hollowkey = ButtonItem(frame=self.frame,
                          image=tk.PhotoImage(file=image_search("akashaLitter.png", raid=self.raid_name)), 
                          name="hollowkey")

        self.hollowkey.button.grid(column=1,row=1)
        self.hollowkey.button.bind('<Button-1>', lambda e : self.add_counter(self.hollowkey))
        self.hollowkey.button.bind('<Button-2>', lambda e : self.subtract_counter(self.hollowkey))
        self.hollowkey.button.bind('<Button-3>', lambda e : self.subtract_counter(self.hollowkey))

        self.hollowkey.count_label.grid(column=1,row=2)
        self.hollowkey.percentage_label.grid(column=1,row=3)

        # corona ring
        self.coronaring = ButtonItem(frame=self.frame, 
                               image=tk.PhotoImage(file=image_search("akashaCoronationring.png", raid=self.raid_name)), 
                               name="coronaring")

        self.coronaring.button.grid(column=2,row=1)
        self.coronaring.button.bind('<Button-1>', lambda e : self.add_counter(self.coronaring))
        self.coronaring.button.bind('<Button-2>', lambda e : self.subtract_counter(self.coronaring))
        self.coronaring.button.bind('<Button-3>', lambda e : self.subtract_counter(self.coronaring))

        self.coronaring.count_label.grid(column=2,row=2)
        self.coronaring.percentage_label.grid(column=2,row=3)

        # lineage ring
        self.lineagering = ButtonItem(frame=self.frame, 
                                image=tk.PhotoImage(file=image_search("akashaLineagering.png", raid=self.raid_name)), 
                                name="lineagering")

        self.lineagering.button.grid(column=3,row=1)
        self.lineagering.button.bind('<Button-1>', lambda e : self.add_counter(self.lineagering))
        self.lineagering.button.bind('<Button-2>', lambda e : self.subtract_counter(self.lineagering))
        self.lineagering.button.bind('<Button-3>', lambda e : self.subtract_counter(self.lineagering))

        self.lineagering.count_label.grid(column=3,row=2)
        self.lineagering.percentage_label.grid(column=3,row=3)

        # intricacy ring        
        self.intricacyring = ButtonItem(frame=self.frame, 
                                  image=tk.PhotoImage(file=image_search("akashaIntricacyring.png", raid=self.raid_name)), 
                                  name="intricacyring")

        self.intricacyring.button.grid(column=4,row=1)
        self.intricacyring.button.bind('<Button-1>', lambda e : self.add_counter(self.intricacyring))
        self.intricacyring.button.bind('<Button-2>', lambda e : self.subtract_counter(self.intricacyring))
        self.intricacyring.button.bind('<Button-3>', lambda e : self.subtract_counter(self.intricacyring))

        self.intricacyring.count_label.grid(column=4,row=2)
        self.intricacyring.percentage_label.grid(column=4,row=3)

        # gold bar
        self.goldbar = ButtonItem(frame=self.frame, 
                            image=tk.PhotoImage(file=image_search("akashaGoldbar.png", raid=self.raid_name)), 
                            name="goldbar")
        
        self.goldbar.button.grid(column=5,row=1)
        self.goldbar.button.bind('<Button-1>', lambda e : self.add_counter(self.goldbar))
        self.goldbar.button.bind('<Button-2>', lambda e : self.subtract_counter(self.goldbar))
        self.goldbar.button.bind('<Button-3>', lambda e : self.subtract_counter(self.goldbar))
        
        self.goldbar.count_label.grid(column=5,row=2)
        self.goldbar.percentage_label.grid(column=5,row=3)
        
        # add all drop items -> determine which item contribute to total count
        self.add_items(self.hollowkey,self.coronaring,self.lineagering,self.intricacyring,self.goldbar)

        # reset button
        self.reset_button = ttk.Button(self.frame, text="Reset", command=lambda:self.reset_count(), width=12).grid(column=5, row=5)

        # key count
        self.key_image = resize_image(img=tk.PhotoImage(file=image_search("akashaHollowKey.png", raid=self.raid_name)),
                               newWidth=25,
                               newHeight=25)
        self.key_image_label = ttk.Label(self.frame,image=self.key_image).grid(column=0, row=4, sticky= tk.W)

        self.key_before = Item(name="keybefore")
        self.load_data(self.key_before)

        self.key_after = Item(name="keyafter")
        self.load_data(self.key_after)

        self.key_since_label = StringVar(value=self.get_item_difference_label(self.key_before.count.get(),self.key_after.count.get()))     

        self.key_text = ttk.Label(self.frame, textvariable=self.key_since_label, justify="left")
        self.key_text.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

        self.key_before_input = ttk.Entry(self.frame, width=12, validate='key', validatecommand=(self.validate_command, '%P'))
        self.key_before_input.grid(column=1, columnspan=2, row=4)
        self.key_before_input.insert(0,self.key_before.count.get())
        self.key_before_input.bind("<KeyRelease>", self.set_item_difference_label)

        self.key_after_input = ttk.Entry(self.frame, width=12, validate='key', validatecommand=(self.validate_command, '%P'))
        self.key_after_input.grid(column=1, columnspan=2, row=5)
        self.key_after_input.insert(0,self.key_after.count.get())
        self.key_after_input.bind("<KeyRelease>", self.set_item_difference_label)
    
    def get_item_difference_label(self,before:int, after:int) -> str:
        return f"Keys since:\n{str(abs(int(before) - int(after)))}"

    def set_item_difference_label(self,e):
        self.key_before.count.set(self.key_before_input.get() if self.key_before_input.get().isdigit() else 0)
        self.key_after.count.set(self.key_after_input.get() if self.key_after_input.get().isdigit() else 0)
        self.key_since_label.set(value=self.get_item_difference_label(self.key_before.count.get(),self.key_after.count.get()))
        self.save_data(self.key_before,self.key_after)
        