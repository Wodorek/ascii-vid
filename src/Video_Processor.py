import cv2 as cv


class VideoProcessor():
    def __init__(self):
        # add selecting tile size
        self.tile_size = 60
        self.vid = None

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

            pixelated = self.process_frame(frame, width, height)

            cv.imshow('Frame', pixelated)

            if cv.waitKey(25) & 0xFF == ord('q'):
                break

        video.release()
        cv.destroyAllWindows()

    def process_frame(self, frame, frame_w, frame_h):

        print(frame)

        new_width = int(frame_w // self.tile_size)
        new_height = int(frame_h // self.tile_size)

        print(new_height, new_width)

        tmp_frame = cv.resize(frame, (new_width, new_height),
                              interpolation=cv.INTER_LINEAR)

        output_frame = cv.resize(
            tmp_frame, (int(frame_w), int(frame_h)), interpolation=cv.INTER_NEAREST)
        return output_frame
