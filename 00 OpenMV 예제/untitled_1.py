# Untitled - By: user - Tue Jul 29 2025

import time
from machine import LED

led = LED(1)  # 1: RED, 2: GREEN, 3: BLUE (보드에 따라 다름)

while True:
    led.on()
    time.sleep_ms(1000)
    led.off()
    time.sleep_ms(1000)
