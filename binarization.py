import cv2
import numpy as np

img_color = cv2.imread('OrgImg/y_apple.jpg', cv2.IMREAD_COLOR)    #컬러로 이미지 입력
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)    #컬러 이미지를 그레이스케일으로 변환
ret,img_binary = cv2.threshold(img_gray, 136, 255, cv2.THRESH_BINARY_INV)    #대상이미지(그레이스케일), 기준, 기준보다 픽셀값이 클때 변경할 값, THRESH_BINARY일 떄 기준보다 픽셀값이 낮으면 0(INV:반전)
cv2.imwrite('RstImg/img_binary_inv.jpg', img_binary)

img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
cv2.imwrite('RstImg/img_binary_rst.jpg', img_result)