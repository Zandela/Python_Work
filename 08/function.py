# coding=utf-8

# 日期：2020-03-09
# 作者：YangZai
# 功能：函数的定义，调用，形参和实参

# 8-1 消息
def display_message(message):
	print(message)

message = '本章学习函数。'
display_message(message)
print()

# 8-2 喜欢的图书
def favorite_book(title):
	print('One of my favorite book is ' + title + '.')
	
favorite_book('Alice in Wonderland')
print()

# 8-3 T恤
def make_shirt(size, sample):
	print(size + '码，字样：' + sample)

# 位置实参调用
make_shirt('L', 'YangZai')
# 关键字实参调用
make_shirt(sample = 'YangZai', size = 'XL')
print()

# 8-4 大号T恤，函数参数设置默认值
def make_big_shirt(size = 'XL', sample = 'I love Python'):
	print(size + '码，字样：' + sample)
	
# 默认字样和尺码T恤
make_big_shirt()
# 默认字样中号T恤
make_big_shirt('L')
# 印有其他字样的T恤（尺码无关紧要）
make_big_shirt(sample = 'YangZai')
print()

# 8-5 城市
def describe_city(name, country = 'china'):
	print(name.title() + ' is in ' + country.title())
	
describe_city('Dongguan')
describe_city('ShenZhen', 'China')
describe_city('Reykjavik', 'Iceland')
print()

# 8-6 城市名
def city_country(name, country):
	string = '"' + name.title() + ', ' + country.title() + '"'
	return string
	
s1 = city_country('dongguan', 'china')
s2 = city_country('jieyang', 'china')
s3 = city_country('Shenzhen', 'China')
print(s1)
print(s2)
print(s3)
print()

# 8-7 专辑，返回字典和设置可选参数
def make_album(singer, name, number=''):
	album = {'singer' : singer, 'name' : name}
	if number:
		album['number'] = number
	return album
	
album_1 = make_album('林俊杰', '和自己对话')
album_2 = make_album('陈鸿宇', '浓烟下的诗歌电台')
album_3 = make_album('林俊杰', '伟大的渺小', 2)
print(album_1)
print(album_2)
print(album_3)
print()

# 8-8 用户的专辑
print("(enter 'q' at any time to quit)")
while True:
	singer = input('Singer:')
	if singer == 'q':
		break
	name = input('Album Name:')
	if name == 'q':
		break

	album = make_album(singer, name)
	print(album)
print()

# 8-9 魔术师
# 显示列表
def show_magicians(magicians):
	print('Magicians:', end = ' ')
	if len(magicians) == 0:
		print('None.')
	for i in range(len(magicians)):
		if i == len(magicians) - 1:
			print(magicians[i], end = '.\n')
		else:
			print(magicians[i], end = ', ')

magicians = []
show_magicians(magicians)
magicians.append('YangZai')
show_magicians(magicians)
magicians.append('Yang')
show_magicians(magicians)
print()

# 8-10 了不起的魔术师
# 修改列表
def make_great(magicians):
	for i in range(len(magicians)):
		magicians[i] += '(the Great)' 
		
make_great(magicians)
show_magicians(magicians)
print()

# 8-11 不变的魔术师
# 向函数传递列表副本
def edit_magicians(edit_magicians):
	for i in range(len(edit_magicians)):
		edit_magicians[i] += '(the Great)' 
	return edit_magicians	
	
edit = edit_magicians(magicians[:])
show_magicians(magicians)
show_magicians(edit)
print()

# 8-12 三明治，传递任意数量的实参
def gather(*food):
	print('三明治的食材有：', end = ' ')
	for f in food:
		print(f, end = ', ')
	print()

gather('火腿', '洋葱')
gather('面包')
gather('番茄', '午餐肉', '生菜')
print()

# 8-13 用户简介，任意数量的关键字实参
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

my_profile = build_profile('zhan', 'tianyou',
							profession = 'programmer',
							age = 26,
							height = '173cm')
print(my_profile, end = '\n\n')

# 8-14 汽车
def build_car(manufacturer, model, **car_info):
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model
	for key, value in car_info.items():
		car[key] = value
	return car

my_car = build_car('subaru', 'outback', color = 'blue', tow_package = True)
print(my_car)