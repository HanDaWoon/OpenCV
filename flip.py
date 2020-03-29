import cv2

src1 = cv2.imread('OrgImg/A.jpg')    #원본 이미지 읽기
src2 = cv2.imread('OrgImg/A.jpg')
dst1 = cv2.flip(src1, 0)    #flip(target img, 0:상하, 1:좌우 )
dst2 = cv2.flip(src2, 1)

cv2.imwrite('RstImg/flip_A.jpg', dst1)    #결과값 저장하기
cv2.imwrite('RstImg/flip_B.jpg', dst2)