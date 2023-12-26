import numpy as np
import cv2 as cv

# 创建一个黑色的图像
img = np.zeros((512, 512, 3), np.uint8)
# 画线
# 画一条 5px 宽的蓝色对角线
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 画矩形
# 画一个矩形，你需要矩形的左上角和右下角。这次我们将会在图像的右上角画一个绿色的矩形。
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# 画圆
# 画一个圆，你需要它的圆心和半径。我们将在上面绘制的矩形上画一个内圆。
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
# 画椭圆
# 画一个椭圆，你需要传好几个参数。
# 一个参数是圆心位置 (x,y)。下个参数是轴的长度 (长轴长度，短轴长度)。
# 角度是椭圆在你逆时针方向的旋转角度。
# startAngle 和 endAngle 表示从长轴顺时针方向测量的椭圆弧的起点和终点。如整圆就传 0 和 360。
# 更多细节请看 cv.ellipse() 的文档。下面是在这个图像中间画的一个半椭圆例子。
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (45, 67, 89), -1)
# cv.ellipse(img=img,box=[],color=(233,43,55),thickness=-1)
cv.ellipse(img=img, center=(256, 256), axes=(100, 50), angle=180, startAngle=0, endAngle=180, color=(98, 76, 54),thickness=-1, lineType=cv.LINE_4, shift=0)
# 画多边形
# 画多边形，首先你需要顶点的做坐标。将这些点组成一个形状为 ROWSx1x2 的数组，ROWS 是顶点数，它应该是 int32 类型。这里我们绘制一个顶点是黄色的小多边形。
pts = np.array([[55, 76], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))
cv.putText(img=img, text="hello", org=(14,400), fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=cv.FONT_HERSHEY_TRIPLEX, color=(255,244,233), thickness=11, lineType=cv.LINE_8, bottomLeftOrigin=False)
cv.imshow("img", img)
cv.waitKey(0)
