import customtkinter as ctk
from src.Video_Processor import VideoProcessor
# from interface.Slider import Slider


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        # main window config
        self.geometry('800x600')
        self.title('Ascii vid')
        self.resizable(False, False)
        self.columnconfigure((0, 1, 2, 3), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.select_btn = None
        self.process_btn = None
        self.video_processor = VideoProcessor()

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
        buttons_frame.grid(row=6, column=0, columnspan=4, sticky='nswe')

        button_1 = ctk.CTkButton(buttons_frame,
                                 text="Open Video", command=self.select_file)
        button_2 = ctk.CTkButton(buttons_frame,
                                 text="Preview Frame", command=self.display_preview, state='disabled')
        self.select_btn = button_2
        button_3 = ctk.CTkButton(buttons_frame,
                                 text="Save Video", command=self.process_and_save)
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

        self.video_processor.select_video(file)

        self.select_btn.configure(True, state='normal')
        self.process_btn.configure(True, state='normal')

    def display_preview(self):

        self.video_processor.show_video()
        supported_formats = ['MP4', 'AVI']

    def process_and_save(self):

        if not self.selected_file:
            print('no file selected')
            return
