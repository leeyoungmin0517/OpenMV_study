import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.HQVGA)
sensor.skip_frames(time=2000)

while True:
    img = sensor.snapshot()
    stats = img.get_statistics()
    mean_values = stats.mean()

    if isinstance(mean_values, tuple):
        l,a,b = mean_values
        print("Mean L:", l, "A:", a, "B:", b)

    else:
        print("mean() 결과가 int입니다. 현재 GRAYSCALE 모드일 수 있습니다.")

