import cv2

img = cv2.imread("sample.jpg")
##読み込んだ画像を表示するプログラム

cv2.imshow("test", img)
cv2.waitKey(0)