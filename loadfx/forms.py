"""Simple zero-dependency terminal forms."""

class Form:
    def __init__(self, title="Form", prompt=": "):
        self.title = str(title)
        self.prompt = prompt
        self.fields = []

    def input(self, name, default="", required=False):
        self.fields.append((str(name), "input", default, required)); return self

    def password(self, name, default="", required=False):
        self.fields.append((str(name), "password", default, required)); return self

    def show(self):
        import getpass
        print(f"\n=== {self.title} ===")
        result = {}
        for name, kind, default, required in self.fields:
            while True:
                suffix = f" [{default}]" if default else ""
                value = getpass.getpass(f"{name}{suffix}{self.prompt}") if kind == "password" else input(f"{name}{suffix}{self.prompt}")
                if not value and default: value = default
                if value or not required: break
                print("This field is required.")
            result[name] = value
        return result
