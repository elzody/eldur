// SPDX-License-Identifier: AGPL-3.0

const std = @import("std");

const gtk = @cImport({
    @cInclude("gtk/gtk.h");
});

fn activate(app: ?*gtk.GtkApplication, user_data: ?*anyopaque) callconv(.c) void {
    const window: *gtk.GtkWidget = gtk.gtk_application_window_new(@ptrCast(app));

    gtk.gtk_window_present(@ptrCast(window));

    _ = user_data;
}

pub fn main() !u8 {
    var gpa: std.heap.DebugAllocator(.{}) = .init;
    const allocator = gpa.allocator();
    defer _ = gpa.deinit();

    const args = try std.process.argsAlloc(allocator);
    defer std.process.argsFree(allocator, args);

    const app: *gtk.GtkApplication = gtk.gtk_application_new("dev.elzody.eldur", gtk.G_APPLICATION_DEFAULT_FLAGS);
    defer gtk.g_object_unref(app);

    _ = gtk.g_signal_connect_data(app, "activate", @ptrCast(&activate), null, null, 0);

    const status = gtk.g_application_run(@ptrCast(app), @intCast(args.len), @ptrCast(args));

    return @intCast(status);
}
