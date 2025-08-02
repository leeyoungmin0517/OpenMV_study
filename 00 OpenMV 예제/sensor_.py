# Untitled - By: user - Sat Jul 19 2025

import sensor
import time

sensor.reset()
sensor.set_pixformat(sensor.RGB565) # 이미지 포맷 설정 : RGB565
sensor.set_framesize(sensor.QVGA)   # 프레임 크기 설정: 320x240
sensor.skip_frames(time=2000)       # 카메라 안정화 대기 시간 (2초)

clock = time.clock()                # FPS 계산용 시계

while True:
    clock.tick()
    img = sensor.snapshot()         # 이미지 캡쳐

    print(clock.fps())              # 현재 이미지 출력
