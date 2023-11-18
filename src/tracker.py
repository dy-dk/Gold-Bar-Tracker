import dataconn as dc
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage, ttk
from ttkthemes import ThemedStyle
from tabs.bar.akasha import Akasha
from tabs.bar.gohl import GOHL
from tabs.bar.pbhl import PBHL
from tabs.customs.custom import Custom
from tabs.sand.dragon import Dragon
from tabs.sand.revans import Revans
from tabs.sand.subhl import SUBHL
from tabs.setting import Setting
from utils import image_search


class Tracker():
    def __init__(self,root:tk.Tk):
        self.root = root
        self.root.title("Drop Tracker")
        self.root.iconphoto(True, PhotoImage(file=image_search("peek.png")))
        self.root.attributes('-topmost', True)
        
        self.style = ThemedStyle(root)
        self.render_component()
    
    def render_component(self):
        self.root_base = ttk.Notebook(root)

        # goldbar tab
        self.goldbar_tab = ttk.Frame(self.root_base)
        self.goldbar_tab_image = ImageTk.PhotoImage((Image.open(image_search("goldbar.png"))).resize((20,20),Image.LANCZOS))
        self.root_base.add(self.goldbar_tab, text="Gold Bar", image=self.goldbar_tab_image, compound="left")
        self.goldbar_tab_base = ttk.Notebook(self.goldbar_tab)

        ## pbhl
        self.pbhl_tab = PBHL(self.goldbar_tab_base)
        self.goldbar_tab_base.add(self.pbhl_tab.frame, text='PBHL')

        ## akasha
        self.akasha_tab = Akasha(self.goldbar_tab_base)
        self.goldbar_tab_base.add(self.akasha_tab.frame, text='Akasha')
        
        ## gohl
        self.gohl_tab = GOHL(self.goldbar_tab_base)
        self.goldbar_tab_base.add(self.gohl_tab.frame, text='GOHL')
        
        self.goldbar_tab_base.pack(expand=1, fill="both")

        # sand tab
        self.sand_tab = ttk.Frame(self.root_base)
        self.sand_tab_image = ImageTk.PhotoImage((Image.open(image_search("eternitysand.png"))).resize((20,20),Image.LANCZOS))
        self.root_base.add(self.sand_tab, text='Eternity Sand', image=self.sand_tab_image, compound="left")
        self.sand_tab_base = ttk.Notebook(self.sand_tab)

        ## dragon
        self.dragon_tab = Dragon(self.sand_tab_base)
        self.sand_tab_base.add(self.dragon_tab.frame, text='Dragons')

        ## revans
        self.revans_tab = Revans(self.sand_tab_base)
        self.sand_tab_base.add(self.revans_tab.frame, text='Revans')

        ## subhl 
        self.subhl_tab = SUBHL(self.sand_tab_base)
        self.sand_tab_base.add(self.subhl_tab.frame, text='SUBHL')

        self.sand_tab_base.pack(expand=1, fill="both")

        # custom tab
        self.custom_tab = ttk.Frame(self.root_base)
        self.custom_tab_image = ImageTk.PhotoImage((Image.open(image_search("custom.png"))).resize((20,20),Image.LANCZOS))
        self.root_base.add(self.custom_tab, text='Custom', image=self.custom_tab_image, compound="left")
        self.custom_tab_base = ttk.Notebook(self.custom_tab)

        for i in range(4):
            self.custom_i_tab = Custom(f"custom{i+1}", self.custom_tab_base)
            self.custom_tab_base.add(self.custom_i_tab.frame, text=f"Custom {i+1}")

        self.custom_tab_base.pack(expand=1, fill="both")

        # setting tab
        self.setting_tab = Setting(ttk.Frame(self.root_base), self.style)
        self.setting_tab_image = ImageTk.PhotoImage((Image.open(image_search("custom.png"))).resize((20,20),Image.LANCZOS))
        self.root_base.add(self.setting_tab.frame, text='Settings', image=self.setting_tab_image, compound="left")

        self.root_base.pack(expand=1, fill="both")  
        
        self.goldbar_tab_base.bind('<<NotebookTabChanged>>', lambda e: dc.save_active_tab("goldbar_tab",self.goldbar_tab_base.select()))        
        self.sand_tab_base.bind('<<NotebookTabChanged>>', lambda e: dc.save_active_tab("sand_tab",self.sand_tab_base.select()))        
        self.custom_tab_base.bind('<<NotebookTabChanged>>', lambda e: dc.save_active_tab("custom_tab",self.custom_tab_base.select()))
        self.root_base.bind('<<NotebookTabChanged>>', lambda e: dc.save_active_tab("resource_tab",self.root_base.select()))        
        self.set_active_tab()
        
    def set_active_tab(self):        
        if(dc.get_active_tab("resource_tab") is None or dc.get_active_tab("resource_tab") == ""):
            return
        
        self.root_base.select(dc.get_active_tab("resource_tab"))
        self.tab_name = self.root_base.tab(dc.get_active_tab("resource_tab"),"text")
        match self.tab_name:
            case "Gold Bar":                
                self.goldbar_tab_base.select(dc.get_active_tab("goldbar_tab") )
            case "Eternity Sand":
                self.sand_tab_base.select(dc.get_active_tab("sand_tab"))
            case "Custom":
                self.custom_tab_base.select(dc.get_active_tab("custom_tab"))
            case _:
                return

if __name__ == "__main__":
    root = tk.Tk()
    app = Tracker(root)
    root.mainloop()