import matplotlib.pyplot as plt
import numpy as np
# 设置中文字符编码为 utf-8
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# 创建一个2x2的子图网格
fig, axs = plt.subplots(2, 2)

# 在左上角的子图上绘制一个简单的散点图
axs[0, 0].scatter([1, 2, 3], [4, 5, 6])
axs[0, 0].set_title('左上图')
axs[0, 0].set_xlabel('X')
axs[0, 0].set_ylabel('Y')

# 在右上角的子图上绘制一个简单的折线图
axs[0, 1].plot([1, 2, 3], [4, 5, 6])
axs[0, 1].set_title('右上图')
axs[0, 1].set_xlabel('X')
axs[0, 1].set_ylabel('Y')

# 在左下角的子图上绘制一个简单的柱状图
axs[1, 0].bar([1, 2, 3], [4, 5, 6])
axs[1, 0].set_title('左下图')
axs[1, 0].set_xlabel('X')
axs[1, 0].set_ylabel('Y')

# 在右下角的子图上绘制一个简单的饼图
axs[1, 1].pie([1, 2, 3], labels=['A', 'B', 'C'])
axs[1, 1].set_title('右下图')
axs[1, 1].set_xlabel('X')
axs[1, 1].set_ylabel('Y')

# # 为所有子图添加x轴和y轴标签
# for ax in axs.flat:
#     ax.set(xlabel='X Label', ylabel='Y Label')
# 为所有子图添加标题（可选）
# for i, j in np.ndenumerate(axs):
#     axs[i, j].set_title(f'Subplot[{i[0]},{j[0]}](http://example.com)')

plt.show()
