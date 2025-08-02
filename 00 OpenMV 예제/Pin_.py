# Untitled - By: user - Mon Jul 21 2025

import time
from machine import LED

led = LED("LED_BLUE")


while True:
    led.on()
    time.sleep_ms(5)
    led.off()
    time.sleep_ms(10)
