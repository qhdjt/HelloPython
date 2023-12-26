import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 读取图像
img = cv.imread('./res/cat.png', cv.IMREAD_COLOR)
print(img.shape)

# 显示图像 1
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 显示图像 2
# 指定窗口加载方式
# cv.namedWindow('image', cv.WINDOW_NORMAL)
# cv.imshow('image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 保存图像
# cv.imshow('image',img)
# k = cv.waitKey(0)
# if k == 27: # ESC 退出
#     # cv.destroyAllWindows()
#     cv.destroyWindow('image')
# elif k == ord('s'): # 's' 保存退出
#     cv.imwrite('messigray.png',img)
#     cv.destroyAllWindows()

# 使用 Matplotlib
cv.cvtColor(img, cv.COLOR_BGR2RGB, img)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏 X 和 Y 轴的刻度值
plt.show()
