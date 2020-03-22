# -*- coding: utf-8 -*-

# 日期：2020-03-22
# 作者：YangZai
# 功能：绘制一个简单的折线图

import matplotlib.pyplot as plt

input_values = list(range(1, 6))
print(input_values)
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()