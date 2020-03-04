# 日期：2020-03-04
# 作者：YangZai
# 功能：操作列表

# 4-1 比萨
pizzas = ['egg yolk shrimp pizza', 'hawaiian pizza', 'mashed potato pizza']
for pizza in pizzas:
    print('I like ' + pizza)
print('I really love pizza!\n')

# 4-2 动物
animals = ['cat', 'dog', 'bird']
for animal in animals:
	print('A ' + animal + ' would make a great pet')
print('Any of these animals would make a great pet!\n')

# 4-3 数到20
for value in range(1, 21):
	print(value)
print()

# 4-4 一百万
'''
values = []
for value in range(1, 1000001):
	values.append(value)
	print(value)
'''

# 4-5 计算1～1000000的总和
values = [value for value in range(1, 1000001)]
print(min(values))
print(max(values))
print(sum(values))
print()
# 用时0.5s

# 4-6 1～20的奇数
odds = [odd for odd in range(1, 21, 2)]
for value in odds:
	print(value)
print()

# 4-7 3～30被3整除的数字
numbers = [number for number in range(3, 31, 3)]
for value in numbers:
	print(value)
print()

# 4-7 3～30被3整除的数字
cubes = [cube ** 3 for cube in range(1, 11)]
for value in cubes:
	print(value)
print()

# 4-8 切片
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print('The first three items in the list are:')
print(my_foods[:3])
print('Three items form the middle of the list are:')
print(my_foods[1:4])
print('The last three items in the list are:')
print(my_foods[2:])
print()

# 4-9 你的比萨和我的比萨
friend_pizzas = pizzas[:]
pizzas.append('assorted sausage pizza')
friend_pizzas.append('chicken mushroom pizza')
print('My favorite pizzas are:')
for pizza in pizzas:
	print(pizza)
print('\nMy friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
	print(pizza)
# 注意：friend_pizzas = pizzas 行不通，结果会输出相同的列表
print()

# 4-13 元组
foods = ('扬州炒饭', '番茄鸡蛋面', '卤肉飯', '清蒸鲈鱼', '紫菜汤')
for food in foods:
	print(food)
# 尝试修改其中一个元素会发生错误
#foods[0] = '白饭'
foods = ('扬州炒饭', '番茄鸡蛋面', '紫菜泡饭', '清蒸鲈鱼', '鲫鱼汤')
print('\n修改后的菜单：')
for food in foods:
	print('\t' + food)