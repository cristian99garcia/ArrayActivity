#!/usr/bin/env python
# -*- coding: utf-8 -*-

from table import Table

import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class CenterBox(Gtk.VBox):
    # A box with a centered child, with set_center_widget
    # the child don't auto-resize

    def __init__(self, child):
        Gtk.VBox.__init__(self)

        hbox = Gtk.HBox()
        hbox.pack_start(child, True, False, 0)
        self.pack_start(hbox, True, False, 0)



class Canvas(Gtk.VBox):

    def __init__(self, sugar=False):
        Gtk.VBox.__init__(self)

        self.values = []  # Start with a empty values list
        self.size = [0, 0]

        self.table = Table()

        box = CenterBox(self.table)

        scroll = Gtk.ScrolledWindow()
        scroll.add(box)

        self.pack_start(scroll, True, True, 0)

        if not sugar:
            self.pack_buttons()

    def pack_buttons(self):
        box = Gtk.HButtonBox()
        box.set_layout(Gtk.ButtonBoxStyle.CENTER)
        self.pack_end(box, False, False, 20)

        row_button = Gtk.Button.new_with_label("Add a row")
        row_button.connect("clicked", lambda button: self.add_row())
        box.add(row_button)

        column_button = Gtk.Button.new_with_label("Add a column")
        column_button.connect("clicked", lambda button: self.add_column())
        box.add(column_button)

    def add_column(self):
        self.table.add_column()
        self.show_all()

    def add_row(self):
        self.table.add_row()
        self.show_all()

    def get_values(self):
        return self.table.get_values()

    def get_size(self):
        return self.table.size


if __name__ == "__main__":
    win = Gtk.Window()
    win.set_title("Array adder")
    win.connect("destroy", Gtk.main_quit)

    canvas = Canvas()
    win.add(canvas)

    win.show_all()
    Gtk.main()
