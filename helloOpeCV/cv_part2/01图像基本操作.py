import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from helloOpeCV.Utils import namedShow

# 首先，一张图像有自己的属性，宽，高，通道数。其中宽和高是我们肉眼可见的属性，而通道数则是图像能呈现色彩的属性。
# 我们都知道，光学三原色是红色，绿色和蓝色，这三种颜色的混合可以形成任意的颜色。
# 常见的图像的像素通道也是对应的R，G，B三个通道，在OpenCV中，每个通道的取值为0～255，。(注：还有RGBA，YCrCb，HSV等其他图像通道表示)。
# 即，一般彩色图像读进内存之后是一个h w c的矩阵，其中h为图像高(相当于矩阵的行)，w为图像宽(相当于矩阵列)，c为通道数。

# 下面我们先加载一副彩色图像
# 黄色为绿色和红色的混合，所以，该图像的所有像素值都应为R=255，G=255，B=0
img = cv.imread("./res/yellow.png")
h, w, c = img.shape
# 图像为128*128*3的大小
print("height:{},width:{},channels:{}".format(h, w, c))
# 注意 img.dtype 在调试时非常重要，因为 OpenCV—Python 代码中的大量错误是由无效的数据类型引起的。


print("""  访问和修改像素值:  """)
# 注意,对于常见的RGB 图像，OpenCV的imread函数返回的是一个蓝色(Blue)、绿色(Green)、红色(Red)值的数组，维度大小为3。
# 而对于灰度图像，仅返回相应的强度。

# 访问三通道的像素
print("img[10, 10]:{}".format(img[10, 10]))  # OpenCV的读取顺序为B，G，R，由于图像所有像素为黄色，因此，G=255，R=255
# 仅访问蓝色通道的像素
blue = img[10, 10, 0]
print("blue:{}".format(blue))
# 你也可以使用同样的方法来修改像素值
img[10, 10] = [0, 0, 0]

# 警告
# Numpy 是一个用于快速阵列计算的优化库。因此，简单地访问每个像素值并对其进行修改将非常缓慢，并不鼓励这样做。
# 注意 上述方法通常用于选择数组的某个区域，比如前 5 行和后 3 列。
# 对于单个像素的访问，可以选择使用 Numpy 数组方法中的 array.item()和 array.itemset()，注意它们的返回值是一个标量。
# 如果需要访问所有的 G、R、B 的值，则需要分别为所有的调用 array.item()。

# 更好的访问像素和编辑像素的方法：
# 访问 红色通道 的值
print("坐标(11,11)处红色通道的值:", img.item(11, 11, 2))
# 修改 红色通道 的值
img.itemset((11, 11, 2), 0)
print("修改后,坐标(11,11)处红色通道的值:", img.item(11, 11, 2))

print("""  访问图像属性:  """)
# 图像属性包括行数，列数和通道数，图像数据类型，像素数等。
# 与一般的numpy.array一样，可以通过 img.shape 访问图像的形状。

# 它返回一组由图像的行、列和通道组成的元组（如果图象是彩色的）：
print("img.shape:{}".format(img.shape))  # (128,128,3)
# 注意 如果图像是灰度图像，则返回的元组仅包含行数和列数，因此它是检查加载的图像是灰度图还是彩色图的一种很好的方法。

# 通过 img.size 访问图像的总像素数：
print("图像的总像素数:{}".format(img.size))  # 49152
# 注意 img.dtype 在调试时非常重要，因为 OpenCV—Python 代码中的大量错误是由无效的数据类型引起的。

# 图像数据类型可以由 img.dtype 获得：
print("图像数据类型:{}".format(img.dtype))  # UINT8
namedShow("img", img)

"""  图像中的感兴趣区域:  """
# 有时，您将不得不处理某些图像区域。对于图像中的眼部检测，在整个图像上进行第一次面部检测。
# 当获得面部时，我们单独选择面部区域并在其内部搜索眼部而不是搜索整个图像。
# 它提高了准确性（因为眼睛总是在脸上：D）和性能（因为我们在一个小区域搜索）。

# 使用 Numpy 索引再次获得 ROI（感兴趣区域）。并将其复制到图像中的另一个区域：

ball = img[5:15, 7:17]
# img[5:15, 7:17]是一个图像切片表达式，通常用于NumPy数组（通常用于存储图像数据）。这个表达式表示从图像中提取一个子区域。
# 5:15 表示从第5行到第15行（不包括15行）的区域。
# 7:17 表示从第7列到第17列（不包括17列）的区域。
img[66:76, 88:98] = ball
namedShow("image", img)

# 检查以下结果：
# 图像基本操作
# 拆分和合并图像通道
# 有时您需要在 B，G，R 通道图像上单独工作。在这种情况下，您需要将 BGR 图像分割为单个通道。
# 在其他情况下，您可能需要将这些单独的通道连接到 BGR 图像。您可以通过以下方式完成：
# b, g, r = cv.spilt(img)
b, g, r = cv.split(img, None)
img = cv.merge((b, g, r))
# 或者使用numpy.array的切片方法
b = img[:, :, 0]
# 假设您要将所有红色像素设置为零，则无需先拆分通道。Numpy 索引更快：
img[:, :, 2] = 0
# 警告
# cv.spilt()是一项代价高昂的操作（就时间而言）。所以只有在你需要时才这样做，否则就使用 Numpy 索引。

# 制作图像边界（填充）
# 如果要在图像周围创建边框，比如相框，可以使用 cv.copyMakeBorder()。但它有更多卷积运算，零填充等应用。该函数采用以下参数：
# src-输入的图像
# top,bottom,left,right-上下左右四个方向上的边界拓宽的值
# borderType-定义要添加的边框类型的标志。它可以是以下类型：

# cv.BORDER_CONSTANT- 添加一个恒定的彩色边框。该值应作为下一个参数value给出。
# cv.BORDER_REFLECT-边框将是边框元素的镜像反射，如下所示：fedcba|abcdefgh|hgfedcb
# cv.BORDER_REFLECT_101或者 cv.BORDER_DEFAULT-与上面相同，但略有改动，如下所示： gfedcb | abcdefgh | gfedcba
# cv.BORDER_REPLICATE -最后一个元素被复制，如下所示： aaaaaa | abcdefgh | hhhhhhh
# cv.BORDER_WRAP-不好解释，它看起来像这样： cdefgh | abcdefgh | abcdefg
# value- 如果边框类型为cv.BORDER_CONSTANT，则这个值即为要设置的边框颜色
# 下面是一个示例代码，演示了所有这些边框类型，以便更好地理解：
BLUE = [255, 0, 0]
img1 = cv.imread('./res/opencv-logo.png')
cv.cvtColor(src=img1, code=cv.COLOR_BGR2RGBA, dst=img1)
replicate = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)
plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, "gray"), plt.title('CONSTANT')
plt.show()
# 请参阅下面的结果。（图像是通过 matplotlib 展示的。因此红色和蓝色通道将互换）：
