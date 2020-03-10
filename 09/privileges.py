# coding=utf-8

# 日期：2020-03-10
# 作者：YangZai
# 功能：Admin,Privileges类

import user

# 权限
class Privileges():
	"""docstring for Privileges"""
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']
		
	def show_privileges(self):
		print('privileges:', end = ' ')
		for i in range(len(self.privileges)):
			print(self.privileges[i], end = ',\t')
		print()

# 管理员
class Admin(user.User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()