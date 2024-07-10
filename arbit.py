#-----------------------------------------------------------------
#                GENERATE CUSTOM WAVEFORM
#                =========================
#
# This program generates a custom waveform based on predefined
# sample points in the code.
#
# Author: Biswadeep Roy
# File  : custom_waveform.py
#-------------------------------------------------------------------
from gpiozero import LED
from time import sleep  # Import sleep function from time module
import spidev  # Import spidev module for SPI communication

spi = spidev.SpiDev()
spi.open(0, 0)  # Initialize SPI on bus 0, device 0
spi.max_speed_hz = 3900000

CS = LED(26)  # GPIO26 is the Chip Select (CS) output
CS.on()  # Disable CS initially
sample = 0

# Waveform sample points
wave = [0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3, 3, 3, 3, 3,
        2.625, 2.25, 1.875, 1.5, 1.125, 0.75, 0.375, 0]

# Function to send data to the DAC
def DAC(data):
    CS.off()  # Enable CS
    temp = (data >> 8) & 0x0F  # Extract the upper byte
    temp = temp + 0x30  # Combine with 0x30
    spi.xfer2([temp])  # Send the upper byte to the DAC

    temp = data & 0xFF
    spi.xfer2([temp])  # Send the lower byte to the DAC

    CS.on()  # Disable CS

try:
    while True:
        DACValue = int(wave[sample] * 4095 / 3.3)  # Calculate DAC value
        DAC(DACValue)  # Send value to the DAC
        sample = sample + 1  # Increment sample index
        sleep(0.0008)  # Wait briefly
        if sample == 20:  # Reset index if end of samples reached
            sample = 0

except KeyboardInterrupt:
    pass
