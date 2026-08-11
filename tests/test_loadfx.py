from loadfx import TextFX, Menu

def test_text():
    assert "hello" in TextFX.red("hello")

def test_menu_normalize():
    assert Menu(["A", "B"])._normalize(["A", "B"]) == [("A", "A"), ("B", "B")]
    assert Menu({"A": 1})._normalize({"A": 1}) == [("A", 1)]
