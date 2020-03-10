# coding=utf-8

# 日期：2020-03-10
# 作者：YangZai
# 功能：导入privileges模块

# 9-12 多个模块
from privileges import Admin

wudi = Admin('WU', 'DI')
wudi.privileges.show_privileges()