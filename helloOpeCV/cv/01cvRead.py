# _*_ coding : utf-8 _*_
import cv2
import numpy as np
from matplotlib import pyplot as plt


def reads(image_path="./res/pxArt.png"):
    # 读取原始图像
    anydepth = cv2.imread(image_path, cv2.IMREAD_ANYDEPTH)
    color = cv2.imread(image_path, cv2.IMREAD_COLOR)
    grayscale = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    ignore_orientation = cv2.imread(image_path, cv2.IMREAD_IGNORE_ORIENTATION)
    load_gdal = cv2.imread(image_path, cv2.IMREAD_LOAD_GDAL)
    reduced_color_2 = cv2.imread(image_path, cv2.IMREAD_REDUCED_COLOR_2)
    reduced_color_4 = cv2.imread(image_path, cv2.IMREAD_REDUCED_COLOR_4)
    reduced_color_8 = cv2.imread(image_path, cv2.IMREAD_REDUCED_COLOR_8)
    reduced_grayscale_2 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_2)
    reduced_grayscale_4 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)
    reduced_grayscale_8 = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_8)
    unchanged = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    # BRG 转 RGB
    anydepth = cv2.cvtColor(src=anydepth, code=cv2.COLOR_BGR2RGB)
    color = cv2.cvtColor(src=color, code=cv2.COLOR_BGR2RGB)
    grayscale = cv2.cvtColor(src=grayscale, code=cv2.COLOR_BGR2RGB)
    ignore_orientation = cv2.cvtColor(src=ignore_orientation, code=cv2.COLOR_BGR2RGB)
    load_gdal = cv2.cvtColor(src=load_gdal, code=cv2.COLOR_BGR2RGB)
    reduced_color_2 = cv2.cvtColor(src=reduced_color_2, code=cv2.COLOR_BGR2RGB)
    reduced_color_4 = cv2.cvtColor(src=reduced_color_4, code=cv2.COLOR_BGR2RGB)
    reduced_color_8 = cv2.cvtColor(src=reduced_color_8, code=cv2.COLOR_BGR2RGB)
    reduced_grayscale_2 = cv2.cvtColor(src=reduced_grayscale_2, code=cv2.COLOR_BGR2RGB)
    reduced_grayscale_4 = cv2.cvtColor(src=reduced_grayscale_4, code=cv2.COLOR_BGR2RGB)
    reduced_grayscale_8 = cv2.cvtColor(src=reduced_grayscale_8, code=cv2.COLOR_BGR2RGB)
    unchanged = cv2.cvtColor(src=unchanged, code=cv2.COLOR_BGR2RGB)
    # 使用plt显示
    fig, axs = plt.subplots(nrows=3, ncols=5, figsize=(20, 20))
    axs[0, 0].set_title('anydepth'), axs[0, 0].imshow(anydepth)
    axs[0, 1].set_title('color'), axs[0, 1].imshow(color)
    axs[0, 2].set_title('grayscale'), axs[0, 2].imshow(grayscale)
    axs[0, 3].set_title('ignore_orientation'), axs[0, 3].imshow(ignore_orientation)
    axs[0, 4].set_title('load_gdal'), axs[0, 4].imshow(load_gdal)
    axs[1, 0].set_title('reduced_color_2'), axs[1, 0].imshow(reduced_color_2)
    axs[1, 1].set_title('reduced_color_4'), axs[1, 1].imshow(reduced_color_4)
    axs[1, 2].set_title('reduced_color_8'), axs[1, 2].imshow(reduced_color_8)
    axs[1, 3].set_title('reduced_grayscale_2'), axs[1, 3].imshow(reduced_grayscale_2)
    axs[1, 4].set_title('reduced_grayscale_4'), axs[1, 4].imshow(reduced_grayscale_4)
    axs[2, 0].set_title('reduced_grayscale_8'), axs[2, 0].imshow(reduced_grayscale_8)
    axs[2, 1].set_title('unchanged'), axs[2, 1].imshow(unchanged)

    # 通道分离
    img = unchanged
    b, g, r = cv2.split(img)
    # 创建与image相同大小的零矩阵
    zeros = np.zeros(img.shape[:2], dtype="uint8")
    channel_r = cv2.merge([r, zeros, zeros])
    channel_g = cv2.merge([zeros, g, zeros])
    channel_b = cv2.merge([zeros, zeros, b])
    channel_rg = cv2.merge([r, g, zeros])
    channel_rb = cv2.merge([r, zeros, b])
    channel_gb = cv2.merge([zeros, g, b])
    axs[2, 2].set_title('r')
    axs[2, 2].imshow(channel_r)
    axs[2, 3].set_title('g')
    axs[2, 3].imshow(channel_g)
    axs[2, 4].set_title('b')
    axs[2, 4].imshow(channel_b)
    # 显示
    plt.show()
    pass


if __name__ == '__main__':
    reads()
