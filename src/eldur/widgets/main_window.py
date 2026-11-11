from gi.repository import Gtk

from eldur.widgets.footer_bar import FooterBar
from eldur.widgets.header_bar import HeaderBar


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        super().__init__()

        self.set_application(application)
        self.set_title("Eldur")
        self.set_titlebar(HeaderBar())

        temp = Gtk.Label()
        temp.set_text("Content")
        temp.set_vexpand(True)

        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        box.append(temp)
        box.append(Gtk.Separator.new(Gtk.Orientation.HORIZONTAL))
        box.append(FooterBar())

        self.set_child(box)
