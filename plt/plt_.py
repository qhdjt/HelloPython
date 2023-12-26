# _*_ coding : utf-8 _*_
# @Time : 2023-06-09 12:49
# @Author : xcsg
# @File :plt
# @Project :opcv
# 生成一个二维随机数组
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    img = np.random.rand(10, 10)
    print(img.shape)
    # 绘制灰度图像
    plt.imshow(img,cmap="gray")
    # 显示图像
    plt.show()
