import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gio, GLib, Gtk
from eldur import MainWindow


class Eldur(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="dev.elzody.Eldur")
        GLib.set_application_name("Eldur")

        self.settings = Gio.Settings(schema_id="dev.elzody.Eldur")

    def do_activate(self):
        window = MainWindow(application=self)

        self.settings.bind(
            "window-width", window, "default-width", Gio.SettingsBindFlags.DEFAULT
        )

        self.settings.bind(
            "window-height", window, "default-height", Gio.SettingsBindFlags.DEFAULT
        )

        window.present()


def main():
    app = Eldur()

    app.run()
