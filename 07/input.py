# coding=utf-8

# 日期：2020-03-07
# 作者：YangZai
# 功能：用户输入和while循环

# 7-1 汽车租赁
car = input('What kind of car do you want to rent?\n')
print('Let me see if I can find you a ' + car.title(), end = '\n\n')

# 7-2 餐馆订位
number = input('How many people dine?\n')
if int(number) > 8:
	print('Sorry, no more tables!', end = '\n\n')
else:
	print('Please, there is an empty table here.', end = '\n\n')

# 7-3 10的整数倍
flag = 0
number = input('请输入一个数字：')
flag = int(number) % 10
if flag == 0:
	print(number + '是10的整数倍', end = '\n\n')
else:
	print(number + '不是10的整数倍', end = '\n\n')

# 7-4 比萨配料
ingredients = []
ingredient = ''
while ingredient != 'quit':
	ingredient = input('请加入配料：')
	if ingredient != 'quit':
		print('我们会在比萨中加入' + ingredient)
		ingredients.append(ingredient)
	else:
		print('您加入的配料有：', end = '')
		for i in range(len(ingredients)):
			if i == len(ingredients) - 1:
				print(ingredients[i], end = '.\n\n')
			else:
				print(ingredients[i], end = ', ')

# 7-5 电影票
age = ''
while age != 'quit':
	age = input('请问您的年龄：')
	if age == 'quit':
		print('很荣幸为您服务，欢迎下次再来！')
		continue
	if int(age) < 3:
		print('欢迎您免费观影！')
	elif int(age) >= 3 and int(age) <= 12:
		print('欢迎您观看影片，票价为10美元。')
	elif int(age) > 12:
		print('欢迎您观看影片，票价为15美元。')
print()

# 7-7 无限循环
i = 6
while i > 0:
	print(i)
	i -= 1		#注释掉这行代码就会陷入无限循环，导致程序无法运行

# 7-8 熟食店
sandwich_orders = ['ham and cheese sandwich', 'tomato ham cheese sandwich', 'tuna sandwich']
finished_sandwiches = []
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made your ' + sandwich + '.')
	finished_sandwiches.append(sandwich)
print('以下三明治都做好了。')
for i in range(len(finished_sandwiches)):
	if i == len(finished_sandwiches) - 1:
		print(finished_sandwiches[i], end = '.\n\n')
	else:
		print(finished_sandwiches[i], end = ', ')

# 7-9 五香熏烟牛肉卖完了
sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'pastrami']
print('熟食店的五香熏烟牛肉卖完了！')
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)

# 7-10 梦想的度假胜地
places = {}
flag = True
while flag:
	name = input('\nWhat is your name?\n')
	if name in places.keys():
		print('您已接受調查，感谢您的参与！\n')
	else:
		place = input('If you could visit one place in the world, where would you go?\n')
		places[name] = place
	repeat = input('Would you like to let another person respond? (yes/no)\n')
	if repeat == 'no':
		flag = False
print('\n---------  RESULT  ---------')
for name, place in places.items():
	print(name.title() + ' would like to visit ' + place + '.')
