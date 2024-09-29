from interface.Window import Window
from src.Video_Processor import VideoProcessor


def main():
    window = Window(VideoProcessor)
    window.mainloop()


if __name__ == '__main__':
    main()
