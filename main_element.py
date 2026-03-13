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

    # Crop input class
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

    # Separator line class
    class Separator_Line:
        def __init__(self, frame, image, row, column):
            self.frame = frame
            self.image = image
            self.row = row
            self.column = column

        def separator_line(self):
            line = Label(self.frame,
                         image=self.image)
            line.grid(row=self.row, column=self.column, pady=(10,0))

    # Button tools class
    class Button_Tools:
        def __init__(self, frame, image, command, row, column):
            self.frame = frame
            self.image = image
            self.command = command
            self.row = row
            self.column = column

        def button_tool(self):
            btn = Button(self.frame,
                         image=self.image,
                         command=self.command)
            btn.grid(row=self.row, column=self.column, padx=2)

    def file_name_label(self):
        self.file_name = Label(self.main_window,
                               text="No Image",
                               relief='sunken',
                               bd=2,
                               padx=5,
                               bg="#ffffff")
        self.file_name.pack(padx=(10,0), pady=(0,0), fill='x')

    def ori_image_label(self):
        self.img_label = Label(self.main_window,
                            #    text="Original Image",
                            #    compound='top',
                               bg="#FFFFFF",
                               relief='sunken',
                               padx=0,
                               bd=2)
        self.img_label.pack(expand=True, fill='both', side='right', padx=(5,0), pady=(0,10))

    def crop_image_label(self):
        self.crop_img_label = Label(self.main_window,
                                    # text="Cropped Image",
                                    # compound='top',
                                    bg="#FFFFFF",
                                    relief='sunken',
                                    padx=0,
                                    bd=2)
        self.crop_img_label.pack(expand=True, fill='both', side='left', padx=(10,0), pady=(0,10))

    def original_size_label(self):
        ori_size_label = Label(self.main_frame.frame_separator1,
                          text="_____[Original]_____")
        ori_size_label.grid(row=0, column=0)

    def size_label_ori(self):
        # width label
        self.width_label = Label(self.main_frame.frame_wh_ori,
                                 width=7,
                                 bg="#C4C4C4",
                                 relief='sunken',
                                 bd=1)
        self.width_label.grid(row=0, column=0)
        # height label
        self.height_label = Label(self.main_frame.frame_wh_ori,
                                  width=7,
                                  bg="#C4C4C4",
                                  relief='sunken',
                                  bd=1)
        self.height_label.grid(row=0, column=1)

    def cropped_size_label(self):
        crop_size_label = Label(self.main_frame.frame_separator2,
                          text="_____[Cropped]_____")
        crop_size_label.grid(row=0, column=0)

    def size_label_crop(self):
        # width label
        self.cropwidth_label = Label(self.main_frame.frame_wh_crop,
                                 width=7,
                                 bg="#C4C4C4",
                                 relief='sunken',
                                 bd=1)
        self.cropwidth_label.grid(row=0, column=0)
        # height label
        self.cropheight_label = Label(self.main_frame.frame_wh_crop,
                                  width=7,
                                  bg="#C4C4C4",
                                  relief='sunken',
                                  bd=1)
        self.cropheight_label.grid(row=0, column=1)

    def separator_ln1(self):
        line = self.Separator_Line(self.main_frame.frame_separator3,
                                   self.aset.line,
                                   0,0)
        line.separator_line()

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
                                                                          self.cropwidth_label,
                                                                          self.cropheight_label,
                                                                          self.crop_img_label,
                                                                          self.aset.info_icon))
        crop_btn.grid(row=0, column=0)

    def separator_ln2(self):
        line = self.Separator_Line(self.main_frame.frame_button,
                                   self.aset.line,
                                   0,0)
        line.separator_line()

    def open_image_button(self):
        open_img_btn = Button(self.main_frame.frame_button,
                              text="Open Image",
                              pady=48,
                              padx=21,
                              bg="#4D75B1",
                              fg="#ffffff",
                              relief='flat',
                              command=lambda: self.main_function.open_file(self.file_name,
                                                                           self.img_label, 
                                                                           self.width_label, 
                                                                           self.height_label))
        open_img_btn.grid(row=1, column=0, pady=(10,0))

    def separator_ln3(self):
        line = self.Separator_Line(self.main_frame.frame_button,
                                self.aset.line,
                                2,0)
        line.separator_line()

    def buttons(self):
        button1 = Button(self.main_frame.frame_btn_tools,
                         image=self.aset.bucket_icon,
                         bg="#ffffff",
                         command=lambda: self.main_function.change_bg_color(self.img_label,
                                                                            self.crop_img_label,
                                                                            button1))
        button1.grid(row=0, column=0)

        button2 = self.Button_Tools(self.main_frame.frame_btn_tools,
                          self.aset.show_icon,
                          self.main_function.show_crop_img,
                          0,1)
        button2.button_tool()

        button3 = self.Button_Tools(self.main_frame.frame_btn_tools,
                          None,
                          None,
                          0,2)
        button3.button_tool()

        button4 = self.Button_Tools(self.main_frame.frame_btn_tools,
                          None,
                          None,
                          0,3)
        button4.button_tool()
        
        