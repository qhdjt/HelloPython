import cv2 as cv
import numpy as np

# 目标追踪
# 现在我们知道了如何将 BGR 图片转化为 HSV 图片，我们可以使用它去提取彩色对象。
#   HSV 比 BGR 在颜色空间上更容易表示颜色。在我们的应用中，我们会尝试提取一个蓝色的彩色对象，方法为：
# 提取每一视频帧。
# 将 BGR 转化为 HSV 颜色空间。
# 我们用蓝色像素的范围对该 HSV 图片做阈值。
# 现在提取出了蓝色对象，我们可以随意处理图片了 。
cap = cv.VideoCapture('../res/video.mp4')
while True:
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(100) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

# 如何找到 HSV 值去追踪?
# 这个问题非常简单，你可以使用相同的函数：cv.cvtColor()。
# 不需要输入图片，你只需要输入你需要的 BGR 值即可.
# 例如, 为了找到绿色的 HSV 值, 可以在 Python 终端中输入以下代码:
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)  # [[[60 255 255]]]
# 现在你可以取 [H-10, 100,100] 和 [H+10, 255, 255] 分别作为上界和下界. 除此之外，你可以使用任何图像编辑工具（如 GIMP）或任何在线转换器来查找这些值，但不要忘记调整 HSV 范围。

