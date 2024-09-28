from PIL import Image, ImageDraw
import numpy as np
import copy


class ImageProcessor():
    def __init__(self, img, tile_size=2):
        self.img = Image.open(img).convert('RGB')
        self.height = self.img.size[1]
        self.width = self.img.size[0]
        self.ratio = self.height/self.width
        self.start_len = 0
        self.tile_size = tile_size

    def process_frame(self):

        pixels = np.array(self.img.getdata(), dtype='i,i,i')
        self.start_len = len(pixels)
        print('original len', len(pixels))

        pixels.shape = (-1, self.height)

        # self.img.show()

        pixel_map = self.create_pixel_map(pixels)

        self.test_pixelation(pixel_map)

    def cut_to_size(self, pixels):
        cut_pixels = copy.deepcopy(pixels)

        # "cut" the image to size, removing from right and bottom
        x_diff = self.width % self.tile_size
        y_diff = self.height % self.tile_size

        cut_pixels = np.resize(
            cut_pixels, (len(cut_pixels)-y_diff, len(cut_pixels[1])-x_diff))

        # remove loging later
        print(f'original height {len(pixels)}, new height {
            len(cut_pixels)} ydiff was {y_diff}')
        print(' ')
        print(f'original width {len(pixels[0])}, new width {
              len(cut_pixels[0])}, xdiff was {x_diff}')

        self.height = self.height - y_diff
        self.width = self.width - x_diff

        return cut_pixels

    def create_pixel_map(self, pixels):

        resized_pixels = self.cut_to_size(pixels)

        tiles = []

        resized_pixels = np.array(resized_pixels)

        resized_pixels = np.array(
            [[1, 1, 2, 2, 3, 3],
             [1, 1, 2, 2, 3, 3],
             [4, 4, 5, 5, 6, 6],
             [4, 4, 5, 5, 6, 6],
             [7, 7, 8, 8, 9, 9],
             [7, 7, 8, 8, 9, 9]])

        for i in range(0, len(resized_pixels), self.tile_size):

            for j in range(0, len(resized_pixels[0]), self.tile_size):
                slice = resized_pixels[i:i+self.tile_size, j:j+self.tile_size]

                averaged = self.avg_in_color(
                    slice)

                tiles.append(averaged)
        print(tiles)
        tilesArr = np.array(tiles, dtype='i')
        tilesArr.shape = (3, 3)
        print(tilesArr)
        return tiles

    def avg_in_greyscale(self, pixels):
        # formula for converting to greyscale is
        # 0.299 Red + 0.587 Green + 0.144 Blue
        flat = pixels.flatten()

    def avg_in_color(self, pixels):
        print(pixels)

        # R = 0
        # G = 0
        # B = 0

        flat = pixels.flatten()
        print(len(flat))
        return int(flat[0])

        # for item in flat:
        #     # R += item
        #     R += item[0]
        #     G += item[1]
        #     B += item[2]

        # # return int(R // (self.tile_size * self.tile_size))
        # return (int(R//len(flat)), int(G//len(flat)), int(B//len(flat)))

    # to be removed after finished
    def test_pixelation(self, pixels):
        pass
        # print(f'original pixels len {
        #       self.start_len} \n new pixel len {len(pixels)}, ratio is {self.ratio}')

        # img = Image.new("RGB", (996//2, 664//2))
        # img.putdata(pixels)
        # img.show()

        # RATIO, YOU NEED THE WIDTH to HEIGHT RATIO!!!
        # TRY GREYSCALE FIRST
