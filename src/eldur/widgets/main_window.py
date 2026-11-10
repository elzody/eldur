from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        super().__init__()

        self.set_application(application)
        self.set_title("Eldur")
