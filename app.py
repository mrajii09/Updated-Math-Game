# Author: Miraj
# Description: Math game framework
# Formula sheet included
import customtkinter as ctk
import tkinter as tk
import random
from logic import *
from windows import *
from windows import windows
from PIL import Image
ctk.set_appearance_mode("Light")

class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Miraj Math")
        self.geometry("1366×768")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.maxsize(800, 600)
        self.minsize(400, 200)
        self.resizable(width = True, height = True)
        self.configure(fg_color="#F5F7FA")
        # Create frame to hold buttons. This will be very useful
        # When switching screens
        self.firstWindow()


    def firstWindow(self):

        # Box to hold label
        box = ctk.CTkFrame(self, fg_color = "#2C3E50", width = 400, height = 100, corner_radius = 30)
        box.grid(row = 0, column = 0, padx=40, pady=(40, 20), sticky = "n")
        # Frame to hold label
        labelFrame = ctk.CTkFrame(box, fg_color = "#E3F2FD", corner_radius = 20)
        labelFrame.grid(row = 0, column = 0, padx=20, pady=20)
        # Label
        label = ctk.CTkLabel(labelFrame,
                             text = "Miraj's Math Game!",
                             font = ("Helvetica Neue", 32, "bold"),
                             text_color="#2C3E50")
        label.pack(padx=20,pady=20)

        # Create frame to hold buttons. This will be very useful
        # When switching screens
        frame = ctk.CTkFrame(self, fg_color="#4A90E2", corner_radius = 15)
        frame.grid(row=1, column=0, padx=20, pady=20)
        # button_callback
        def button_callback():
            frame.grid_forget()
            box.grid_forget()
            labelFrame.grid_forget()
            label.pack_forget()
            self.windows = windows(self)
            self.windows.GameWindow()
        
        #Formula button callback
        def formulas():
            frame.grid_forget()
            box.grid_forget()
            labelFrame.grid_forget()
            label.pack_forget()
            self.windows = windows(self)
            self.windows.formulaWindow()
        
        #Settings button callback
        def settings():
            frame.grid_forget()
            box.grid_forget()
            labelFrame.grid_forget()
            label.pack_forget()
            self.windows = windows(self)
            self.windows.settingsWindow()

        # make a button
        # grid geometry manager is used to set the position
        # and padding of the widget
        # Start button, will switch frames when clicked
        startButton = ctk.CTkButton(frame, #Window it is placed in
                                    text = "Start Game", # Text
                                    width = 200,
                                    height = 100,
                                    font = ("Helvetica Neue", 24, "bold"),
                                    fg_color="Green",
                                    command=button_callback) #when
        startButton.grid(row=1, column=0, padx=10, pady=10)

        # End button, will close the app when clicked
        endButton = ctk.CTkButton(frame, #Window it is placed in
                                text = "End Game", # Text
                                width = 200,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                fg_color="Red",
                                command=exit) #when
        endButton.grid(row=2, column=1, padx=10, pady=10)
        # Formula button
        formulaButton = ctk.CTkButton(frame,
                                    text = "Formulas",
                                    width = 200,
                                    height = 100,
                                    font = ("Helvetica Neue", 24, "bold"),
                                    fg_color="Blue",
                                    command=formulas)
        formulaButton.grid(row=1, column=1, padx=10, pady=10)

        # Settings button
        settingsButton = ctk.CTkButton(frame,
                                      text = "Settings",
                                      width = 200,
                                      height = 100,
                                      font = ("Helvetica Neue", 24, "bold"),
                                      fg_color="Black",
                                      command=settings)
        settingsButton.grid(row=2, column=0, padx=10, pady=10)