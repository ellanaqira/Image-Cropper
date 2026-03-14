from tkinter import *
from main_element import Main_element

class Main_window:
    def __init__(self):
        self.main_window = Tk()

        # CALLING ELEMENT FROM MAIN_ELEMENT
        self.main_element = Main_element(self.main_window)
        self.main_element.file_name_label()
        self.main_element.ori_image_label()
        self.main_element.crop_image_label()

        self.main_element.original_size_label()
        self.main_element.size_label_ori()
        self.main_element.cropped_size_label()
        self.main_element.size_label_crop()
        # Separator line1
        self.main_element.separator_ln1()

        self.main_element.left_cropinput()
        self.main_element.smaller_symbol1()
        self.main_element.right_cropinput()
        self.main_element.top_cropinput()
        self.main_element.smaller_symbol2()
        self.main_element.bottom_cropinput()
        self.main_element.crop_button()
        # Separator line2
        self.main_element.separator_ln2()

        self.main_element.open_image_button()
        # Separator line3
        self.main_element.separator_ln3()

        self.main_element.buttons()

        self.window_setup()

    def window_setup(self):
        icon = PhotoImage(file='aset/cropper_icon.png')
        self.main_window.iconphoto(True, icon)
        self.main_window.geometry("1000x600")
        self.main_window.title("Image Cropper")

    def run(self):
        self.main_window.mainloop()
    
if __name__ == "__main__":
    app = Main_window()
    app.run()