# Untitled - By: user - Tue Jul 29 2025

import sensor
import time

sensor.reset()
sensor.set_pixformat(sensor.JPEG)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

# 이미지 캡처 및 저장
img = sensor.snapshot()                 # JPEG 이미지 캡처
img.save("/test.jpg")                   # SD카드에 JPEG 저장
