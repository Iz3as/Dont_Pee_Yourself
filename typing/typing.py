import sys, time

def dur_type(str, dur=0.05):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(dur)
  sys.stdout.write("\n")
  sys.stdout.flush()

def laugh(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0)
  sys.stdout.write("HA")
  sys.stdout.flush()