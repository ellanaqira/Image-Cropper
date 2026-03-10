from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk

class Main_function:
    def open_file(self, image_label):
        self.file_types = ()
        self.image_file_path = fd.askopenfilename(initialdir='/home/lana/Pictures',
                                         filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico"),
                                                    ("all files", "*.*")])
        if self.image_file_path:
            image = Image.open(self.image_file_path)
            img_size = list(image.size)
            print(f"image size {img_size}")
            print(type(img_size))
            print(type(img_size[0]))
            img_width = int(img_size[0])
            img_height = int(img_size[1])

            while img_width > 1000 or img_height > 1000:
                img_width = img_width/2
                img_height = img_height/2
                image = image.resize((int(img_width), int(img_height)))
                print(f"size divided by 2 = {img_width}")
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.photo = photo
                