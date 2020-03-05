# 日期：2020-03-05
# 作者：YangZai
# 功能：字典的创建，遍历，修改，删除

# 6-1 创建字典-人
human = {'first_name' : 'Xu', 'last_name' : 'Zeshan', 'age' : 18, 'city' : 'Dongguan'}
print(human['first_name'])
print(human)
print()

# 6-2 喜欢的数字
numbers = {'YangZai' : 7, 'Monkey' : 18, 'WenZhicong' : 8, 'Feason' : 6, 'ZhengBingchun' : 17}
print('YangZai\'s favorite number is ' + str(numbers['YangZai']))
print('Monkey\'s favorite number is ' + str(numbers['Monkey']))
print('WenZhicong\'s favorite number is ' + str(numbers['WenZhicong']))
print('Feason\'s favorite number is ' + str(numbers['Feason']))
print('ZhengBingchun\'s favorite number is ' + str(numbers['ZhengBingchun']))
print()

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
print('新型类：' + vocabulary['新型类'])
print()

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
	print(river.title(), end = ',')
print('\nAll countries:', end = ' ')
for country in set(rivers.values()) :
	print(country.title(), end = ',')
