#!/usr/bin/env python3

from threading import Thread
import time
from tkinter import Tk, BOTH, DISABLED, NORMAL, TkVersion, TclVersion, N, S, W, E
from tkinter import ttk


class Main(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Tkinter')
        self.worker_thread = None

        # Widgets
        self.frame = ttk.Frame(self)
        self.button_start = ttk.Button(self.frame, text='Start', command=self.on_button_start)
        self.button_stop = ttk.Button(self.frame, text='Stop', command=self.on_button_stop)
        self.button_stop.config(state=DISABLED)
        self.progress = ttk.Progressbar(self.frame, length=200)

        # Layout
        self.frame.pack(expand=True, fill=BOTH, padx=5, pady=5)
        self.button_start.grid(row=0, column=0, sticky=(N, S, E, W), padx=5, pady=5)
        self.button_stop.grid(row=1, column=0, sticky=(N, S, E, W), padx=5, pady=5)
        self.progress.grid(row=2, column=0, sticky=(N, S, E, W), padx=5, pady=5)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)

        # Callbacks
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

    def worker(self):
        for i in range(101):
            if self.worker_thread.should_close:
                break
            self.after(0, self.update_progress, i)
            time.sleep(0.05)
        self.after(0, self.button_start.config, {'state': NORMAL})
        self.after(0, self.button_stop.config, {'state': DISABLED})

    def update_progress(self, value):
        self.progress['value'] = value

    def on_button_start(self):
        self.worker_thread = Thread(target=self.worker)
        self.worker_thread.should_close = False
        self.worker_thread.start()
        self.button_start.config(state=DISABLED)
        self.button_stop.config(state=NORMAL)

    def on_button_stop(self):
        self.worker_thread.should_close = True

    def on_closing(self):
        if self.worker_thread is not None:
            self.worker_thread.should_close = True
            self.worker_thread.join()
        self.destroy()


print('Tk', TkVersion)
print('Tcl', TclVersion)
root = Main()
# root.style = ttk.Style()
# print(root.style.theme_names())
# root.style.theme_use("clam")
root.mainloop()
