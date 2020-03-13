# coding=utf-8

# 日期：2020-3-12
# 作者：YangZai
# 功能：设置类

class Settings ():
	"""存储《外星人入侵》的所有设置的类"""
	def __init__(self):
		'''初始化游戏的设置'''
		# 屏幕大小设置
		self.screen_width = 1200
		self.screen_height = 800
		#	设置背景颜色
		self.bg_color = (0, 0, 255)
		# 飞船设置
		self.ship_speed_factor = 1.5	#速度
		
		# 子弹设置
		self.bullet_speed_factor = 1	#速度
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3