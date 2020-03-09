# coding=utf-8

# 日期：2020-03-09
# 作者：YangZai
# 功能：調用函数

import printing_fuctions as f

# 8-15 打印模型
f.print_model('Hello Python World!')

# 8-16 导入模块的方法
# import functions
# functions.draw_Star(400)

# from functions import draw_Star
# draw_Star(400)

# from functions import draw_Star as draw
# draw(400)

# import functions as fn
# fn.draw_Star(400)

from functions import *
draw_Star(400)