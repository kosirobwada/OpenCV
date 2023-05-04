import cv2

img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)  # グレースケールで読み込む
edges = cv2.Canny(img, 100, 200)  # Canny法でエッジ検出を行う

cv2.imshow("test", edges)
cv2.waitKey(0)
