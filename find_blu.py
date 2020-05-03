import cv2

img_color = cv2.imread('OrgImg/color_circle.png')
height, width = img_color.shape[:2]    # 높이와 너비

img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
# HSV이미지로 변환

lower_blue = (120-10, 30, 30)    # 하한값
upper_blue = (120+10, 255, 255)    # 상한값

# 바이너리이미지 휙득, 범위내의 이미지 흰색 나머지 검은색
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

# bitwise_and(src1, src2, dst, InputArray mask=noArray())
img_result = cv2.bitwise_and(img_color, img_color, mask=img_mask)

cv2.imwrite('RstImg/img_mask.jpg', img_mask)
cv2.imwrite('RstImg/img_result.jpg', img_result)
