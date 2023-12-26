import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 目标
# 我们将学习不同的形态操作，如腐蚀、膨胀、开、闭等。
# 我们将看到不同的函数，如： cv.erode()、 cv.dilate()、 cv.morphologyEx() 等。
# 理论
# 形态学变换是基于图像形状的一些简单操作。它通常在二值图像上执行。
# 它需要两个输入，一个是我们的原始图像，第二个是决定操作性质的结构元素或内核。
# 两个基本的形态学操作是腐蚀和膨胀。
# 接下来如开，闭，梯度等也会介绍。在下图的帮助下，我们将逐一看到它们：

kernel = np.ones((7, 7), np.uint8)
img = cv.imread('./res/j.png', cv.IMREAD_GRAYSCALE)
# 形态学操作

# 1、腐蚀
# 腐蚀的基本概念就像土壤侵蚀一样，只侵蚀前景对象的边界（总是尽量保持前景为白色）。
# 那它有什么作用呢？内核在图像中滑动（如二维卷积）。只有当内核下的所有像素都为 1 时，原始图像中的像素（1 或 0）才会被视为 1，否则会被侵蚀（变为零）。
# 所以根据内核的大小，边界附近的所有像素都将被丢弃。因此，前景对象的厚度或大小在图像中减少或只是白色区域减少。
# 它有助于消除小的白色噪音（如我们在“颜色空间”一章中所看到的），分离两个连接的对象等。
erosion = cv2.erode(img, kernel, iterations=1)
# 2、膨胀
# 它与腐蚀正好相反。这里，如果内核下至少有一个像素为“1”，则像素元素为“1”。
# 所以它会增加图像中的白色区域，或者增加前景对象的大小。通常情况下，在去除噪音的情况下，腐蚀后会膨胀。
# 因为，腐蚀消除了白噪声，但它也缩小了我们的对象。所以我们扩大它。
# 由于噪音消失了，它们不会再回来，但我们的目标区域会增加到腐蚀之前的状态。它还可用于连接对象的断开部分。
dilation = cv2.dilate(img, kernel, iterations=1)
# 3、开运算
# 开只是腐蚀的另一个名称，随后是膨胀。正如我们上面所解释的，它对消除噪音很有用。在这里，我们使用 cv.morphologyEx()。
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
# 4、闭运算
# 关闭与打开相反，膨胀后腐蚀。它在填充前景对象内的小孔或对象上的小黑点时很有用。
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
# 5、形态梯度
# 它是图像的膨胀和腐蚀之间的差值。结果将类似于对象的轮廓。
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
# 6、顶帽
# 它是原图像和原图像开运算结果的差值。下面是 9x9 核的例子。
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
# 7、黑帽
# 它是原图像和原图像的闭的差值。
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
# 使用matplotlib同时展示原始图像和处理后的图像
plt.subplot(2, 5, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 2), plt.imshow(dilation, cmap='gray'), plt.title('Dilation'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 3), plt.imshow(erosion, cmap='gray'), plt.title('Erosion'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 4), plt.imshow(opening, cmap='gray'), plt.title('opening'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 5), plt.imshow(closing, cmap='gray'), plt.title('closing'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 6), plt.imshow(gradient, cmap='gray'), plt.title('gradient'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 7), plt.imshow(tophat, cmap='gray'), plt.title('tophat'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 5, 8), plt.imshow(blackhat, cmap='gray'), plt.title('blackhat'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 5, 9), plt.imshow(erosion, cmap='gray'), plt.title('Erosion'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 5, 10), plt.imshow(erosion, cmap='gray'), plt.title('Erosion'), plt.xticks([]), plt.yticks([])
plt.show()
# 结构元素
# 在前面的例子中，我们在 numpy 的帮助下手工创建了一个结构参量。它是长方形的。
# 但在某些情况下，您可能需要椭圆/圆形的内核。因此，opencv 有一个函数，cv.getStructuringElement()。只要传递内核的形状和大小，就可以得到所需的内核。
# 核
# cv2.MORPH_RECT：矩形结构元素，所有元素值都是1
# cv2.MORPH_CROSS：十字形结构元素，对角线元素值都是1
# cv2.MORPH_ELLIPSE：椭圆形结构元素
kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(7, 7), anchor=(-1, -1))
kernel1 = cv.getStructuringElement(cv.MORPH_CROSS, (7, 7))
kernel2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))
print("kernel:\n{}".format(kernel))
print("kernel1:\n{}".format(kernel1))
print("kernel2:\n{}".format(kernel2))
