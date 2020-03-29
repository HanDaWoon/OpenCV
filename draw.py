import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)    #numpy.zeros 를 이용하여 값이 0인 배열을 만든다 (X, Y, 맴버) 채우는 데이터 타입 uint8

cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)    # 선 img에, (,) 에서, (,) 까지, BGR, 선의 굴기
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)    # 사각형img에, 좌상 꼭지점, 우하 꼭지점, (BGR), 두께
cv2.circle(img, (477, 63), 63, (0, 0, 255), -1)    # 원 img에, 중심, 반지름, BGR, -1:주어진 색상으로 채움 
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)    # 타원 img에, 중심, (장축, 단축)각각 1/2 길이, 기울기 각도, 시작각도, 끝 각도, BGR, 채움

font = cv2.FONT_HERSHEY_SIMPLEX    #폰트 지정
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255,255,255), 2)    # 글자 표시 img에, '~'라는 글자를, 좌표에, 폰트, 크기, BGR, 굵기

cv2.imwrite('RstImg/draw_img.jpg', img)    # 저장