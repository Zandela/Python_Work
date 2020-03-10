# coding=utf-8

# 日期：2020-03-11
# 作者：YangZai
# 功能：导入Python标准库模块collections中的OrderedDict类

# 9-13 使用OrderedDict，添加与输出的顺序一致
from collections import OrderedDict

dict = OrderedDict()
dict['对象'] = '变量可以引用的东西。现在你将对象和值等价使用。'
dict['序列'] = '一个有序的值的集合，每个值通过一个整数索引标识。'
dict['元素'] = '序列中的一个值'
dict['切片'] = '以索引范围指定的字符串片段。'
dict['不可变'] = '元素不能被改变的序列的性质。'
for key, value in dict.items() :
	print(key + '：' + value)

# 自己创建的OrderedDict类无法使添加和输出的顺序一致，这是为什么？
'''
class OrderedDict():
	"""docstring for OrderedDict"""
	def __init__(self, vocabulary):
		self.vocabulary = vocabulary
		
	def add(self, key, value):
		self.vocabulary[key] = value

	def show(self):
		for key, value in self.vocabulary.items() :
			print(key + '：' + value)

	def del_key(self, key):
		del self.vocabulary[key]

vocabulary = {
	'对象' : '变量可以引用的东西。现在你将对象和值等价使用。',
	'序列' : '一个有序的值的集合，每个值通过一个整数索引标识。',
	'元素' : '序列中的一个值',
	'切片' : '以索引范围指定的字符串片段。',
	'不可变' : '元素不能被改变的序列的性质。'
	}
vocabulary = {}
# 创建OrderedDict实体类
dict = OrderedDict()
dict.show()
'''