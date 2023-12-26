import cv2 as cv
import numpy as np

# cv.putText(img, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
# img: 需要绘制文本的图像。
# text: 要绘制的文本。
# org: 文本的左下角坐标，通常设置为 (0,0)。
# font: 字体类型。
# fontScale: 字体大小。
# color: 字体颜色。可以是一个元组，例如 (255, 0, 0) 表示蓝色。
# thickness: 文本线宽，如果为负数（如 cv.FILLED），则线宽为字体大小的两倍。
# lineType: 线条类型。
# bottomLeftOrigin: 是否以左下角为原点开始绘制。默认为 False，表示以左上角为原点。
# 创建一个空图像
img = np.zeros((512, 512, 3), np.uint8)
text = 'Hello OpenCV'
org = (50, 50)  # 左下角坐标
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)  # 蓝色
thickness = 2
img = cv.putText(img, text, org, font, fontScale, color, thickness)
cv.imshow(text, img)
key = cv.waitKey(0)
if key == 27:  # ESC 退出
    # cv.destroyAllWindows()
    cv.destroyWindow('image')
# elif key == ord('s'): # 's' 保存退出
#     cv.imwrite('messigray.png',img)
#     cv.destroyAllWindows()
