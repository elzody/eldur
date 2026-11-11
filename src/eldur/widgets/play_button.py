from gi.repository import Gtk


class PlayButton(Gtk.Button):
    def __init__(self):
        super().__init__()

        self.set_label("Play")
        self.add_css_class("suggested-action")
