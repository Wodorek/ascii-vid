import customtkinter as ctk
import cv2
from interface.slider import Slider


class Window(ctk.CTk):
    def __init__(self, video_processor):
        super().__init__()

        # main window config
        self.geometry('800x600')
        self.title('Ascii vid')
        self.resizable(False, False)
        self.columnconfigure((0, 1, 2, 3), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        # change later to None
        self.selected_file = './rect.png'
        self.select_btn = None
        self.process_btn = None

        # create sliders
        # slider_1 = Slider(self, text='witam', color=self._fg_color)
        # slider_2 = Slider(self, text='konsumenta', color=self._fg_color)
        # slider_3 = Slider(self, text='bozego', color=self._fg_color)

        # # place sliders
        # slider_1.grid(row=1, column=0, columnspan=2)
        # slider_2.grid(row=2, column=0, columnspan=2)
        # slider_3.grid(row=3, column=0, columnspan=2)

        # place buttons
        buttons_frame = ctk.CTkFrame(master=self, fg_color=self._fg_color)
        buttons_frame.columnconfigure((0, 1, 2), weight=1)
        buttons_frame.rowconfigure((0, 1, 2), weight=1)
        buttons_frame.grid(row=6, column=0, columnspan=4, sticky='nswe', )

        button_1 = ctk.CTkButton(buttons_frame,
                                 text="Open Video", command=self.select_file)
        button_2 = ctk.CTkButton(buttons_frame,
                                 text="Preview Frame", command=self.display_preview, state='disabled')
        self.select_btn = button_2
        button_3 = ctk.CTkButton(buttons_frame,
                                 text="Save Video", command=lambda: self.process_and_save(video_processor))
        self.process_btn = button_3

        # remove before release
        self.select_btn.configure(True, state='normal')
        self.process_btn.configure(True, state='normal')

        button_1.grid(row=1, column=0,)
        button_2.grid(row=1, column=1,)
        button_3.grid(row=1, column=2,)

    def select_file(self):
        file = ctk.filedialog.askopenfilename(
            filetypes=[('MP4 files', '*.mp4'), ('AVI files', '*.avi')])
        self.selected_file = file
        self.select_btn.configure(True, state='normal')
        self.process_btn.configure(True, state='normal')

    def display_preview(self):
        if not self.selected_file:
            print('no file selected')
            return

        supported_formats = ['MP4', 'AVI']

        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture(self.selected_file)

        # Check if camera opened successfully
        if (cap.isOpened() == False):
            print("Error opening video file")

        # Read until video is completed
        while (cap.isOpened()):

            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                # Display the resulting frame
                cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

        # Break the loop
            else:
                break

        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()

    def process_and_save(self, img_processor):

        if not self.selected_file:
            print('no file selected')
            return

        processor = img_processor(self.selected_file)

        processor.process_frame()
