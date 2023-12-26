import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def get_variable_name(var):
    for name, value in globals().items():
        if value is var:
            return name


def cv_show(img):
    title = get_variable_name(img)
    cv.namedWindow(title, cv.WINDOW_NORMAL)
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return


img = cv.imread('./res/bin.png', 0)
# Output dtype = cv.CV_8U
sobelx8u = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=3)
print(cv.CV_8U)
print(cv.CV_64F)
# Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx64f = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray'), plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray'), plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()
