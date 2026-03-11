from tkinter import *
from tkinter import filedialog as fd
from main_frame import Main_frame
from main_function import Main_function
from aset import Aset

class Main_element:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_frame = Main_frame()
        self.main_function = Main_function()
        self.aset = Aset()

    def image_label(self):
        self.img_label = Label(self.main_window,
                          bg="#f8f8f8",
                          relief='sunken',
                          padx=0,
                          bd=2)
        self.img_label.pack(expand=True, fill='both', side="right", padx=(20,0), pady=20)

    class Crop_Input:
        def __init__(self, frame, configure):
            self.frame = frame
            self.title = configure.get ("title", "")
            self.row_label = configure.get("row l", 0)
            self.col_label = configure.get("col l", 0)
            self.entry_width = configure.get("ent w", 0)
            self.row_entry = configure.get("row e", 0)
            self.col_entry = configure.get("col e", 0)
        # crop input title and entry
        def ci_titen(self):
            crop_label = Label(self.frame,
                               text=self.title)
            crop_label.grid(row=self.row_label, column=self.col_label)

            self.crop_entry = Entry(self.frame,
                               width=self.entry_width)
            self.crop_entry.grid(row=self.row_entry, column=self.col_entry)

    def separator1(self):
        sep_ln1 = Label(self.main_frame.frame_separator1,
                       image=self.aset.line)
        sep_ln1.grid(row=0, column=0, pady=(5,0))

    def left_cropinput(self):
        self.configure = {"title" : "Left",
                          "row l" : 0,
                          "col l" : 0,
                          "ent w" : 6,
                          "row e" : 1,
                          "col e" : 0,
                          }
        self.left_ci = self.Crop_Input(self.main_frame.frame_ci, self.configure)
        self.left_ci.ci_titen()

    def right_cropinput(self):
        self.configure = {"title" : "Right",
                          "row l" : 0,
                          "col l" : 2,
                          "ent w" : 6,
                          "row e" : 1,
                          "col e" : 2
                          }
        self.right_ci = self.Crop_Input(self.main_frame.frame_ci, self.configure)
        self.right_ci.ci_titen()

    def smaller_symbol1(self):
        smaller_symbol = Label(self.main_frame.frame_ci,
                        text="<",
                        font=('system ui', 14))
        smaller_symbol.grid(row=1, column=1)

    def top_cropinput(self):
        self.configure = {"title" : "Top",
                          "row l" : 3,
                          "col l" : 0,
                          "ent w" : 6,
                          "row e" : 4,
                          "col e" : 0
                          }
        self.top_ci = self.Crop_Input(self.main_frame.frame_ci, self.configure)
        self.top_ci.ci_titen()

    def smaller_symbol2(self):
        smaller_symbol = Label(self.main_frame.frame_ci,
                        text="<",
                        font=('system ui', 14))
        smaller_symbol.grid(row=4, column=1)

    def bottom_cropinput(self):
        self.configure = {"title" : "Bottom",
                          "row l" : 3,
                          "col l" : 2,
                          "ent w" : 6,
                          "row e" : 4,
                          "col e" : 2
                          }
        self.bottom_ci = self.Crop_Input(self.main_frame.frame_ci, self.configure)
        self.bottom_ci.ci_titen()

    def crop_button(self):
        crop_btn = Button(self.main_frame.frame_cb,
                          text='Crop',
                          pady=2,
                          padx=44,
                          bg="#4D75B1",
                          fg="#ffffff",
                          relief='flat',
                          command=lambda: self.main_function.crop_img_cmd(self.main_window,
                                                                          self.left_ci.crop_entry,
                                                                          self.top_ci.crop_entry,
                                                                          self.right_ci.crop_entry,
                                                                          self.bottom_ci.crop_entry,
                                                                          self.aset.info_icon))
        crop_btn.grid(row=0, column=0)
    
    def separator2(self):
        sep_ln2 = Label(self.main_frame.frame_separator2,
                       image=self.aset.line)
        sep_ln2.grid(row=0, column=0, pady=(5,0))

    def width_height_te(self):
        # width TITLE AND ENTRY BAR
        width_title = Label(self.main_frame.frame_wh,
                           text='Width')
        width_title.grid(row=0, column=0)
        self.width_entry = Entry(self.main_frame.frame_wh,
                                 width=7)
        self.width_entry.grid(row=1, column=0)
        # HEIGHT TITLE AND ENTRY BAR
        height_title = Label(self.main_frame.frame_wh,
                           text='Height')
        height_title.grid(row=0, column=1)
        self.height_entry = Entry(self.main_frame.frame_wh,
                      width=7)
        self.height_entry.grid(row=1, column=1)

    def open_image_button(self):
        open_img_btn = Button(self.main_frame.frame_button,
                              text="Open Image",
                              pady=2,
                              padx=20,
                              bg="#4D75B1",
                              fg="#ffffff",
                              relief='flat',
                              command=lambda: self.main_function.open_file(self.img_label, 
                                                                           self.width_entry, 
                                                                           self.height_entry))
        open_img_btn.grid(row=1, column=0)
        