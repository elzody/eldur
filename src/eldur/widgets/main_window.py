from gi.repository import Gtk

from eldur.widgets.header_bar import HeaderBar


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        super().__init__()

        self.set_application(application)
        self.set_title("Eldur")
        self.set_titlebar(HeaderBar())
