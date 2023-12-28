import inspect

import cv2
import cv2 as cv
import numpy as np
from cv2.typing import MatLike


def cv_show(mat):
    cv2.namedWindow(winname=mat.__str__(), flags=cv2.WINDOW_NORMAL)
    cv2.imshow(mat.__str__(), mat)
    cv2.waitKey(0)


def step1(img: MatLike) -> MatLike:
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(7, 3))
    # 开操作，去除竖栅
    out = cv.morphologyEx(src=img, op=cv.MORPH_OPEN, kernel=kernel)
    # 应用阈值处理,去除电极
    ret, thresh = cv2.threshold(out, 230, 255, cv2.THRESH_TOZERO_INV)
    ultimate = cv.morphologyEx(src=thresh, op=cv.MORPH_OPEN, kernel=kernel)
    return ultimate


# 开操作


# 均值滤波
def step2(img: MatLike) -> MatLike:
    # 应用阈值处理
    ret, thresh = cv2.threshold(img, 220, 255, cv2.THRESH_TOZERO_INV)
    # cv.imshow("step2",thresh)
    # cv.waitKey(0)
    t = step1(thresh)
    blur = cv.blur(t, (23, 29))
    return blur


# 动态二值化
def step3(base: MatLike, blur: MatLike) -> MatLike:
    # 计算图像差值
    diff = cv2.subtract(blur, base)
    # diff_abs = np.abs(img1 - img)

    # 应用阈值处理进行二值化
    ret, thresh = cv2.threshold(diff, 55, 255, cv2.THRESH_BINARY)
    return thresh


if __name__ == '__main__':
    src = cv2.imread("./dd.BMP", cv2.IMREAD_REDUCED_GRAYSCALE_2)
    # src = cv.imread("dd.BMP")
    s1 = step1(src)
    cv_show(s1)
    s2 = step2(s1)
    cv_show(s2)
    s3 = step3(s2, s1)
    cv_show(s3)
