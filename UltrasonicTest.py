from gpiozero import DistanceSensor
from time import sleep

# Sensor 1: original pins
sensor1 = DistanceSensor(echo=24, trigger=23)

# Sensor 2: new pins (avoid conflicts; e.g., GPIO 25 echo, 8 trigger - check your wiring)
sensor2 = DistanceSensor(echo=25, trigger=8)

try:
    with open("/home/elec490uav/Desktop/ELEC490UAV/distance_log.txt", "a") as logfile:
        while True:
            dist1_cm = sensor1.distance * 100
            dist2_cm = sensor2.distance * 100
            log_entry = f"S1:{dist1_cm:.2f}cm S2:{dist2_cm:.2f}cm"
            print(log_entry)
            logfile.write(log_entry + " ")
            logfile.flush()
            sleep(1)
except KeyboardInterrupt:
    print('Cleanup')
