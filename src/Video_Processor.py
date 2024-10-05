import cv2 as cv
from PIL import Image, ImageFont, ImageDraw
import numpy as np


class VideoProcessor():
    def __init__(self):
        # add selecting tile size
        self.tile_size = 40
        self.vid = None
        self.font = ImageFont.truetype(
            'LiberationSerif-Regular.ttf', self.tile_size)
        self.selected_greyscale = ['@', '%', '#',
                                   '*', '+', '=', '-', ':', '.', ' ', ' ']
        # used to select index of greyscale
        self.divider = (255 // len(self.selected_greyscale)) + 1

    def set_tile_size(self, size):
        self.tile_size = size

    def select_video(self, vid):
        self.vid = vid

    def show_video(self):

        if not self.vid:
            print("no video selected")
            return

        video = cv.VideoCapture(self.vid)

        if video.isOpened() == False:
            print("Error opening stream or file")
            return

        height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
        width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
        frame_rate = video.get(cv.CAP_PROP_FPS)

        print(f'height: {height}, width: {width}, frame_rate: {frame_rate}')
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        output = cv.VideoWriter('test.mp4', fourcc,
                                frame_rate, (width, height))
        frames_num = video.get(cv.CAP_PROP_FRAME_COUNT)

        print('started')

        while (video.isOpened()):
            ret, frame = video.read()
            print(f'{video.get(cv.CAP_PROP_POS_FRAMES)}/{frames_num}')

            if ret != True:
                break

            pixelated = self.pixelate_frame(frame, width, height)
            blank = np.full([height, width, 3],
                            (255, 255, 255), dtype=np.uint8)

            with_text = self.fill_with_chars(
                pixelated, blank, int(width), int(height))

            output.write(with_text)

            if cv.waitKey(25) & 0xFF == ord('q'):
                break

        print('finished')
        print(f'size of out = {output.get(cv.CAP_PROP_FRAME_HEIGHT)}')
        video.release()
        output.release()

        cv.destroyAllWindows()

    def pixelate_frame(self, frame, frame_w, frame_h):
        new_width = int(frame_w // self.tile_size)
        new_height = int(frame_h // self.tile_size)

        tmp_frame = cv.resize(frame, (new_width, new_height),
                              interpolation=cv.INTER_LINEAR)

        output_frame = cv.resize(
            tmp_frame, (int(frame_w), int(frame_h)), interpolation=cv.INTER_NEAREST)
        return output_frame

    def write_char(self, pil_draw, x, y, char):
        pil_draw.text((x, y), char, (0, 0, 0), font=self.font)

    def fill_with_chars(self, input_frame, output_frame, width, height):
        # opencv drawing text on image is bad, so conversion to PIL image is required

        read_from = Image.fromarray(cv.cvtColor(input_frame, cv.COLOR_BGR2RGB))
        draw_to = Image.fromarray(
            cv.cvtColor(output_frame, cv.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(draw_to)

        for i in range(0, width, self.tile_size):
            for j in range(0, height, self.tile_size):
                char = self.select_char(read_from.getpixel((i, j)), True)
                self.write_char(draw, i, j, char)

        return cv.cvtColor(np.asanyarray(draw_to), cv.COLOR_RGB2BGR)

    def select_char(self, px, color=False):
        if color:
            pixel = self.rgb_to_grey(px)
        else:
            pixel = px[0]
        idx = pixel // self.divider

        return self.selected_greyscale[idx]

    def rgb_to_grey(self, px):
        # formula for conversion is 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue
        R, G, B = px
        return int((0.299 * R + 0.587 * G + 0.0114 * B)//1)
