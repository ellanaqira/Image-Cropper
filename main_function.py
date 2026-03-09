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

            # if img_size[0] <= 5000 and img_size[1] <= 5000:
            #     image = image.resize((int(img_size[0]/3), int(img_size[1]/3)))
            #     print("size divided by 3")
        while img_size[0] > 1000 or img_size[1] > 1000:
            image = image.resize((int(img_size[0]/2), int(img_size[1]/2)))
            print(f"size divided by 2 = {image}")
            if img_size[0] < 1000 or img_size[1] < 1000:
                photo = ImageTk.PhotoImage(image)
                image_label.config(image=photo)
                image_label.photo = photo


            # else:
            #     image = image.resize((img_size[0], img_size[1]))
            
            # photo = ImageTk.PhotoImage(image)
            # image_label.config(image=photo)
            # image_label.photo = photo

        
    # def display_image(self, img_label):
    #     image = Image.open(self.image_file_path)
    #     photo = ImageTk.PhotoImage(image)
    #     img_label.config(imgage=photo)
    #     img_label.photo = photo