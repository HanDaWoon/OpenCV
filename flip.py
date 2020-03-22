import cv2

src = cv2.imread('src/A.jpg')    #원본 이미지 읽기

dst = cv2.flip(src, 0)    #flip(target img, 0:상하, 1:좌우 )

cv2.imwrite('dst/flip_A.jpg', dst)    #결과값 저장하기