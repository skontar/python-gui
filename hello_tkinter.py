#!/usr/bin/env python3

from tkinter import ttk
from tkinter import Tk, BOTH


class Main(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widgets + callbacks
        self.frame = ttk.Frame(self)
        self.button = ttk.Button(self.frame, text='Test', command=self.on_button)

        # Layout
        self.frame.pack(expand=True, fill=BOTH, padx=5, pady=5)
        self.button.pack(expand=True, fill=BOTH)

    def on_button(self):
        print('tkinter callback')


root = Main()
root.mainloop()
