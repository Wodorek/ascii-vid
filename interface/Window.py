import customtkinter as ctk
from PIL import Image


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('800x600')
        self.title('Ascii vid')
        self.resizable(False, False)

        self.columnconfigure((0, 1, 2, 3), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        slider_1 = ctk.CTkSlider(self, from_=0, to=100)
        slider_2 = ctk.CTkSlider(self, from_=0, to=100)
        slider_3 = ctk.CTkSlider(self, from_=0, to=100)

        slider_1.grid(row=1, column=0, columnspan=2)
        slider_2.grid(row=2, column=0, columnspan=2)
        slider_3.grid(row=3, column=0, columnspan=2)

        preview = Image.open('./sz.png')
        # preview.thumbnail((300, 300), Image.Resampling.LANCZOS)

        image = ctk.CTkImage(
            light_image=preview, size=(300, 300))

        label = ctk.CTkLabel(
            self, image=image, text='', )

        label.grid(row=1, column=2, columnspan=2, rowspan=4, sticky='nswe')

        buttons_frame = ctk.CTkFrame(master=self, fg_color=self._fg_color)
        buttons_frame.columnconfigure((0, 1, 2), weight=1)
        buttons_frame.rowconfigure((0, 1, 2), weight=1)
        buttons_frame.grid(row=6, column=0,
                           columnspan=4, sticky='nswe', )

        button_1 = ctk.CTkButton(master=buttons_frame, text="Open Video")
        button_2 = ctk.CTkButton(master=buttons_frame, text="Process Video")
        button_3 = ctk.CTkButton(master=buttons_frame, text="Save Video")

        button_1.grid(row=1, column=0,)
        button_2.grid(row=1, column=1,)
        button_3.grid(row=1, column=2,)
