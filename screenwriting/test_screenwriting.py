#!/usr/bin/env python
# coding: utf8
from screenwriting import dur_type


def test_dur_type(capsys):
    testtable = [
        ("pipis", 0.02, "\n", "pipis\n"),
        ("pipis\n\n\n\n\n", 0.01, "\n", "pipis\n\n\n\n\n\n"),
        (u"V̸̗̣̍ö̵̥͑i̵͈̭͋͝d̵̠͔̚i̴̝͝n̸̹͘͝i̵̤̊ù̴̹̫̊s̊̚̕̕͝", 0.01, "\n", u"V̸̗̣̍ö̵̥͑i̵͈̭͋͝d̵̠͔̚i̴̝͝n̸̹͘͝i̵̤̊ù̴̹̫̊s̊̚̕̕͝\n"),
        ("HA", 0, "heehee", "HAheehee"),
        (u"(A mysterious  e̴n̵t̸i̶t̸y̵  flies out.)", 0.2, "\n", u"(A mysterious  e̴n̵t̸i̶t̸y̵  flies out.)\n")
    ]
    for (inputstr, dur, endstr, expout) in testtable:
        dur_type(inputstr, dur, endstr)
        captured = capsys.readouterr()
        assert captured.out == expout

