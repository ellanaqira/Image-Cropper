from PIL import Image, ImageTk

class Aset:
    def __init__(self):
        self.line = self.load_img('aset/line.png', (40,2))
        self.info_icon = self.load_img('aset/exclamation_mark.png', (70,70))

    def load_img(self, path, size):
        img = Image.open(path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)