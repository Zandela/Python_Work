# coding=utf-8

# 日期：2020-03-11
# 作者：YangZai
# 功能：文件的读取、写入、附加

# 10-1 读取learning_python.txt文件
filename = 'learning_python.txt'

# 读取整个文件，读取成字符串
with open(filename) as file_object:
	contents = file_object.read()
	print(contents)

# 遍历文件对象，读取成列表
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
print()

# 将各行存储在一个列表中
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
print()

# 10-2 替换learning_python.txt文件中的字符串'Python'成'C'输出在屏幕上
for line in lines:
	line = line.replace('Python', 'C')
	print(line.rstrip())
print()
# replace()的第3个参数代表替换的次数
print(contents.replace('Python', 'C', 2))

# 10-3 访客
name = input('Please tell me your name:')
filename = 'guest.txt'
# 对文件内容完全覆盖
with open(filename, 'w') as file_object:
	file_object.write(name)
print()

# 10-4 访客名单
filename = 'guest_book.txt'

print("enter 'q' quit")
while True:
	name = input('Please tell me your name:')
	if name == 'q':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(name + '\n')
			print('Hello, ' + name)
			
with open(filename) as file_object:
	guests = file_object.read()
	print(guests)
	
# 10-5 关于编程的调查
filename = 'survey.txt'

print("enter 'q' quit")
while True:
	cause = input('你为何喜欢编程？\n')
	if cause == 'q':
		print('感谢您的参与调查，谢谢！')
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(cause + '\n')

with open(filename) as file_object:
	print(file_object.read())
