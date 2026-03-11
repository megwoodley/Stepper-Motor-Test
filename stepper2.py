import pigpio
import time

pi = pigpio.pi()  # Connect to pigpiod daemon
if not pi.connected:
    exit("pigpiod not running")

DIR = 22
STEP = 23
ENABLE = 24

pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)
pi.set_mode(ENABLE, pigpio.OUTPUT)

pi.write(ENABLE, 0)  # Enable motor
pi.write(DIR, 1)     # Clockwise

steps = 200
pulse_width = 500    # Microseconds HIGH (adjust 100-1000)
delay = 0.005        # Total cycle time ~0.01s/step for 1s runtime

for _ in range(steps):
    pi.write(STEP, 1)
    time.sleep(delay / 2)
    pi.write(STEP, 0)
    time.sleep(delay / 2)

pi.write(ENABLE, 1)  # Disable
pi.stop()            # Cleanup
