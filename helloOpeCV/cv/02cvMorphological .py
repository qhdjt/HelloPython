import cv2
import matplotlib.pyplot as plt


# 基本梯度是用膨胀后的图像减去腐蚀后的图像得到差值图像
# 原图像减去腐蚀之后的图像得到差值图像
# 用图像膨胀之后再减去原来的图像得到的差值图像
def show_image(image_path="./res/pxArt.png"):
    # 读取原始图像
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    # 将图像转为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 将灰度图像进行二值化处理
    ret, binary = cv2.threshold(src=gray, thresh=176, maxval=255, type=cv2.THRESH_BINARY)
    # 核
    # cv2.MORPH_RECT：矩形结构元素，所有元素值都是1
    # cv2.MORPH_CROSS：十字形结构元素，对角线元素值都是1
    # cv2.MORPH_ELLIPSE：椭圆形结构元素
    kernel1 = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(5, 5), anchor=(-1, -1))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    # kernel = np.ones((7, 5), np.uint8)

    kernel = kernel2
    # 对二值化图像进行膨胀操作
    dilation = cv2.dilate(binary, kernel, iterations=1)
    # 对二值化图像进行腐蚀操作
    erosion = cv2.erode(binary, kernel, iterations=1)
    # cv2.morphologyEx()
    # src：输入图像
    # dst：输出图像
    # op：表示形态学运算类型
    # kernel：膨胀操作的核，也是用getStructuringElement()获得的Mat对象。其两个元素都不能小于1。
    # anchor：锚的位置。默认(-1, -1)，表示锚位于中心
    # iterations：迭代使用erode()的次数。默认1次
    # borderType：用于推断图像外部像素的某种边界模式。
    # borderValue：不管

    # MORPH_DILATE：膨胀
    dilate = cv2.morphologyEx(binary, cv2.MORPH_DILATE, kernel)
    # MORPH_ERODE：腐蚀
    erode = cv2.morphologyEx(binary, cv2.MORPH_ERODE, kernel)
    # MORPH_OPEN：开运算
    opening = cv2.morphologyEx(src=binary, op=cv2.MORPH_OPEN, kernel=kernel, anchor=(-1, -1))
    # MORPH_CLOSE：闭运算
    close = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    # MORPH_BLACKHAT：黑帽
    blackhat = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel)
    # MORPH_TOPHAT：顶帽
    tophat = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernel)
    # MORPH_GRADIENT：形态学梯度
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
    cross = cv2.morphologyEx(binary, cv2.MORPH_CROSS, kernel)
    ellipse = cv2.morphologyEx(binary, cv2.MORPH_ELLIPSE, kernel)
    hitmiss = cv2.morphologyEx(binary, cv2.MORPH_HITMISS, kernel)
    rect = cv2.morphologyEx(binary, cv2.MORPH_RECT, kernel)

    # 显示图像
    # 支持中文
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # plt.title("啥")
    fig, axs = plt.subplots(nrows=3, ncols=5, figsize=(20, 20))
    axs[0, 0].set_title('原图'), axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[0, 1].set_title('灰度图'), axs[0, 1].imshow(gray, cmap='gray')
    axs[0, 2].set_title('二值化图像'), axs[0, 2].imshow(binary, cmap='gray')
    axs[0, 3].set_title('膨胀后的图像'), axs[0, 3].imshow(dilation, cmap='gray')
    axs[0, 4].set_title('dilate'), axs[0, 4].imshow(dilate, cmap='gray')

    axs[1, 0].set_title('腐蚀后的图像'), axs[1, 0].imshow(erosion, cmap='gray')
    axs[1, 1].set_title('erode'), axs[1, 1].imshow(erode, cmap='gray')
    axs[1, 2].set_title('opening'), axs[1, 2].imshow(opening, cmap='gray')
    axs[1, 3].set_title('close'), axs[1, 3].imshow(close, cmap='gray')
    axs[1, 4].set_title('blackhat'), axs[1, 4].imshow(blackhat, cmap='gray')

    axs[2, 0].set_title('tophat'), axs[2, 0].imshow(tophat, cmap='gray')
    axs[2, 1].set_title('gradient'), axs[2, 1].imshow(gradient, cmap='gray')
    axs[2, 2].set_title('ellipse'), axs[2, 2].imshow(ellipse, cmap='gray')
    axs[2, 3].set_title('hitmiss'), axs[2, 3].imshow(hitmiss, cmap='gray')
    axs[2, 4].set_title('rect'), axs[2, 4].imshow(rect, cmap='gray')
    # 显示
    plt.show()


if __name__ == '__main__':
    show_image()
