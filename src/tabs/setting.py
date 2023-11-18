from tkinter import StringVar, ttk
import tkinter as tk
from ttkthemes import ThemedStyle
import dataconn as dc

class Setting():
    def __init__ (self, frame:ttk.Frame, style:ThemedStyle):
        self.frame = frame
        self.style = style
        
        self.theme = StringVar(value=dc.get_setting("theme","black"))

        self.render_frame()

    def render_frame(self):
        self.settingsThemeString = StringVar(value="Change Theme")
        self.settingsThemeStringDark = StringVar(value="Swap to Light Theme")
        self.settingsThemeStringLight = StringVar(value="Swap to Dark Theme")
        
        self.settingsThemeTitle = ttk.Label(self.frame, textvariable=self.settingsThemeString, justify="left")
        self.settingsThemeTitle.grid(column=0, columnspan=2, row=5, sticky= tk.NW)
        
        self.settingsThemeToggleButton = ttk.Button(self.frame)
        if self.theme.get() == "black":
            self.settingsThemeToggleButton.configure(textvariable=self.settingsThemeStringDark)
        elif self.theme.get() == "arc":
            self.settingsThemeToggleButton.configure(textvariable=self.settingsThemeStringLight)
        self.settingsThemeToggleButton.bind('<Button-1>', lambda event: self.themeToggle(self.theme.get()))
        self.settingsThemeToggleButton.grid(column=0, columnspan=2, row=6, sticky= tk.NW)
        
        self.themeToggle(self.theme)

    def themeToggle(self,currentTheme):
        match currentTheme:
            case "black":
                self.themeSetting("arc")
                self.settingsThemeToggleButton.configure(textvariable=self.settingsThemeStringLight)
            case "clearlook":
                self.themeSetting("black")
                self.settingsThemeToggleButton.configure(textvariable=self.settingsThemeStringDark)
            case _:
                self.themeSetting("black")
                self.settingsThemeToggleButton.configure(textvariable=self.settingsThemeStringDark)
    
    def themeSetting(self,themeColor):
        self.theme.set(themeColor)
        self.style.set_theme(self.theme.get())
        dc.save_setting("theme",themeColor)