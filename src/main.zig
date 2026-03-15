const gtk = @cImport({
    @cInclude("gtk/gtk.h");
});

pub fn main() void {
    gtk.g_print("Hello GTK!\n");
}
