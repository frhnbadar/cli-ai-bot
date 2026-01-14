import time
import sys

def stream_text(text, delay=0.03):
    for word in text.split():
        sys.stdout.write(word + " ")
        sys.stdout.flush()
        time.sleep(delay)
    print()
