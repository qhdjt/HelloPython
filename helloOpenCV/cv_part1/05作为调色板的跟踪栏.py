import numpy as np
import cv2 as cv


# 对于 cv.getTrackbarPos() 函数，第一个参数是轨迹栏名字，第二那个是被附上窗口名字，第三个参数是默认值，第四个是最大值，第五个是回调函数，滑条改变所执行的函数。
# 这个回调函数也有一个默认参数，表示轨迹栏位置。我们并不关心函数做什么事，所以我们简单提一下。
# 轨迹栏的另一个重要应用是用作按钮或者开关。
# OpenCV，默认情况，是没有按钮功能的。因此我们能用轨迹栏做一些这样的功能。
# 在我们的程序中，我门创建了一个开关，其中程序只会在开关打开时有效，否则屏幕始终是黑色。

def nothing(x):
    pass


# 创建一个黑色图像，一个窗口
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')
# 创建一个改变颜色的轨迹栏
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)
# 创建一个开关用来启用和关闭功能的
switch = '0 : OFF \n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)
while (1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv.destroyAllWindows()
