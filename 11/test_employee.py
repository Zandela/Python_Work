# coding=utf-8

# 日期：2020-03-12
# 作者：YangZai
# 功能：测试employee.py代码

import unittest

from employee import Employee

# Employee类测试
class TestEmployee():
	"""针对Employee类测试"""
	def setUp(self):
		self.employee_1 = Employee('Guang', 'Chen', 6000)
		self.salary = 6000

	def test_give_default_raise(self):
		self.employee_1.give_raise()
		self.assertEqual(self.salary + 5000, self.employee_1.annual_salary)

	def test_give_custom_raise(self):
		self.employee_1.give_raise(3000)
		self.assertEqual(self.salary + 3000, self.employee_1.annual_salary)

unittest.main()