import cv2 as cv


class VideoProcessor():
    def __init__(self):
        # add selecting tile size
        self.tile_size = 20
        self.vid = None

    def set_tile_size(self, size):
        self.tile_size = size

    def select_video(self, vid):
        self.vid = vid
        print(self.vid)

    def show_video(self):

        print(self.vid)
        if not self.vid:
            print("no video selected")
            return

        video = cv.VideoCapture(self.vid)

        if video.isOpened() == False:
            print("Error opening stream or file")
            return

        while (video.isOpened()):
            ret, frame = video.read()

            if ret != True:
                break

            grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            cv.imshow('Frame', grey)

            if cv.waitKey(25) & 0xFF == ord('q'):
                break

        video.release()
        cv.destroyAllWindows()
