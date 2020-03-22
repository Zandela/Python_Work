# -*- coding: utf-8 -*-

# 日期：2020-03-22
# 作者：YangZai
# 功能：绘制立方图

import matplotlib.pyplot as plt

number = 5001
x_values = list(range(1, number))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.BuPu,
	edgecolor = 'none', s = 40)
plt.plot(x_values, y_values, linewidth = 3)

# 设置图表标题并给坐标轴加上标签
plt.title("Cube Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Cube of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()