from gi.repository import Gtk

from eldur.widgets.menu_button import MenuButton
from eldur.widgets.play_button import PlayButton


class HeaderBar(Gtk.HeaderBar):
    def __init__(self):
        super().__init__()

        self.pack_start(MenuButton())
        self.pack_start(PlayButton())
        self.set_decoration_layout("icon:minimize,close")
