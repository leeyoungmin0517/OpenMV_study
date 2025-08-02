# Untitled - By: user - Sat Jul 19 2025

import sensor
import time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

clock = time.clock()

while (True):
    clock.tick()
    img = sensor.snapshot()                    # image.Image 객체

    blobs = img.find_blobs([200, 255])         # 밝기 범위가 200~225인 밝은 영역(블롭)을 탐지

    for blob in blobs :                        # 중심좌표 가죠오기
        cx = blob.cx()
        cy = blobs.cy()
        img.                            # 중심에 원 그리기
        img.draw_circle(cx, cy, 10, color=225) # 반지름이 10, 흰색 원
        img.set_pixel(cx, cy, 100)             # 중심점에 픽셀을 지정된 색상으로 변경(여기선 어두운 회색 100)

        print("Blob at:" , cx, cy)
    print(clock.fps())
