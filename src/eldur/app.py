from gi.repository import Gio, GLib, Gtk

from eldur.widgets import MainWindow


class Eldur(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="dev.elzody.Eldur")
        GLib.set_application_name("Eldur")

        self.settings = Gio.Settings(schema_id="dev.elzody.Eldur")

    def do_activate(self):
        window = MainWindow(application=self)
        window.present()


def main():
    app = Eldur()

    app.run()
