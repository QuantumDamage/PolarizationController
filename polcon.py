import dbus

qkd_bus = dbus.bus.BusConnection("tcp:host=localhost,port=6666")
