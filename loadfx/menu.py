import os

class Menu:
    def __init__(self, items, title="Menu", prompt="Select", numbered=True, clear=False, allow_quit=True, quit_value=None):
        self.items=items; self.title=title; self.prompt=prompt; self.numbered=numbered
        self.clear=clear; self.allow_quit=allow_quit; self.quit_value=quit_value

    def _normalize(self, data):
        if isinstance(data, dict):
            return [(str(k), v) for k, v in data.items()]
        if isinstance(data, (list, tuple)):
            out=[]
            for item in data:
                out.extend(self._normalize(item) if isinstance(item, dict) else [(str(item), item)])
            return out
        raise TypeError("Menu expects a list, tuple, or dictionary.")

    def _choose(self, items):
        while True:
            if self.clear: os.system("cls" if os.name == "nt" else "clear")
            print(f"\n=== {self.title} ===\n")
            for i, (label, _) in enumerate(items, 1):
                print((f"{i}. " if self.numbered else "- ") + label)
            if self.allow_quit: print("q. Quit")
            answer=input(f"\n{self.prompt}: ").strip()
            if self.allow_quit and answer.lower() in {"q", "quit", "exit"}: return self.quit_value
            if answer.isdigit() and 0 < int(answer) <= len(items): return items[int(answer)-1][1]
            print("Invalid selection. Please try again.")

    def show(self):
        return self._show(self.items)

    def _show(self, data):
        if isinstance(data, dict) and any(isinstance(v, dict) for v in data.values()):
            items=list(data.items())
            while True:
                selected=self._choose([(str(k), v) for k, v in items])
                if selected is self.quit_value: return selected
                if isinstance(selected, dict):
                    result=self._show(selected)
                    if result is not self.quit_value: return result
                else: return selected
        if isinstance(data, dict): return self._choose(self._normalize(data))
        if isinstance(data, (list, tuple)): return self._choose(self._normalize(data))
        raise TypeError("Menu expects a list, tuple, or dictionary.")
