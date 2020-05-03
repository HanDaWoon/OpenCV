import numpy as np
import cv2

color = [255, 0, 0]    # BGR
pixel = np.uint8([[color]])    # 하나의 픽셀로 구성된 이미지로 변환

hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)    # HSV색공간으로 변환
hsv = hsv[0][0]    # 픽셀값

print("bgr: ", color)
print("hsv: ", hsv)
