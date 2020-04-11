import cv2

img_color = cv2.imread('OrgImg/y_apple.jpg')

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 140, 255, 0)
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img_color, contours, -1, (0, 255, 0), 3)

cv2.imwrite('RstImg/img_contours.jpg', img_color)