from tkinter import *
from tkinter import filedialog as fd
from main_frame import Main_frame
from main_function import Main_function

class Main_element:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_frame = Main_frame()
        self.main_function = Main_function()

    def image_label(self):
        self.img_label = Label(self.main_window,
                          bg="#f8f8f8",
                          relief='sunken',
                          bd=2)
        self.img_label.pack(expand=True, fill='both', padx=20, pady=20)

    def open_image_button(self):
        open_img_btn = Button(self.main_frame.frame_button,
                              text="Open Image",
                              command=lambda: self.main_function.open_file(self.img_label))
        open_img_btn.grid(row=0, column=0, padx=(0,20))
        