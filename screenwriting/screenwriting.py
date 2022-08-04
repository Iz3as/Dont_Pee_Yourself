import sys
import time


def dur_type(txt, dur=0.05):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dur)
    sys.stdout.write("\n")
    sys.stdout.flush()


def laugh(txt):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
    sys.stdout.write("HA")
    sys.stdout.flush()
