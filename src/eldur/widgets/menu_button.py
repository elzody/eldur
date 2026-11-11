from gi.repository import Gtk


class MenuButton(Gtk.MenuButton):
    def __init__(self):
        super().__init__()

        self.set_icon_name("open-menu-symbolic")
        self.set_primary(True)
