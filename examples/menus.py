from loadfx import Menu

# Single list
print(Menu(["Home", "Projects", "Settings", "Exit"], "List Menu").show())

# Dictionary
print(Menu({"Python":"python", "JavaScript":"javascript", "C++":"cpp"}, "Dictionary Menu").show())

# Multiple dictionaries
print(Menu([{"Frontend":"frontend", "Backend":"backend"}, {"AI":"ai", "Cybersecurity":"cyber"}], "Multiple Dictionary Menu").show())

# Nested dictionary
print(Menu({"Programming":{"Python":"python", "JavaScript":"javascript"}, "Projects":{"New":"new", "Open":"open"}}, "Nested Menu").show())
