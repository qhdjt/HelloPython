import cv2 as cv
from matplotlib import pyplot as plt


def get_variable_name(var):
    for name, value in globals().items():
        if value is var:
            return name


def cv_show(img):
    title = get_variable_name(img)
    cv.namedWindow(title,cv.WINDOW_NORMAL)
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return


# Sobel 算子是一种联合高斯平滑加微分运算，因此对噪声的抵抗能力更强。
# 可以指定要计算的导数的方向，垂直或水平（分别由参数、Yorder 和 Xorder 指定）。还可以通过参数 ksize 指定内核的大小。
# 如果 ksize=-1，则使用 3x3 Scharr 滤波器，这比 3x3 Sobel 滤波器效果更好。请参阅所用内核的文档。
img = cv.imread('./res/bin.png', cv.IMREAD_GRAYSCALE)
# Sobel
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
sobelx = cv.convertScaleAbs(sobelx)
sobely = cv.convertScaleAbs(sobely)
# 融合梯度
# sobel_xy = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
sobel_xy = cv.add(sobelx, sobely)

scharrx = cv.Scharr(img, cv.CV_64F, 1, 0)
cv_show(scharrx)
scharry = cv.Scharr(img, cv.CV_64F, 0, 1)
scharrx = cv.convertScaleAbs(scharrx)
scharry = cv.convertScaleAbs(scharry)
# 融合梯度
scharr_xy = cv.add(scharrx, scharry)

laplacian = cv.Laplacian(img, cv.CV_64F, ksize=3)
laplacian = cv.convertScaleAbs(laplacian)

plt.subplot(2, 4, 1), plt.imshow(img, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Original'),
plt.subplot(2, 4, 2), plt.imshow(sobelx, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Sobel X')
plt.subplot(2, 4, 3), plt.imshow(sobely, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Sobel Y')
plt.subplot(2, 4, 4), plt.imshow(sobel_xy, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('sobel_xy')
plt.subplot(2, 4, 5), plt.imshow(laplacian, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Laplacian')
plt.subplot(2, 4, 6), plt.imshow(scharrx, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('scharr x')
plt.subplot(2, 4, 7), plt.imshow(scharry, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('scharr y')
plt.subplot(2, 4, 8), plt.imshow(scharr_xy, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('scharr_xy')

plt.show()
