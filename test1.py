import cv2

img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)
##白黒画像にするプログラム

cv2.imshow("test", img)
cv2.waitKey(0)
