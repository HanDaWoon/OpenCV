import cv2
import numpy as np

def add_image(imgfile1, imgdile2):    #합성 하는 함수 선언
    img1 = cv2.imread(imgfile1)    #1번 이미지 읽기
    img2 = cv2.imread(imgdile2)    #2번 이미지 읽기
    
    #이미지 합성하기
    add_img1 = img1 + img2  
    add_img2 = cv2.add(img1, img2)
    
    #합성한 이미지 저장
    cv2.imwrite('dst/test_ApB.jpg', add_img1) 
    cv2.imwrite('dst/test_AadB.jpg', add_img2)
    
    cv2.waitKey(0)
    

add_image('src/A.jpg', 'src/B.jpg')