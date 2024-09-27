from PIL import Image, ImageDraw
import copy


class ImageProcessor():
    def __init__(self, img):
        self.img = Image.open(img).convert('RGBA')

    def process_frame(self):

        pixels = list(self.img.getdata())

        width, height = self.img.size

        pixels = [pixels[i * width:(i+1) * width] for i in range(height)]

        self.img.show()

        self.turn_into_tiles(pixels)

    def turn_into_tiles(self, pixels, tile_size=3):
        # tiles are laid as  1 2 3
        #                    4 5 6
        #                    7 8 9

        pixels_copy = copy.deepcopy(pixels)

        # "cut" the image to size
        x_diff = len(pixels_copy[0]) % tile_size
        y_diff = len(pixels_copy) % tile_size

        if x_diff > 0:
            for i in range(len(pixels_copy)):
                pixels_copy[i] = pixels_copy[i][: len(pixels_copy[i]) - x_diff]

        if y_diff > 0:
            pixels_copy = pixels_copy[: len(pixels_copy) - y_diff]

        tiles = []

        print(f'original height {len(pixels)}, new height {
              len(pixels_copy)} ydiff was {y_diff}')
        print(' ')
        print(f'original width {len(pixels[0])}, new width {
              len(pixels_copy[0])}, xdiff was {x_diff}')

        for i in range(0, len(pixels), tile_size):
            pass
