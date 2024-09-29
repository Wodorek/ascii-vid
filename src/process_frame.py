
import numpy as np
import copy


class ImageProcessor():
    def __init__(self, img, tile_size=60):
        self.img = None
        self.height = self.img.size[1]
        self.width = self.img.size[0]
        self.ratio = self.height/self.width
        self.start_len = 0
        self.tile_size = tile_size
