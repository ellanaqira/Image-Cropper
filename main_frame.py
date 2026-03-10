from tkinter import *

class Main_frame:
    def __init__(self):
        self.frame_tool = Frame()
        self.frame_tool.pack(side='right')

        self.frame_wh = Frame(self.frame_tool)
        self.frame_wh.pack()

        self.frame_button = Frame(self.frame_tool)
        self.frame_button.pack()