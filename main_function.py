from tkinter import *
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
            image = Image.open(self.image_file_path)
            img_size = list(image.size)
            image_name = (os.path.basename(self.image_file_path))
            print(f"image size {img_size}")
            print(img_size[0])
            print(img_size[1])
            img_width = int(img_size[0])
            img_height = int(img_size[1])

            while img_width > 1000 or img_height > 1000:
                img_width = img_width/2
                img_height = img_height/2
                image = image.resize((int(img_width), int(img_height)))
                print(f"width divided by 2  = {img_width}")
                print(f"height divided by 2 = {img_height}")
            photo = ImageTk.PhotoImage(image)
            name_label.config(text=f"{self.image_file_path}")
            image_label.config(image=photo)
            image_label.image = photo

            # width_label.delete('0', 'end')
            # height_label.delete('0', 'end')
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
            cropped_img = real_img.crop((crop_l, crop_u, crop_r, crop_b))
            crop_img_size = list(cropped_img.size)
            crop_width = int(crop_img_size[0])
            crop_height = int(crop_img_size[1])
            cropw_label.config(text=crop_width)
            croph_label.config(text=crop_height)

            while crop_width > 900 or crop_height > 900:
                crop_width = crop_width/2
                crop_height = crop_height/2
                cropped_img = cropped_img.resize((int(crop_width), int(crop_height)))

            show_img = ImageTk.PhotoImage(cropped_img)
            crop_prev.config(image=show_img)
            crop_prev.image = show_img
            print(cropped_img)
            
            cropped_img.show()
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
