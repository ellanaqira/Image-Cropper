from tkinter import *
from main_element import Main_element

class Main_window:
    def __init__(self):
        self.main_window = Tk()

        # CALLING ELEMENT FROM MAIN_ELEMENT
        self.main_element = Main_element(self.main_window)
        self.main_element.image_label()

        self.main_element.left_cropinput()
        self.main_element.top_cropinput()
        self.main_element.right_cropinput()
        self.main_element.bottom_cropinput()

        self.main_element.width_height_te()
        self.main_element.crop_button()
        self.main_element.open_image_button()

        self.window_setup()

    def window_setup(self):
        self.main_window.geometry("1000x600")
        self.main_window.title("Image Cropper")
        self.main_window.config(bg="#5E5E5E")

    def run(self):
        self.main_window.mainloop()
    
if __name__ == "__main__":
    app = Main_window()
    app.run()