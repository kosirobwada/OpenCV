import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread('logo.png')

# 変更前の色
target_color = np.array([26, 119, 238])

# 変更後の色
change_color = np.array([12, 12, 12])

# 色の変更
diff = np.abs(img - target_color)
mask = np.all(diff < 10, axis=2)
img[mask] = change_color

# 変更後の画像の保存
cv2.imwrite('modified_logo.png', img)
