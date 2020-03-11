# coding=utf-8

# 日期：2020-03-12
# 作者：YangZai
# 功能：测试代码

# 11-1 城市和国家
def city_function(city, country):
	city_country = city.title() + ', ' + country.title()
	return city_country

# 11-2 人口数量
def population_function_1(city, country, population):
	city_country_population = city.title() + ', ' + country.title() + ' - population ' + population
	return city_country_population

# 将形参population改为可选的
def population_function_2(city, country, population = ''):
	if population:
		city_country_population = city.title() + ', ' + country.title() + ' - population ' + population
	else:
		city_country_population = city.title() + ', ' + country.title()
	return city_country_population