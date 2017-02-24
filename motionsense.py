# Fairly generic routine to start and stop shell scripts when motion detected.

#import libraries
from gpiozero import MotionSensor
from time import sleep
import time
import subprocess

#set sensor to GPIO pin 4 - alter if necessary
sensor = MotionSensor(4)

try:
    while True:
        sensor.wait_for_motion()
        print('Motion detected! Stream active.')
        subprocess.call("./startstream.sh")
        sleep(20) #keep stream active for 20 seconds

        sensor.wait_for_no_motion()
        print('No motion detected. Stream stopped.')
        subprocess.call("./stopstream.sh")

except:
    print('Ctrl-C pressed. Program ended.')

