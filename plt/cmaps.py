import matplotlib.pyplot as plt

cmaps = plt.colormaps()
print("所有cmap：")
# 打印每个颜色映射
for i, cmap in enumerate(cmaps):
    print(f"Color Map{i+1}: {cmap}")