import sys
import time
import pynput

mouse = pynput.mouse.Controller()

clicks_amount = int(sys.argv[1])

time.sleep(10)
for _ in range(clicks_amount):
    mouse.click(pynput.mouse.Button.left)
    time.sleep(0.1)
