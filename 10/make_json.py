# coding=utf-8

# 日期：2020-03-11
# 作者：YangZai
# 功能：存储JSON数据

import json

# 10-11 喜欢的数字
filename = 'numbers.json'
while True:
	try:
		numbers = [int(input('请输入你喜欢的数字：'))]
		with open(filename, 'w') as file_object:
			json.dump(numbers, file_object)
	except ValueError:
		print('输入数字类型有误，请重新输入！')
	else:
		with open(filename) as file_object:
			num = json.load(file_object)
		print("I know your favorite number! It's " + str(num[0]))
		break

# 10-12 记住喜欢的数字
def get_num():
	try:
		with open(filename) as file_object:
			num = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return num

def new_num():
	num = get_num()
	if num:
		print("I know your favorite number! It's " + str(num[0]))
	else:
		numbers = [int(input('请输入你喜欢的数字：'))]
		with open(filename, 'w') as file_object:
			json.dump(numbers, file_object)

new_num()
# JSON文件存在内容为空，open()打开文件会使程序死机