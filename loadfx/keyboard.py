"""Minimal cross-platform keyboard callback registry."""
import threading

_handlers = {}

class Keyboard:
    def on(self, key, handler):
        _handlers[str(key).upper()] = handler
        return self

    def off(self, key):
        _handlers.pop(str(key).upper(), None); return self

    def trigger(self, key, *args, **kwargs):
        handler = _handlers.get(str(key).upper())
        return handler(*args, **kwargs) if handler else None

    def clear(self):
        _handlers.clear(); return self

keyboard = Keyboard()
