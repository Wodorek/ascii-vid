import tkinter as tk
from tkinter import ttk


def create_interface():
    window = tk.Tk()
    window.geometry('800x600')
    window.title('Ascii converter')

    selectBtn = ttk.Button(window, text='Select Video')
    processBtn = ttk.Button(window, text='Process Video')
    saveBtn = ttk.Button(window, text='Save Video')

    selectBtn.pack(side='left')
    processBtn.pack(side='left')
    saveBtn.pack(side='left')

    return window
