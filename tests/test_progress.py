import io

from loadfx import MultiProgress, ProgressBar, track


def test_progress_updates_in_place():
    out = io.StringIO()
    bar = ProgressBar(10, stream=out)
    bar.update(1)
    bar.update(10)
    value = out.getvalue()
    assert "Progress" in value
    assert "100.00%" in value
    assert value.count("\n") == 1


def test_progress_styles():
    for style in ["classic", "blocks", "dots", "dotline", "small-dots", "arrows", "squares", "circles", "braille", "pulse", "bars", "hash", "equals", "stars"]:
        bar = ProgressBar(10, stream=io.StringIO(), style=style)
        bar.update(5)


def test_step_update():
    out = io.StringIO()
    bar = ProgressBar(10, stream=out)
    bar.update(step=5)
    assert bar.current == 5


def test_track():
    out = io.StringIO()
    values = list(track([1, 2, 3], stream=out))
    assert values == [1, 2, 3]


def test_multi_progress_creation():
    out = io.StringIO()
    multi = MultiProgress(stream=out)
    first = multi.add("Download", 10)
    second = multi.add("Install", 10)
    first.update(5)
    second.update(7)
    assert len(multi.bars) == 2
