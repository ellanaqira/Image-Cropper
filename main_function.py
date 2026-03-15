from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import os

class Main_function:
    def open_file(self, name_label, image_label, width_label, height_label):
        self.file_types = ()
        self.image_file_path = fd.askopenfilename(initialdir='/home/lana/Pictures',
                                         filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico"),
                                                    ("all files", "*.*")])
        if self.image_file_path:
            self.image = Image.open(self.image_file_path)
            img_size = list(self.image.size)
            print(f"image size {img_size}")
            print(img_size[0])
            print(img_size[1])
            self.img_width = int(img_size[0])
            self.img_height = int(img_size[1])

            while self.img_width > 1000 or self.img_height > 1000:
                self.img_width = int(self.img_width/2)
                self.img_height = int(self.img_height/2)
                self.image = self.image.resize((self.img_width, self.img_height))
                print(f"width divided by 2  = {self.img_width}")
                print(f"height divided by 2 = {self.img_height}")
            self.photo = ImageTk.PhotoImage(self.image)
            name_label.config(text=f"{self.image_file_path}")
            image_label.config(image=self.photo)
            image_label.image = self.photo

            width_label.config(text=img_size[0])
            height_label.config(text=img_size[1])

    def crop_img_cmd(self, master, left_entry, top_entry, right_entry, bottom_entry, cropw_label, croph_label, crop_prev, info_icon):
        try:
            crop_l = int(left_entry.get())
            crop_u = int(top_entry.get())
            crop_r = int(right_entry.get())
            crop_b = int(bottom_entry.get())

            real_img = Image.open(self.image_file_path)
            print(f"real image = {real_img.size}")
            self.cropped_img = real_img.crop((crop_l, crop_u, crop_r, crop_b))
            crop_img_size = list(self.cropped_img.size)
            self.crop_width = int(crop_img_size[0])
            self.crop_height = int(crop_img_size[1])
            cropw_label.config(text=self.crop_width)
            croph_label.config(text=self.crop_height)
            self.raw_cropped_img = self.cropped_img.resize((self.crop_width, self.crop_height))

            while self.crop_width > 800 or self.crop_height > 800:
                self.crop_width = int(self.crop_width/2)
                self.crop_height = int(self.crop_height/2)
                self.cropped_img = self.cropped_img.resize((self.crop_width, self.crop_height))

            show_img = ImageTk.PhotoImage(self.cropped_img)
            crop_prev.config(image=show_img)
            crop_prev.image = show_img
            print(self.cropped_img)

        except AttributeError:
            mb.showerror("No Image", "You haven't added any image yet.")
    
        except ValueError:
            info_win = Toplevel(master)
            info_win.geometry("350x170")
            info_win.resizable(FALSE, FALSE)
            info_win.title('Information')
            info_win.config(bg="#FFFFFF")

            info_label = Label(info_win,
                               font=('system ui', 11),
                               justify='left',
                               image=info_icon,
                               compound='left',
                               bg="#FFFFFF",
                               padx=20,
                               text="""
Information

- Left must be smaller than Right
- Top must be smaller than Bottom""")
            info_label.pack()

            Button(info_win,
                text="OK",
                width=10,
                pady=3,
                command=lambda:info_win.destroy()).pack(pady=(25,0))
            
    def change_bg_color(self, ori_label, crop_label, button):
        bg_color = colorchooser.askcolor()
        ori_label.config(bg=bg_color[1])
        crop_label.config(bg=bg_color[1])
        button.config(bg=bg_color[1])

    def show_crop_img(self):
        try:
            self.raw_cropped_img.show()
        except AttributeError:
            mb.showerror("No Image", "You haven't cropped any image.")

    def zoomin_ori_img(self, ori_label):
        try:
            self.img_width = self.img_width / (90/100)
            zoom_w = int(self.img_width)

            self.img_height = self.img_height / (90/100)
            zoom_h = int(self.img_height)

            zoom_img = self.image.resize((zoom_w, zoom_h))
            show_img = ImageTk.PhotoImage(zoom_img)
            ori_label.config(image=show_img)
            ori_label.image = show_img
        except AttributeError:
            mb.showerror("No Image", "You haven't added any image yet.")

    def zoomout_ori_img(self, ori_label):
        try:
            self.img_width = self.img_width * (90/100)
            zoom_w = int(self.img_width)

            self.img_height = self.img_height * (90/100)
            zoom_h = int(self.img_height)

            zoom_img = self.image.resize((zoom_w, zoom_h))
            show_img = ImageTk.PhotoImage(zoom_img)
            ori_label.config(image=show_img)
            ori_label.image = show_img
        except AttributeError:
            mb.showerror("No Image", "You haven't added any image yet.")

    def rotate(self, crop_label):
        try:
            self.cropped_img = self.cropped_img.rotate(90, expand=True)
            raw_rot_img = self.cropped_img 
            show_rot_img = ImageTk.PhotoImage(raw_rot_img)
            crop_label.config(image=show_rot_img)
            crop_label.image = show_rot_img
        
            # rot_img.show()
        except AttributeError:
            mb.showerror("No Image", "You haven't cropped any image yet.")

    def zoomin_crop_img(self, crop_label):
        try:
            self.crop_width = self.crop_width / (90/100)
            zoom_w = int(self.crop_width)

            self.crop_height = self.crop_height / (90/100)
            zoom_h = int(self.crop_height)

            zoom_img = self.cropped_img.resize((zoom_w, zoom_h))
            show_img = ImageTk.PhotoImage(zoom_img)
            crop_label.config(image=show_img)
            crop_label.image = show_img
        except AttributeError:
            mb.showerror("No Image", "You haven't cropped any image yet.")

    def zoomout_crop_img(self, crop_label):
        try:
            self.crop_width = self.crop_width * (90/100)
            zoom_w = int(self.crop_width)

            self.crop_height = self.crop_height * (90/100)
            zoom_h = int(self.crop_height)

            zoom_img = self.cropped_img.resize((zoom_w, zoom_h))
            show_img = ImageTk.PhotoImage(zoom_img)
            crop_label.config(image=show_img)
            crop_label.image = show_img
        except AttributeError:
            mb.showerror("No Image", "You haven't cropped any image yet.")

    def flip_horizontal(self, crop_label):
        try:
            self.cropped_img = self.cropped_img.transpose(method=Image.FLIP_LEFT_RIGHT)
            flip_h_img = self.cropped_img
            show_flip_h = ImageTk.PhotoImage(flip_h_img)
            crop_label.config(image=show_flip_h)
            crop_label.image = show_flip_h
        except AttributeError:
            mb.showerror("No Image", "You haven't cropped any image yet.")

    def flip_vertical(self, crop_label):
        try:
            self.cropped_img = self.cropped_img.transpose(method=Image.FLIP_TOP_BOTTOM)
            flip_v_img = self.cropped_img
            show_flip_v = ImageTk.PhotoImage(flip_v_img)
            crop_label.config(image=show_flip_v)
            crop_label.image = show_flip_v
        except AttributeError:
            mb.showerror("No Image", "You haven't cropped any image yet.")

    def clear_crop_input(self, l_entry, r_entry, t_entry, b_entry):
        l_entry.delete('0', 'end')
        r_entry.delete('0', 'end')
        t_entry.delete('0', 'end')
        b_entry.delete('0', 'end')

    def save_image(self, main_window):
        save_win = Toplevel(main_window)
        save_win.attributes('-topmost', bool(True))
        save_win.geometry("470x190")
        save_win.resizable(FALSE, FALSE)
        save_win.title('Save image')

        # file path frame
        fp_frame = Frame(save_win)
        fp_frame.pack()
        # file name frame
        fn_frame = Frame(save_win)
        fn_frame.pack()
        # save button fraem
        s_btn_frame = Frame(save_win)
        s_btn_frame.pack()

        # file path label and entry
        fp_label = Label(fp_frame,
                        text="File Path---(Paste your file path here)")
        fp_label.grid(row=0, column=0, sticky='w', pady=(20,0))
        fp_entry = Entry(fp_frame,
                    width=50)
        fp_entry.grid(row=1, column=0, sticky='w')

        # file name label, entry, and combobox
        fn_label = Label(fn_frame,
                        text="File Name")
        fn_label.grid(row=0, column=0, sticky='w')
        fn_entry = Entry(fn_frame,
                    width=43)
        fn_entry.grid(row=1, column=0, sticky='w')

        # Combobox creation
        n = StringVar()
        monthchoosen = ttk.Combobox(fn_frame, width = 5, textvariable = n)
        monthchoosen['values'] = ('.png',
                                  '.gif',
                                  '.bmp',
                                  '.ico')
        monthchoosen.grid(row=1, column=2)
        monthchoosen.current(0)

        def save_image():
            f_path = fp_entry.get()
            f_name = fn_entry.get()
            f_format = n.get()
            if f_path == "":
                mb.showerror('empty file path', 'you havent enter a File path')
            elif f_name == "":
                mb.showerror('empty file name', 'you havent enter a File name')
            else:
                try:
                    print((f"{f_path}/{f_name}"))
                    self.cropped_img.save(f"{f_path}/{f_name}{f_format}")
                    mb.showinfo("save image", f"{f_name} has been saved at:\n{f_path}/{f_name}{f_format})")
                except FileNotFoundError:
                    mb.showerror("Directory not found", f"No such file or directory: {f_path}/{f_name}{f_format}")

        save_button = Button(s_btn_frame,
                            text="Save",
                            bg="#4D75B1",
                            fg="#ffffff",
                            padx=187,
                            command=save_image)
        save_button.pack(pady=(30,0))       
