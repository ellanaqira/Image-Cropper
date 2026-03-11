from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk

class Main_function:
    def open_file(self, image_label, width_label, height_label):
        self.file_types = ()
        self.image_file_path = fd.askopenfilename(initialdir='/home/lana/Pictures',
                                         filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico"),
                                                    ("all files", "*.*")])
        if self.image_file_path:
            image = Image.open(self.image_file_path)
            img_size = list(image.size)
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
            image_label.config(image=photo)
            image_label.photo = photo

            width_label.delete('0', 'end')
            height_label.delete('0', 'end')
            width_label.insert("0", img_size[0])
            height_label.insert("0", img_size[1])

    def crop_img_cmd(self, left_entry, top_entry, right_entry, bottom_entry):
        crop_l = int(left_entry.get())
        crop_u = int(top_entry.get())
        crop_r = int(right_entry.get())
        crop_b = int(bottom_entry.get())

        real_img = Image.open(self.image_file_path)
        print(f"real image = {real_img.size}")
        croppped_img = real_img.crop((crop_l, crop_u, crop_r, crop_b))
        croppped_img.show()