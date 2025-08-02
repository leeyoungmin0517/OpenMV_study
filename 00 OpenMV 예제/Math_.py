# Untitled - By: user - Mon Jul 21 2025

import math
import time

while True:
    angle_deg = 30  # 30도
    angle_rad = math.radians(angle_deg)  # 라디안으로 변환

    sin_val = math.sin(angle_rad)  # sin(30도)
    root_val = math.sqrt(16)       # √16 = 4.0
    deg_back = math.degrees(angle_rad)  # 라디안 → 도로 다시 변환

    print("각도(deg):", angle_deg)
    print("각도(rad):", angle_rad)
    print("sin(30°):", sin_val)
    print("sqrt(16):", root_val)
    print("다시 변환된 각도(degrees):", deg_back)
    print("-----")

    time.sleep(1000)  # 1초 대기
