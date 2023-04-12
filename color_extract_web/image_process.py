from PIL import Image
import extcolors

class ImageProcess:
    def __init__(self, file_name: str):
        self.img = Image.open('static/image/' + file_name)
        self.resized_img = self.resize_img()

    def resize_img(self):
        w, h = self.img.width, self.img.height
        if w > 1000 or h > 1000:
            if w > h:
                re_img = self.img.resize((int(w // (w / 1000)), int(h // (w / 1000))))
            else:
                re_img = self.img.resize((int(w // (h / 1000)), int(h // (h / 1000))))
            return re_img
        else:
            return self.img

    def most_color(self, n: int):
        img_to_extract = self.resized_img.resize((500, 500))
        colors = extcolors.extract_from_image(img_to_extract, tolerance=n, limit=10)
        color_dict = {}
        for i in range(len(colors[0])):
            r = colors[0][i][0][0]
            g = colors[0][i][0][1]
            b = colors[0][i][0][2]
            col = "#%02x%02x%02x" % (r, g, b)
            color_dict[col] = round(colors[0][i][1] / colors[1] * 100, 4)
        return color_dict