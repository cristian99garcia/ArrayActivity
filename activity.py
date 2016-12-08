#!/usr/bin/python
# -*- coding: utf-8 -*-

from canvas import Canvas

import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toolbarbox import ToolbarBox

from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.activity import activity


class ArrayActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.canvas = Canvas(True)
        self.set_canvas(self.canvas)

        self.label_size = Gtk.Label("Width: 0\nHeight: 0")
        self.label_sum = Gtk.Label("")

        self.make_toolbar()

        self.show_all()

    def make_toolbar(self):
        def make_separator(expand=True):
            separator = Gtk.SeparatorToolItem()
            separator.props.draw = not expand
            separator.set_expand(expand)
            return separator

        toolbarbox = ToolbarBox()
        toolbarbox.toolbar.insert(ActivityToolbarButton(self), -1)

        toolbarbox.toolbar.insert(make_separator(False), -1)

        row_button = ToolButton("add-row")
        row_button.connect("clicked", self._on_add_row)
        toolbarbox.toolbar.insert(row_button, -1)

        column_button = ToolButton("add-column")
        column_button.connect("clicked", self._on_add_column)
        toolbarbox.toolbar.insert(column_button, -1)

        item = Gtk.ToolItem()
        item.add(self.label_size)
        toolbarbox.toolbar.insert(item, -1)

        toolbarbox.toolbar.insert(make_separator(False), -1)

        sum_button = ToolButton("list-add")
        sum_button.connect("clicked", self._on_sum)
        toolbarbox.toolbar.insert(sum_button, -1)

        item = Gtk.ToolItem()
        item.add(self.label_sum)
        toolbarbox.toolbar.insert(item, -1)

        toolbarbox.toolbar.insert(make_separator(True), -1)

        stop_button = StopButton(self)
        stop_button.props.accelerator = '<Ctrl>Q'
        toolbarbox.toolbar.insert(stop_button, -1)

        toolbarbox.toolbar.show_all()
        self.set_toolbar_box(toolbarbox)

    def _on_add_row(self, widget):
        self.canvas.add_row()
        self.update_label_size()
        self.label_sum.set_label("")

    def _on_add_column(self, widget):
        self.canvas.add_column()
        self.update_label_size()
        self.label_sum.set_label("")

    def _on_sum(self, widget):
        self.label_sum.set_label(str(sum(self.canvas.get_simple_value_list())))

    def update_label_size(self):
        size = tuple(self.canvas.get_size())
        self.label_size.set_label("Width: %d\nHeight: %d" % size)
