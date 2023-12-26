import cv2 as cv
import numpy as np

# 图像加法
# x = np.uint8([250])
# y = np.uint8([10])
# print(cv.add(x, y))  # 250 + 10 =260 => 255
# print(x + y)  # 4

# 图像混合
# img1 = cv.imread('../res/img_1.png')
# img2 = cv.imread('../res/img_2.png')
# dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
# cv.imshow('dst', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()


# 按位操作
# 加载两张图片
img1 = cv.imread('./res/cat.png')
img2 = cv.imread('./res/opencv-logo.png')
# 我想在左上角放置一个logo,所以我创建了一个 ROI,并且这个ROI的宽和高为我想放置的logo的宽和高
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
# 现在创建一个logo的掩码,通过对logo图像进行阈值,并对阈值结果并创建其反转掩码
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# 现在使 ROI 中的徽标区域变黑
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
# 仅从徽标图像中获取徽标区域。
img2_fg = cv.bitwise_and(img2, img2, mask=mask)
# 在 ROI 中放置徽标并修改主图像
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()
