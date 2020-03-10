# coding=utf-8

# 日期：2020-03-10
# 作者：YangZai
# 功能：Restaurant类

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
#		初始化类属性
		self.restaurant_name = restaurant_name
		self.cuisine_type_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print(self.restaurant_name + '\t' + self.cuisine_type_type)
	
	def open_restaurant(self):
		print('Restaurant is opening!')
	
	def set_number_served(self, number):
		self.number_served = number
		
	def inscrement_number_served(self):
		while self.number_served < 80:
			self.number_served += 1