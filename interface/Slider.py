import customtkinter as ctk


class Slider(ctk.CTkFrame):
    def __init__(self, master, text, color):
        super().__init__(master)
        self.master = master

        self._fg_color = color
        self._bg_color = color

        label = ctk.CTkLabel(master=self, text=text,)
        slider = ctk.CTkSlider(master=self)

        label.grid(row=0, column=0, sticky='nswe')
        slider.grid(row=1, column=0, sticky='nswe')
