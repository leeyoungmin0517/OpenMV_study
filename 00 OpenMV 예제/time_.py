# Untitled - By: user - Mon Jul 21 2025

import sensor, image, time

# 센서 초기화
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

# 시간 측정용 clock 객체 생성
clock = time.clock()

while(True):
    clock.tick()  # 새로운 프레임 측정 시작

    img = sensor.snapshot()  # 이미지 캡처

    # 원 그리기 (중앙에 반지름 30인 원)
    img.draw_circle(160, 120, 30, color=(255, 0, 0))

    # 프레임 속도 출력
    print("FPS: ", clock.fps())

    # 100ms 대기 (0.1초)
    time.sleep(100)
