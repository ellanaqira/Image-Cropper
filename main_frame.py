from tkinter import *

class Main_frame:
    def __init__(self):
        self.frame_tool = Frame()
        self.frame_tool.pack(side='right')

        # Separator frame1
        self.frame_separator1 = Frame(self.frame_tool)
        self.frame_separator1.pack()

        # Weight and Height Frame
        self.frame_wh = Frame(self.frame_tool)
        self.frame_wh.pack()

        self.frame_button = Frame(self.frame_tool)
        self.frame_button.pack()

        # Separator frame2
        self.frame_separator2 = Frame(self.frame_tool)
        self.frame_separator2.pack()

        # Crop input Frame
        self.frame_ci = Frame(self.frame_tool)
        self.frame_ci.pack()

        # Crop button frame
        self.frame_cb = Frame(self.frame_tool)
        self.frame_cb.pack()