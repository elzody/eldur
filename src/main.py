import gi

gi.require_version("Gtk", "4.0")

from gi.repository import GLib, Gtk


class Eldur(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="dev.elzody.eldur")
        GLib.set_application_name("Eldur")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Eldur")
        window.present()


def main():
    app = Eldur()

    app.run()


if __name__ == "__main__":
    main()
