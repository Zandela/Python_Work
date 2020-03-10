# coding=utf-8

# 日期：2020-03-10
# 作者：YangZai
# 功能：User类

# 用户
class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
# 描述用户信息
	def describe_user(self):
		print(self.first_name.title() + ' ' + self.last_name.title())
# 问候用户
	def greet_user(self):
		print('Hello,', end = ' ')
		self.describe_user()
# 登录次数+1
	def inscrement_login_attempts(self):
		self.login_attempts += 1
# 重置登录次数
	def reset_login_attempts(self):
		self.login_attempts = 0