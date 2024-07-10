#-------------------------------------------------------
#
#               ALTERNATE LED BLINKING
#               =======================
#
# This project connects two LEDs to GPIO 17 and GPIO 27
# of the Raspberry Pi 5. The program alternates blinking
# the LEDs every second.
#
# Program: alternate_blink.py
# Author : Biswadeep Roy
#--------------------------------------------------------
from gpiozero import LED
from time import sleep  # import the sleep function from time library

led1 = LED(17)  # initialize LED1 at GPIO pin 17
led2 = LED(27)  # initialize LED2 at GPIO pin 27

while True:
    led1.on()  # turn ON LED1
    led2.off()  # turn OFF LED2
    sleep(1)  # wait for 1 second
    led1.off()  # turn OFF LED1
    led2.on()  # turn ON LED2
    sleep(1)  # wait for 1 second
