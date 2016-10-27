#!/usr/bin/env python3

from gi.repository import Gtk


class Window(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_border_width(5)

        # Widgets
        self.button = Gtk.Button('Test')

        # Layout
        self.box = Gtk.Box()
        self.box.pack_start(self.button, True, True, 0)
        self.add(self.box)

        # Callbacks
        self.connect('delete-event', Gtk.main_quit)
        self.button.connect('clicked', self.on_button)

        self.show_all()

    def on_button(self, button):
        print('PyGObject callback')


win = Window()
Gtk.main()
