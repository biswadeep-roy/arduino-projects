/*================================================
      ARDUINO UNO - RASPBERRY PI 5
      ============================

In this project, a button is connected to Arduino Uno
pin 2. An HC-06 Bluetooth module is connected to pin 3.
The program sends the command "1" over Bluetooth when
the button is pressed.

Author: Biswadeep Roy
File  : arduino_rpi_bluetooth
==================================================*/
#include <SoftwareSerial.h>
SoftwareSerial mySerial(4, 3);        // rx, tx

int buttonPin = 2;                    // Button connected to pin 2

void setup() 
{
  mySerial.begin(9600);               // Set baud rate for serial communication
  pinMode(buttonPin, INPUT);          // Configure button pin as input
}

// Main program loop
void loop() 
{
  while (digitalRead(buttonPin) == 1);   // Wait while button is not pressed
  while (digitalRead(buttonPin) == 0);   // Wait while button is pressed
  mySerial.print("1");                   // Send "1" via Bluetooth
  delay(1000);                           // Delay for debouncing
}
