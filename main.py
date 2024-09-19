from interface.Window import Window
from src.process_frame import process_frame


def main():
    window = Window(process_frame)
    window.mainloop()


if __name__ == '__main__':
    main()
