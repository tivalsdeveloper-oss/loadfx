"""Plugin base class for extending loadfx."""

class Plugin:
    name = "plugin"
    def register(self):
        return None

    def unregister(self):
        return None
