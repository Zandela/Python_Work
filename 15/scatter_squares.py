# -*- coding: utf-8 -*-

# 日期：2020-03-22
# 作者：YangZai
# 功能：绘制散点图

import matplotlib.pyplot as plt

# 绘制单个点
# plt.scatter(2, 4, s = 200)
# 绘制一系列点
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# edgecolor属性删除点的轮廓
# c属性自定义颜色
# 颜色映射(colormap)是一系列颜色：camp属性
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.BuPu,
	edgecolor = 'none', s = 40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()
# 在当前目录中存储图像
plt.savefig('square_plot.png', bbox_inches = 'tight')