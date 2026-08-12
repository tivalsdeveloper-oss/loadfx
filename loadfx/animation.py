import random, string, sys, time
from .colors import CLEAR_LINE

class Animation:
    @staticmethod
    def typewriter(text, speed=.04, stream=None):
        stream=stream or sys.stdout
        for ch in str(text): stream.write(ch); stream.flush(); time.sleep(speed)
        stream.write("\n"); return text

    @staticmethod
    def slide(text, steps=10, delay=.03, stream=None):
        stream=stream or sys.stdout
        for i in range(steps+1): stream.write(CLEAR_LINE+"\r"+" "*i+str(text)); stream.flush(); time.sleep(delay)
        stream.write("\n"); return text

    @staticmethod
    def glitch(text, passes=5, delay=.05, stream=None):
        stream=stream or sys.stdout; original=str(text)
        for _ in range(passes):
            noisy="".join(random.choice(string.ascii_letters+"!@#$%") if random.random()<.25 else c for c in original)
            stream.write(CLEAR_LINE+"\r"+noisy); stream.flush(); time.sleep(delay)
        stream.write(CLEAR_LINE+"\r"+original+"\n"); return original

    @staticmethod
    def fade_in(text, steps=5, delay=.08, stream=None):
        stream=stream or sys.stdout
        text=str(text)
        for i in range(1, steps+1):
            stream.write(CLEAR_LINE+"\r"+text[:max(1, int(len(text)*i/steps))]); stream.flush(); time.sleep(delay)
        stream.write("\n"); return text

    @staticmethod
    def save(animation, path):
        import json
        data = animation if isinstance(animation, dict) else {"type": "animation", "value": str(animation)}
        with open(path, "w", encoding="utf-8") as f: json.dump(data, f, indent=2)
        return path

    def __init__(self, text=None, effect="typewriter", **kwargs):
        self.text=text; self.effect=effect; self.options=kwargs

    def export(self, path):
        return self.save({"text": self.text, "effect": self.effect, "options": self.options}, path)
