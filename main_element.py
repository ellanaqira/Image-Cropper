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
        self.img_label.pack(expand=True, fill='both', padx=(20,0), pady=20)

    def width_height_te(self):
        # width TITLE AND ENTRY BAR
        width_title = Label(self.main_frame.frame_wh,
                           text='Width')
        width_title.grid(row=0, column=0)
        self.width_entry = Entry(self.main_frame.frame_wh,
                      width=10)
        self.width_entry.grid(row=1, column=0)
        # HEIGHT TITLE AND ENTRY BAR
        height_title = Label(self.main_frame.frame_wh,
                           text='Height')
        height_title.grid(row=0, column=1)
        self.height_entry = Entry(self.main_frame.frame_wh,
                      width=10)
        self.height_entry.grid(row=1, column=1)

    def crop_button(self):
        crop_btn = Button(self.main_frame.frame_button,
                          text='Crop',
                          command=lambda: self.main_function.crop_img_cmd(self.width_entry,
                                                                          self.height_entry))
        crop_btn.grid(row=0, column=0)

    def open_image_button(self):
        open_img_btn = Button(self.main_frame.frame_button,
                              text="Open Image",
                              command=lambda: self.main_function.open_file(self.img_label, 
                                                                           self.width_entry, 
                                                                           self.height_entry))
        open_img_btn.grid(row=1, column=0)
        