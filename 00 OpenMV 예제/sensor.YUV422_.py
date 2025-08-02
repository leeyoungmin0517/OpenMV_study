import sensor, image, time

# 카메라 설정
sensor.reset()
sensor.set_pixformat(sensor.YUV422)  # YUV422 포맷 설정
sensor.set_framesize(sensor.QVGA)    # 해상도 설정
sensor.skip_frames(time=2000)        # 초기화 대기

clock = time.clock()

while True:
    clock.tick()
    img = sensor.snapshot()  # 이미지 캡처

    # 특정 좌표의 픽셀 값(YUV 값)을 가져옴
    x, y = 160, 120  # 이미지 중앙
    yuv_pixel = img.get_pixel(x, y)
    print("Pixel at ({}, {}): YUV = {}".format(x, y, yuv_pixel))

    # 디버깅용 FPS 출력
    print("FPS:", clock.fps())
