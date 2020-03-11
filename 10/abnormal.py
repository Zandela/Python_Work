# coding=utf-8

# 日期：2020-03-11
# 作者：YangZai
# 功能：异常处理

# 10-6 加法运算，处理TypeError异常
try:
	print('请输入两个数字')
	n1 = input('第一个：')
	n2 = input('第二个：')
	sum = int(n1) + int(n2)
# int()引发的是ValueError异常
# 两个不同类型相加才会引发TypeError异常
except ValueError:
	print('输入数据类型有误！')
else:
	print('相加等于' + str(sum))
print()

# 10-7 加法计算器
while True:
	try:
		print('请输入两个数字')
		n1 = input('第一个：')
		n2 = input('第二个：')
		sum = float(n1) + float(n2)
	except ValueError:
		print('输入数据类型有误！请重新输入。')
	else:
		print('相加等于' + str(sum))
		break
print()

# 10-8 猫和狗
filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'
try:
	with open(filename_1) as file_object_1:
		contents_1 = file_object_1.read()
		print(contents_1)
	with open(filename_2) as file_object_2:
		contents_2 = file_object_2.read()
		print(contents_2)
except FileNotFoundError:
	print('访问的文件不存在！\n')

# 10-9 沉默的猫和狗
filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'
try:
	with open(filename_1) as file_object_1:
		contents_1 = file_object_1.read()
		print(contents_1)
	with open(filename_2) as file_object_2:
		contents_2 = file_object_2.read()
		print(contents_2)
except FileNotFoundError:
	pass

# 10-10 常见单词
filename = 'The Training of Wild Animals by Frank Charles Bostock.txt'

with open(filename) as file_object:
	contents = file_object.read()

number = contents.lower().count('the')
print('the出现的次数：' + str(number) + '次')