# RPi_MPU6050
This is a simple MPU_6050 library for RPi

Tested on Arch Linux

To connect the sensor you need to use the GPIO pins on the Pi, the important pins are
 * Pin 1 - 3.3V connect to VCC
 * Pin 3 - SDA connect to SDA
 * Pin 5 - SCL connect to SCL
 * Pin 6 - Ground connect to GND

You will need the following packages:
 * i2c-tools (for detect connected I2C devices)
 * python-smbus

Visit http://blog.bitify.co.uk/2013/11/interfacing-raspberry-pi-and-mpu-6050.html to see how to get addresses!

My classes based on Andrew Birkett's article.

http://blog.bitify.co.uk/2013/11/reading-data-from-mpu-6050-on-raspberry.html
__So long and thanks for all the fish!__
