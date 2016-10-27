#!/usr/bin/env python3

from threading import Thread
from time import sleep

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, GObject


class Window(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_border_width(5)
        self.set_title('PyGObject')
        self.worker_thread = None

        # Widgets
        self.button_start = Gtk.Button('Start', expand=True)
        self.button_stop = Gtk.Button('Stop', expand=True, sensitive=False)
        self.progress = Gtk.ProgressBar()
        self.status_icon = Gtk.StatusIcon(file='star.ico')

        self.menu = Gtk.Menu()
        close = Gtk.ImageMenuItem(Gtk.STOCK_QUIT, use_stock=True)
        close.connect('activate', self.on_close, None)
        self.menu.append(close)

        # Layout
        self.grid = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL, row_spacing=5)
        self.grid.add(self.button_start)
        self.grid.add(self.button_stop)
        self.grid.add(self.progress)
        self.add(self.grid)

        # Callbacks
        self.button_start.connect('clicked', self.on_button_start)
        self.button_stop.connect('clicked', self.on_button_stop)
        self.status_icon.connect('popup-menu', self.on_menu)
        self.connect('delete-event', self.on_close)

        self.show_all()

    def on_button_start(self, button):
        self.button_start.set_sensitive(False)
        self.button_stop.set_sensitive(True)
        self.worker_thread = Thread(target=self.worker)
        self.worker_thread.should_close = False
        self.worker_thread.start()

    def on_button_stop(self, button):
        self.worker_thread.should_close = True

    def on_menu(self, sender, button, time):
        self.menu.show_all()
        self.menu.popup(None, None, Gtk.StatusIcon.position_menu, sender, button, time)

    def on_close(self, widget, event):
        if self.worker_thread is not None:
            self.worker_thread.should_close = True
            self.worker_thread.join()
        Gtk.main_quit()

    def worker(self):
        for i in range(101):
            if self.worker_thread.should_close:
                break
            GLib.idle_add(self.progress.set_fraction, i / 100)
            sleep(0.05)
        GLib.idle_add(self.button_start.set_sensitive, True)
        GLib.idle_add(self.button_stop.set_sensitive, False)

print('PyGObject', '.'.join(str(a) for a in GObject.pygobject_version))
print('GTK', '{}.{}.{}'.format(Gtk.MAJOR_VERSION, Gtk.MINOR_VERSION, Gtk.MICRO_VERSION))
win = Window()
Gtk.main()
