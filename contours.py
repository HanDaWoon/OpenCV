import cv2
import numpy as np


TREE = cv2.RETR_TREE
LIST = cv2.RETR_LIST
EXTERNAL = cv2.RETR_EXTERNAL
CCOMP = cv2.RETR_CCOMP
SIMPLE = cv2.CHAIN_APPROX_SIMPLE
NONE = cv2.CHAIN_APPROX_NONE


def basic(src, threshold, retr, approx):
    """원본 이미지, 임계값, RETR mode, approx"""
    img_color = cv2.imread('OrgImg/'+src)
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    ret, img_binary = cv2.threshold(img_gray, threshold, 255, 0)
    contours, hierarchy = cv2.findContours(img_binary, retr, approx)
    return img_color, contours, hierarchy


print("컨투어")
print("A:찾고그리기, B:좌표에 그림, C:hierarchy")
print("D:영역크기, E:근사화, F:무게중심, G:경계사각형, H:Convex Hull, I:Convexity Defects")

run = input("run:")
print("\n" * 3)

#################################################
# 컨투어 찾고 그리기
if run == "A":

    img_color = cv2.imread('OrgImg/contours_a.png')    # 컬러이미지를 읽음

    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)    # 그레이스케일 변환
    ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)    # 이진화

    # cv.findContours(src, mode, method[, contours[, hierarchy[, offset]]])
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # cv2.drawContours(src, contours, contourldx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]])
    # index가 0인 컨투어를 img_color에 BGR,두께 로 그림(contourldx 가 -1 이면 모든 컨투어를 그림)
    cv2.drawContours(img_color, contours, 0, (0, 255, 0), 2)
    cv2.drawContours(img_color, contours, 1, (255, 0, 0,), 2)

    cv2.imwrite('RstImg/컨투어찾고그리기.jpg', img_color)

#################################################
# 컨투어의 좌표
elif run == "B":

    img_color, contours, hierarchy = basic("box.jpg", 127, LIST, SIMPLE)

    # 컨투어에 포함된 모든 좌표마다 파란색 원을 그림
    for cnt in contours:
        for p in cnt:
            cv2.circle(img_color, (p[0][0], p[0][1]), 10, (255, 0, 0), -1)

    cv2.imwrite('RstImg/컨투어의좌표.jpg', img_color)

#################################################
# hierarchy
elif run == "C":
    # RETR mode = RETR_TREE / RETR_LIST / RETR_EXTERNAL / RETR_CCOMP
    img_color, contours, hierarchy = basic("hierarchy.png", 127, LIST, SIMPLE)

    for cnt in contours:
        cv2.drawContours(img_color, [cnt], 0, (0, 255, 0), 2)

    print(hierarchy)

    cv2.imwrite('RstImg/hierarchy.jpg', img_color)

#################################################
# 영역크기
elif run == "D":

    img_color, contours, hierarchy = basic("contours_a.png", 127, LIST, SIMPLE)

    for cnt in contours:
        cv2.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)

    cv2.imwrite('RstImg/영역크기.jpg', img_color)

    # 각 컨투어의 영역을 출력
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

#################################################
# 근사화
elif run == "E":

    img_color, contours, hierarchy = basic("contours_b.png", 127, LIST, SIMPLE)

    # 컨투어 그리기
    cv2.drawContours(img_color, contours, 0, (255, 0, 0), 3)    # Blue

    # arcLength(컨투어(배열), 폐곡선 여부
    # approxPolyDP(컨투어(배열), 근사치 정확도(입력과 출력 다각형사이의 최대편차간격, 폐곡선 여부)
    for cnt in contours:
        epsilon = 0.02 * cv2.arcLength(cnt, True)    # arcLength의 2%를 정확도로 사용
        approx = cv2.approxPolyDP(cnt, epsilon, True)    # 근사화된 배열
        print(len(approx))
        cv2.drawContours(img_color, [approx], 0, (0, 255, 255), 5)    # Yellow

    cv2.imwrite('RstImg/근사화.jpg', img_color)

#################################################
# 무게중심
elif run == "F":

    img_color, contours, hierarchy = basic("contours_a.png", 127, LIST, SIMPLE)

    for cnt in contours:
        cv2.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)  # blue

    for cnt in contours:
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cv2.circle(img_color, (cx, cy), 3, (0, 0, 255), -1)    # Red

    cv2.imwrite('RstImg/무게중심.jpg', img_color)

# 질량 중심 공식 : x = m10/m00, y = m01/m00
# cv2.moments(numpy array 1xN or Nx1)
# Spatial Moments(공간) : M00(폐곡선면적), M01, M02, M03, M10, M11, M12, M20, M21, M30
# Central Moments(중심) : Mu02, Mu03, Mu11, Mu12, Mu20, Mu21, Mu30
# Central Normalized Moments(평준화) : Nu02, Nu03, Nu11, Nu12, Nu20, Nu21, Nu30

#################################################
# 경계사각형
elif run == "G":

    img_color, contours, hierarchy = basic("contours_a.png", 127, LIST, SIMPLE)

    # 컨투어 그리기
    for cnt in contours:
        cv2.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)  # blue

    # 최소단위의 경계사각형을 그림
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img_color, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 도형의 방향을 생각하여 경계사각형을 그림
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)    # 컨투어에 외접하면서 면적이 가장 작은 직사각형
        box = cv2.boxPoints(rect)    # rect의 4개의 꼭지점 좌표값 휙득
        box = np.int0(box)    # float to int
        cv2.drawContours(img_color, [box], 0, (0, 0, 255), 2)
    # minAreaRect(contours) retun 좌상단 꼭지점 좌표, 가로/세로 폭, 기울기
    # boxPoints(minAreaRect의 return) return 꼭지점 4개의 좌표(float)

    cv2.imwrite('RstImg/격계사각형.jpg', img_color)

#################################################
# Convex Hull
elif run == "H":

    img_color, contours, hierarchy = basic("contours_c.png", 127, LIST, SIMPLE)

    cv2.drawContours(img_color, contours, 0, (255, 0, 0), 2)    # blue

    for cnt in contours:
        hull = cv2.convexHull(cnt)    # 컨투어에 대한 convex Hull 곡선을 return
        cv2.drawContours(img_color, [hull], 0, (0, 255, 0), 2)    # green

    cv2.imwrite('RstImg/Convex Hull.jpg', img_color)

#################################################
# Convexity Defects
elif run == "I":

    img_color, contours, hierarchy = basic("contours_c.png", 127, LIST, SIMPLE)

    cv2.drawContours(img_color, contours, 0, (255, 0, 0), 2)    # blue

    for cnt in contours:
        hull = cv2.convexHull(cnt)
        cv2.drawContours(img_color, [hull], 0, (0, 255, 0), 2)    # green

    for cnt in contours:
        hull = cv2.convexHull(cnt, returnPoints=False)    # 컨투어와 convexHull의 접점
        defects = cv2.convexityDefects(cnt, hull)
        # 시작점, 끝점, 가장 먼점, 가장 먼점 까지의 대략적 거리

        for i in range(defects.shape[0]):    # 찾은 인덱스의 개수
            sp, ep, fp, dist = defects[i, 0]    # star p, end p, far p, dist
            start = tuple(cnt[sp][0])
            end = tuple(cnt[ep][0])
            far = tuple(cnt[fp][0])

            print(dist)

            # 가장 먼점 까지의 거리가 500 이상일때 선과 원 그림
            if dist > 500:
                cv2.line(img_color, start, end, [0, 255, 0], 5)
                cv2.circle(img_color, far, 5, [0, 0, 255], -1)

    cv2.imwrite('RstImg/Convexity Defects.jpg', img_color)

#################################################
else:

    print("떙!")
