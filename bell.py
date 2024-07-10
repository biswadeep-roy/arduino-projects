#------------------------------------------------------------------
#
#                WHO IS AT MY DOOR
#                =================
#
# This program uses a camera, a pushbutton switch, and a relay 
# connected to a Raspberry Pi 5. The camera is positioned outside 
# the door to capture an image of who is outside. Pressing the 
# button activates the relay for 5 seconds, then takes a picture 
# and sends it to a smartphone via Bluetooth.
#
# Program: doorbell.py
# Author : Biswadeep Roy
#--------------------------------------------------------------------
from gpiozero import LED, Button
from time import sleep  # Import sleep function from time library
import os

button = Button(20)  # Button connected to GPIO pin 20
relay = LED(21)  # Relay connected to GPIO pin 21
relay.off()

while True:
    sleep(1)
    if button.is_pressed:  # Check if the button is pressed
        relay.on()  # Turn on the relay for 5 seconds
        sleep(5)
        relay.off()
        os.system("obexftp --nopath --uuid none --noconn --bluetooth 50:50:A4:0F:62:3F --channel 12 -p door.jpg")
    else:
        relay.off()
