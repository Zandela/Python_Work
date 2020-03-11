# coding=utf-8

# 日期：2020-03-12
# 作者：YangZai
# 功能：测试city_functions.py代码

import unittest

from city_functions import city_function
from city_functions import population_function_1
from city_functions import population_function_2

# 11-1 测试city_function()函数
class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		city_country = city_function('sanriago', 'chile')
		self.assertEqual(city_country, 'Sanriago, Chile')

unittest.main()

# 11-2 测试population_function_1()函数
class PopulationTestCase(unittest.TestCase):
	def test_city_country(self):
		city_country = population_function_1('sanriago', 'chile', '5000000')
		self.assertEqual(city_country, 'Sanriago, Chile - population 5000000')

unittest.main()

# 11-3 测试population_function_2()函数
class PopulationTestCase(unittest.TestCase):
	def test_city_country(self):
		city_country = city_function('sanriago', 'chile')
		self.assertEqual(city_country, 'Sanriago, Chile')

	def test_city_country_population(self):
		city_country = population_function_2('sanriago', 'chile', '5000000')
		self.assertEqual(city_country, 'Sanriago, Chile - population 5000000')

unittest.main()