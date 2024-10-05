import cv2 as cv
from PIL import Image, ImageFont, ImageDraw
import numpy as np


class VideoProcessor():
    def __init__(self):
        # add selecting tile size
        self.tile_size = 20
        self.vid = None
        self.font = ImageFont.truetype(
            'LiberationSerif-Regular.ttf', self.tile_size)

    def set_tile_size(self, size):
        self.tile_size = size

    def select_video(self, vid):
        self.vid = vid
        print(self.vid)

    def show_video(self):

        if not self.vid:
            print("no video selected")
            return

        video = cv.VideoCapture(self.vid)

        if video.isOpened() == False:
            print("Error opening stream or file")
            return

        height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
        width = video.get(cv.CAP_PROP_FRAME_WIDTH)
        frame_rate = video.get(cv.CAP_PROP_FPS)

        while (video.isOpened()):
            ret, frame = video.read()

            if ret != True:
                break

            pixelated = self.pixelate_frame(frame, width, height)

            with_text = self.write_char(pixelated, 0, 100)

            cv.imshow('Frame', with_text)

            if cv.waitKey(25) & 0xFF == ord('q'):
                break

        video.release()
        cv.destroyAllWindows()

    def pixelate_frame(self, frame, frame_w, frame_h):
        new_width = int(frame_w // self.tile_size)
        new_height = int(frame_h // self.tile_size)

        tmp_frame = cv.resize(frame, (new_width, new_height),
                              interpolation=cv.INTER_LINEAR)

        output_frame = cv.resize(
            tmp_frame, (int(frame_w), int(frame_h)), interpolation=cv.INTER_NEAREST)
        return output_frame

    def write_char(self, frame, x, y):
        # opencv drawing text on image is bad, so conversion to PIL image is required
        pil_image = Image.fromarray(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_image)
        draw.text((x, y), 'a', (0, 0, 0), font=self.font)

        return cv.cvtColor(np.asanyarray(pil_image), cv.COLOR_RGB2BGR)
