from machine import Pin
import time
LEDPIN = Pin(25, Pin.OUT)

while True:
    LEDPIN.on()
    time.sleep(1)
    LEDPIN.off()