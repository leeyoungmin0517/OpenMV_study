import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time=2000)

clock = time.clock()

while True:
    clock.tick()
    img = sensor.snapshot()

    x = 100
    y = 60

    # set_pixel은 RGB565 값 (정수) 사용
    img.set_pixel(x, y, 0xF800)  # 빨강

    # draw_cross는 (R, G, B) 튜플 사용
    img.draw_cross(x, y, color=(255, 0, 0))

    print("Pixel set at:", x, y)
