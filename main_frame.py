from tkinter import *

class Main_frame:
    def __init__(self):
        self.frame_tool = Frame(relief='sunken', bd=2)
        self.frame_tool.pack(side='right', anchor='n')

        # Separator frame1
        self.frame_separator1 = Frame(self.frame_tool)
        self.frame_separator1.pack()

        # Original Weight and Height Frame
        self.frame_wh_ori = Frame(self.frame_tool)
        self.frame_wh_ori.pack()

        # Separator frame2
        self.frame_separator2 = Frame(self.frame_tool)
        self.frame_separator2.pack()

        # Cropped Weight and Height Frame
        self.frame_wh_crop = Frame(self.frame_tool)
        self.frame_wh_crop.pack()

        # Separator frame3
        self.frame_separator3 = Frame(self.frame_tool)
        self.frame_separator3.pack()

        # Crop input Frame
        self.frame_ci = Frame(self.frame_tool)
        self.frame_ci.pack()

        # Crop button frame
        self.frame_cb = Frame(self.frame_tool)
        self.frame_cb.pack()

        # Open image button frame
        self.frame_button = Frame(self.frame_tool)
        self.frame_button.pack()

        # Button tools frame
        self.frame_btn_tools = Frame(self.frame_tool)
        self.frame_btn_tools.pack()

        # Separator frame4
        self.frame_separator4 = Frame(self.frame_tool)
        self.frame_separator4.pack()