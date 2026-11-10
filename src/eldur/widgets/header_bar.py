from gi.repository import Gtk


class HeaderBar(Gtk.HeaderBar):
    def __init__(self):
        super().__init__()

        self.set_decoration_layout("icon:minimize,close")
