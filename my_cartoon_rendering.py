import cv2
import numpy as np


img = cv2.imread('sampleImages/image1.jpg')

# cvtColor(src, code) -> 이미지의 색상공간을 변환하는데 사용됨.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # gray로 변환

# medianBlur(src, code) 
gray = cv2.medianBlur(gray, 7)

# adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C) -> 흑백처리(0과 255)
# edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)



# adaptiveThreshold 적용 -> binary image 생성
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
# dilate -> 팽창 (선을 굵게 함)
kernel = np.ones((3, 3), np.uint8)
edges= cv2.dilate(edges, kernel, iterations=1)
# bitwise_not -> 색상 반전
edges= cv2.bitwise_not(edges)



# bilateralFilter(src, d, sigmaColor, sigmaSpace) -> edge-preserving and smoothing
color = cv2.bilateralFilter(img, -1, 10, 100)
# d = -1 이면 sigmaSpace 값에 의해 자동 설정.

# bitwise(src1, src2, [mask]) -> mask의 0이 아닌 부분만 src1과 src2가 AND연산함. 0인 부분은 mask로 씌움.
cartoon = cv2.bitwise_and(color, color, mask=edges)

merge = np.hstack((img, cartoon))

cv2.imshow("My Cartoon Rendering", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()