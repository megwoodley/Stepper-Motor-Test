from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger = 23)

try:
    with open("/home/elec490uav/Desktop/ELEC490UAV/distance_log.txt", "a") as logfile:
        while True:
            distance_cm = sensor.distance * 100
            log_entry = f"{distance_cm:.2f}cm"
            print(log_entry)
            logfile.write(log_entry + " ")
            logfile.flush()
            sleep(1)
except KeyboardInterrupt:
      print('Cleanup')