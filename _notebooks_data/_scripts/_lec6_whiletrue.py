import time
import sys

try:
    i = 0
    while True:
        print(f"This is my {i}th iteration, now Im going to sleep")
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print("Endless cycle was interrupted")
    sys.exit(1)