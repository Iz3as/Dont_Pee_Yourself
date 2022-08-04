from screenwriting import dur_type


def test_type(capsys):
    testtable = [
        ("pipis", 0.02, "pipis\n"),
        ("pipis\n\n\n\n\n", 0.01, "pipis\n\n\n\n\n\n"),
        ("V̸̗̣̍ö̵̥͑i̵͈̭͋͝d̵̠͔̚i̴̝͝n̸̹͘͝i̵̤̊ù̴̹̫̊s̊̚̕̕͝", 0.01, "V̸̗̣̍ö̵̥͑i̵͈̭͋͝d̵̠͔̚i̴̝͝n̸̹͘͝i̵̤̊ù̴̹̫̊s̊̚̕̕͝\n")
    ]
    for (inputstr, dur, expout) in testtable:
        dur_type(inputstr, dur)
        captured = capsys.readouterr()
        assert captured.out == expout
