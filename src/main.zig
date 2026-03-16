const std = @import("std");

const gtk = @cImport({
    @cInclude("gtk/gtk.h");
});

pub fn main() !u8 {
    var gpa: std.heap.DebugAllocator(.{}) = .init;
    const allocator = gpa.allocator();
    defer _ = gpa.deinit();

    const args = try std.process.argsAlloc(allocator);
    defer std.process.argsFree(allocator, args);

    const app: *gtk.GtkApplication = gtk.gtk_application_new("dev.elzody.eldur", gtk.G_APPLICATION_DEFAULT_FLAGS);
    defer gtk.g_object_unref(app);

    const status = gtk.g_application_run(@ptrCast(app), @intCast(args.len), @ptrCast(args));

    return @intCast(status);
}
