from PIL import Image, ImageTk

class Aset:
    def __init__(self):
        self.line = self.load_img('aset/line.png', (125,3))
        self.info_icon = self.load_img('aset/exclamation_mark.png', (70,70))
        self.bucket_icon = self.load_img('aset/bucket.png', (25,25))
        self.show_icon = self.load_img('aset/show_icon.png', (25,25))
        self.zoomin_icon = self.load_img('aset/zoomin.png', (25,25))
        self.zoomout_icon = self.load_img('aset/zoomout.png', (25,25))
        self.zoomin_crop_icon = self.load_img('aset/crop_zoomin.png', (25,25))
        self.zoomout_crop_icon = self.load_img('aset/crop_zoomout.png', (25,25))
        self.save_icon = self.load_img('aset/save.png', (25,25))
        self.rotate_icon = self.load_img('aset/rotate.png', (25,25))
        self.flip_h = self.load_img('aset/flip_h.png', (25,25))
        self.flip_v = self.load_img('aset/flip_v.png', (25,25))
        self.clear_icon = self.load_img('aset/clear.png', (25,25))
        self.ask_icon = self.load_img('aset/ask.png', (25,25))
        self.main_icon = self.load_img('aset/cropper_icon.png', (120,120))
        self.swan = self.load_img('aset/swan.jpeg', (470,350))
        self.crop_input = self.load_img('aset/crop_input.png', (120,120))
        self.swan_crop = self.load_img('aset/swan_crop.jpeg', (250,220))
        self.white_ball = self.load_img('aset/white_ball.png', (20,20))
        self.gray_ball = self.load_img('aset/gray_ball.png', (20,20))
        self.black_ball = self.load_img('aset/black_ball.png', (20,20))
        self.color_ball = self.load_img('aset/color_ball.png', (20,20))


    def load_img(self, path, size):
        img = Image.open(path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)