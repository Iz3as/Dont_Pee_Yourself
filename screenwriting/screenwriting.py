import sys
import time


def dur_type(txt, dur=0.05, endstr="\n"):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dur)
    sys.stdout.write(endstr)
    sys.stdout.flush()



