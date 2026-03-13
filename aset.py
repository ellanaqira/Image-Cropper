from PIL import Image, ImageTk

class Aset:
    def __init__(self):
        self.line = self.load_img('aset/line.png', (125,3))
        self.info_icon = self.load_img('aset/exclamation_mark.png', (70,70))
        self.bucket_icon = self.load_img('aset/bucket.png', (25,25))
        self.show_icon = self.load_img('aset/show_icon.png', (25,25))
        self.zoomin_icon = self.load_img('aset/zoomin.png', (25,25))
        self.zoomout_icon = self.load_img('aset/zoomout.png', (25,25))


    def load_img(self, path, size):
        img = Image.open(path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)