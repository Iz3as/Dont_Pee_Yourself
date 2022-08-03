import pytest
from typing.typing import dur_type, laugh

def test_type(capsys):
    dur_type("pipis", 0.02)
    captured = capsys.readouterr()
    assert captured.out == "pipis\n"