from typing import dur_type


def test_type(capsys):
    dur_type("pipis", 0.02)
    captured = capsys.readouterr()
    assert captured.out == "pipis\n"
