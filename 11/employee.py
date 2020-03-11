# coding=utf-8

# 日期：2020-03-12
# 作者：YangZai
# 功能：测试代码

# 11-3 雇员
class Employee():
	"""docstring for Employee"""
	def __init__(self, last_name, first_name, annual_salary):
		self.last_name = last_name
		self.first_name = first_name
		self.annual_salary = annual_salary

	def give_raise(self, add = 5000):
		self.annual_salary += add
		