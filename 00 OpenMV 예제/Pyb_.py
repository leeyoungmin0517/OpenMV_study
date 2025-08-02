# Untitled - By: user - Mon Jul 21 2025

import pyb
import time

# OpenMV 보드에 있는 LED는 일반적으로 다음과 같습니다:
# LED(1): 빨간색, LED(2): 초록색, LED(3): 파란색

while True:
    # 빨간 LED ON
    pyb.LED(1).on()
    time.sleep(300)
    pyb.LED(1).off()

    # 초록 LED ON
    pyb.LED(2).on()
    time.sleep(300)
    pyb.LED(2).off()

    # 파란 LED ON
    pyb.LED(3).on()
    time.sleep(300)
    pyb.LED(3).off()
