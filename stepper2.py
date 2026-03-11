# GPIO pins (BCM mode) - sysfs method (no RPi.GPIO library needed)
STEP_PIN = 17
DIR_PIN = 18
ENABLE_PIN = 27
MICROSTEPS = 1

# Motor params
STEPS_PER_REV_MOTOR = 200
GEAR_MOTOR_TO_OUTPUT = 21 / 64
STEPS_PER_OUTPUT_REV = STEPS_PER_REV_MOTOR / GEAR_MOTOR_TO_OUTPUT

# Setup GPIO using sysfs (works on all Pi models)
def gpio_export(pin):
    with open(f'/sys/class/gpio/export', 'w') as f:
        f.write(str(pin))

def gpio_direction(pin, direction):
    with open(f'/sys/class/gpio/gpio{pin}/direction', 'w') as f:
        f.write(direction)

def gpio_write(pin, value):
    with open(f'/sys/class/gpio/gpio{pin}/value', 'w') as f:
        f.write(str(value))

# Initialize pins
gpio_export(STEP_PIN)
gpio_export(DIR_PIN)
gpio_export(ENABLE_PIN)
gpio_direction(STEP_PIN, 'out')
gpio_direction(DIR_PIN, 'out')
gpio_direction(ENABLE_PIN, 'out')
gpio_write(ENABLE_PIN, 0)  # Enable driver

def move_degrees(degrees, speed_delay=0.005):
    steps = int(abs(degrees) / 360 * STEPS_PER_OUTPUT_REV * MICROSTEPS)
    direction = 1 if degrees > 0 else 0
    gpio_write(DIR_PIN, direction)
    for _ in range(steps):
        gpio_write(STEP_PIN, 1)
        time.sleep(speed_delay)
        gpio_write(STEP_PIN, 0)
        time.sleep(speed_delay)

print("Starting sequence...")
move_degrees(30)
time.sleep(0.5)
move_degrees(-30)
time.sleep(0.5)
move_degrees(-30)

gpio_write(ENABLE_PIN, 1)  # Disable driver

# Cleanup
with open('/sys/class/gpio/unexport', 'w') as f:
    f.write(str(STEP_PIN))
with open('/sys/class/gpio/unexport', 'w') as f:
    f.write(str(DIR_PIN))
with open('/sys/class/gpio/unexport', 'w') as f:
    f.write(str(ENABLE_PIN))

print("Done.")
