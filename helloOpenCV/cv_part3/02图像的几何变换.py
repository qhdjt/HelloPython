import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 变换
# OpenCV 提供了两个变换函数， cv.warpAffine 和 cv.getPerspectiveTransform ，用这两个函数就可以完成所有类型的变换。
# cv.warpAffine 输入为 2x3 的变换矩阵， cv.getPerspectiveTransform 输入为 2x3 的变换矩阵。

# 缩放
# 缩放是调整图片的大小。 OpenCV 使用 cv.resize() 函数进行调整。可以手动指定图像的大小，也可以指定比例因子。
# 可以使用不同的插值方法。对于下采样(图像上缩小)，最合适的插值方法是 cv.INTER_AREA 对于上采样(放大),最好的方法是 cv.INTER_CUBIC （速度较慢）和 cv.INTER_LINEAR (速度较快)。
# 默认情况下，所使用的插值方法都是 cv.INTER_AREA 。你可以使用如下方法调整输入图片大小：
def scaling():
    img = cv.imread('./res/cat.png')
    # res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
    res = cv.resize(img, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
    cv.imshow(res.shape.__str__(), res)
    cv.waitKey(0)
    # OR
    height, width = img.shape[:2]
    # res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
    size = (int(width * 0.5), int(height * 0.5))
    res = cv.resize(img, size, interpolation=cv.INTER_AREA)
    cv.imshow(res.shape.__str__(), res)
    cv.waitKey(0)


# 平移变换
# cv.warpAffine 函数的第三个参数是输出图像的大小，其形式应为（宽度、高度）。记住宽度=列数，高度=行数。
def translation():
    # 缩放
    img = cv.imread('./res/cat.png', 0)
    rows, cols = img.shape
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv.warpAffine(img, M, (cols, rows))
    cv.imshow('img', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


# 旋转
def rotation():
    img = cv.imread('./res/cat.png', cv.IMREAD_GRAYSCALE)
    rows, cols = img.shape
    # cols-1 and rows-1 are the coordinate limits.
    M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
    dst = cv.warpAffine(img, M, (cols, rows))
    cv.imshow('img', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


# 仿射变换
# 在仿射变换中，原始图像中的所有平行线在输出图像中仍然是平行的。
# 为了找到变换矩阵，我们需要从输入图像中取三个点及其在输出图像中的对应位置。
# 然后 cv.getPerspectiveTransform 将创建一个 2x3 矩阵，该矩阵将传递给 cv.warpAffine。
def affine():
    img = cv.imread('./res/drawing.png')
    rows, cols, ch = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    for pt in pts1:
        cv.circle(img, (int(pt[0]), int(pt[1])), 5, (0, 0, 255), -1)
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv.getAffineTransform(pts1, pts2)
    dst = cv.warpAffine(img, M, (cols * 2, rows * 2))
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()


# 透视变换
# 对透视转换，你需要一个 3x3 变换矩阵。即使在转换之后，直线也将保持直线。
# 要找到这个变换矩阵，需要输入图像上的 4 个点和输出图像上的相应点。在这四点中，任意三点不应该共线。
# 然后通过 cv.getPerspectiveTransform 找到变换矩阵。然后对这个 3x3 变换矩阵使用 cv.warpPerspective。
def transform():
    img = cv.imread('./res/drawing1.png')
    rows, cols, ch = img.shape
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    # 使用cv2.circle()函数在图像上绘制点
    for pt in pts1:
        cv.circle(img, (int(pt[0]), int(pt[1])), 5, (0, 0, 255), -1)
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    dst = cv.warpPerspective(img, M, (300, 300))
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()


# 缩放
scaling()
# 平移变换
translation()
# 旋转
rotation()
# 仿射变换
affine()
# 透视变换
transform()
