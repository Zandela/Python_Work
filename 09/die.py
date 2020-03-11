# coding=utf-8

# 日期：2020-03-11
# 作者：YangZai
# 功能：摇骰子

from random import randint

class Die():
	def __init__(self, count, sides = 6):
		self.count = count
		self.sides = sides
# 摇点数
	def roll_die(self):
		self.count = randint(1, self.sides)
		print(self.count)
# 创建6面的骰子
die_1 = Die(0)
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
print()
# 创建10面的骰子
die_2 = Die(0, 10)
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
print()
# 创建20面的骰子
die_3 = Die(0, 20)
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
print()
