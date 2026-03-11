from tkinter import *

class Main_frame:
    def __init__(self):
        self.frame_tool = Frame()
        self.frame_tool.pack(side='right', padx=7)

        # Crop input Frame
        self.frame_ci = Frame(self.frame_tool)
        self.frame_ci.pack()

        # Crop button frame
        self.frame_cb = Frame(self.frame_tool)
        self.frame_cb.pack()

        # Weight and Height Frame
        self.frame_wh = Frame(self.frame_tool)
        self.frame_wh.pack()

        self.frame_button = Frame(self.frame_tool)
        self.frame_button.pack()