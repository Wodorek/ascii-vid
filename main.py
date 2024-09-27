from interface.Window import Window
from src.process_frame import ImageProcessor


def main():
    window = Window(ImageProcessor)
    window.mainloop()


if __name__ == '__main__':
    main()
