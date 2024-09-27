from PIL import Image, ImageDraw


class ImageProcessor():
    def __init__(self, img):
        self.img = Image.open(img).convert('RGBA')

    def process_frame(self):

        pixels = list(self.img.getdata())

        width, height = self.img.size

        pixels = [pixels[i * width:(i+1) * width] for i in range(height)]

        self.img.show()

    def turn_into_tiles(self, pixels):
        # tiles are laid as  1 2 3
        #                    4 5 6
        #                    7 8 9

        pass
