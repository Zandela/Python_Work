# 日期：2020-03-05
# 作者：YangZai
# 功能：字典的创建，遍历，修改，删除

# 6-1 创建字典-人
human = {'first_name' : 'Xu', 'last_name' : 'Zeshan', 'age' : 18, 'city' : 'Dongguan'}
print(human['first_name'])
print(human, end = '\n\n')

# 6-2 喜欢的数字
numbers = {'YangZai' : 7, 'Monkey' : 18, 'WenZhicong' : 8, 'Feason' : 6, 'ZhengBingchun' : 17}
print('YangZai\'s favorite number is ' + str(numbers['YangZai']))
print('Monkey\'s favorite number is ' + str(numbers['Monkey']))
print('WenZhicong\'s favorite number is ' + str(numbers['WenZhicong']))
print('Feason\'s favorite number is ' + str(numbers['Feason']))
print('ZhengBingchun\'s favorite number is ' + str(numbers['ZhengBingchun']), end = '\n\n')

# 6-3 词汇表
vocabulary = {
	'字典' : '一系列键—值对 。每个键 都与一个值相关联,你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。',
	'BDFL' : 'Benevolent Dictator For Life被指python的作者，直译过来为”终身的慈善独裁者“，大概是指作者一生都会免费慈善关注python，并在必要的时刻做出独裁决定。',
	'EAFP' : 'Easier to ask for forgiveness than permission. 这个是指python的一种编码规则，不管一个数据是否合法，一般先用try去执行，当except时再做处理。与之相对的是下面的LBYL。',
	'LBYL' : 'Look before you leap. 这个是与python相对的一种规则，在C语言中都是先去if判断，满足条件才会执行。相对于EAFP有一个缺点就是，当多线程时if判断条件满足后，但是其他线程修改了后依然不会满足，所以在python中EAFP相对会好一些。',
	'新型类' : '在python3种已经不存在经典类了，都属于新型类。python2种定义的时候从object继承的类为新型类，不是从object继承的为经典类。'
	}
print('字典：' + vocabulary['字典'])
print('BDFL：' + vocabulary['BDFL'])
print('EAFP：' + vocabulary['EAFP'])
print('LBYL：' + vocabulary['LBYL'])
print('新型类：' + vocabulary['新型类'], end = '\n\n')

# 6-4 for循环遍历词汇表
for key, value in vocabulary.items() :
	print(key + '：' + value)
print()
# 添加键-值对
vocabulary['loader'] = 'An object that loads a module. It must define a method named load_module(). A loader is typically returned by a finder. See PEP 302 for details and importlib.abc.Loader for an abstract base class. '
# 删除键-值对
del vocabulary['字典']
for key, value in vocabulary.items() :
	print(key + '：' + value)
print()
	
# 6-5 河流
rivers = {'nile' : 'egypt', 'yellow river' : 'china', 'mississippi' : 'america'}
for key, value in rivers.items() :
	print('The ' + key.title() + ' runs through ' + value.title() + '.')
print('All rivers:', end = ' ')
for river in set(rivers.keys()) :
	print(river.title(), end = ', ')
print('\nAll countries:', end = ' ')
for country in set(rivers.values()) :
	print(country.title(), end = ', ')

# 6-6 调查
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
list_survey = ['jen', 'john', 'neil', 'phil']
for name in favorite_languages.keys() :
	if name in list_survey :
		print(name.title() + ' in the dictionary.')
	else :
		print(name.title() + ' come to my survey.')
print()

# 6-7 嵌套——字典列表
human_02 = {'first_name' : 'Zhan', 'last_name' : 'Tianyou', 'age' : 108, 'city' : 'Heaven'}
human_03 = {'first_name' : 'Zhang', 'last_name' : 'Wuji', 'age' : 35, 'city' : 'Song'}
people = [human, human_02, human_03]
for i in range(3) :
	print(people[i])
print()

# 6-8 宠物
Andy = {'type' : 'dog', 'host' : 'Yang'}
Marly = {'type' : 'cat', 'host' : 'Zheng'}
Xixi = {'type' : 'cat', 'host' : 'Zhan'}
Honey = {'type' : 'dog', 'host' : 'Deng'}
pets = [Andy, Marly, Xixi, Honey]
for i in range(4) :
	print(pets[i])
print()

# 6-9 喜欢的地方——字典中存储列表
place_1 = ['Xiameng', 'Beijing']
place_2 = ['Yangzhou']
place_3 = ['Humeng', 'Taiwan', 'Henan']
favorite_places = {'Yang' : place_1, 'Hu' : place_2, 'Liu' : place_3}
for name, place in favorite_places.items() :
	print(name.title() + ' like ', end = '')
	for i in range(len(place)) :
		if i < len(place) - 1 :
			print(place[i], end = ', ')
		else :
			print(place[i], end = '.\n')
print()

# 6-10 喜欢的数字
numbers_1 = [7, 18]
numbers_2 = [10, 5, 8]
numbers_3 = [666, 2, 45]
numbers_4 = [6]
numbers_list = {
	'YangZai' : numbers_1,
	'Monkey' : numbers_2,
	'Feason' : numbers_3,
	'He' : numbers_4
}
for name, number in numbers_list.items() :
	print(name.title() + ' like ', end = '')
	for i in range(len(number)) :
		if i < len(number) - 1 :
			print(number[i], end = ', ')
		else :
			print(number[i], end = '.\n')
print()

# 6-11 城市——字典中存储字典
cities = {
	'Dongguan' : {
		'country' : 'china',
		'population' : '5000万',
		'fact' : '沐足'
	},
	'GuangZhou' : {
		'country' : 'china',
		'population' : '9000万',
		'fact' : '羊城'
	},
	'XiaMeng' : {
		'country' : 'china',
		'population' : '7000万',
		'fact' : '鼓浪屿'
	}
}
for city, details in cities.items() :
	print(city, end = ': ')
	for nature, result in details.items() :
		print(nature + ':' + result, end = ', ')
	print()