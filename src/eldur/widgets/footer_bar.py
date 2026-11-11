from gi.repository import Gtk

from eldur.widgets.play_button import PlayButton


class FooterBar(Gtk.CenterBox):
    def __init__(self):
        super().__init__()

        self.set_margin_top(4)
        self.set_margin_bottom(4)
        self.set_margin_start(4)
        self.set_margin_end(4)

        self.set_end_widget(PlayButton())
