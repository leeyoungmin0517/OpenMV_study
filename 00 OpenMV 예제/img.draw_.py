import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)     # 컬러 모드
sensor.set_framesize(sensor.QVGA)       # 해상도 설정
sensor.skip_frames(time=2000)
clock = time.clock()

# 선명한 녹색 추적을 위한 LAB 기준 임계값
green_threshold = (20, 60, -70, -20, -20, 20)

while(True):
    clock.tick()
    img = sensor.snapshot()

    # 녹색 blob 찾기
    blobs = img.find_blobs([green_threshold], pixels_threshold=200, area_threshold=200)

    for blob in blobs:
        # 사각형 표시
        img.draw_rectangle(blob.rect(), color=(0, 255, 0))  # 녹색 사각형
        # 중심점 십자선
        img.draw_cross(blob.cx(), blob.cy(), color=(0, 255, 0))
        # 텍스트 표시
        img.draw_string(blob.x(), blob.y() - 10, "GREEN!", mono_space=False, color=(0, 255, 0))

    print("FPS:", clock.fps())
