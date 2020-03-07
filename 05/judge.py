# 日期：2020-03-07
# 作者：YangZai
# 功能：判断if语句

# 5-1 条件测试
test = ['bbq', 'half', 'People']
for i in range(len(test)) :
	print(test[i] == 'half')
	print(test[i] != 'People')
print(test[2].lower() == 'people', end = '\n\n')

# 5-2 and、or多条件测试
age_01 = [56, 21, 6, 65, 12]
age_02 = [12, 4, 44, 43, 91]
for i in range(5) :
	if age_01[i] <= 22 and age_02[i] >= 68 :
		print('Yes')
	elif age_01[i] <= 22 or age_02[i] >= 68 :
		print('Maybe')
	else : 
		print('No')
# 检查特定值
print('12在列表1：' + str(12 in age_01))
print('21不在列表2：' + str(21 not in age_02), end = '\n\n')

# 5-3 外星人颜色
alien_color = 'red'
if alien_color == 'green' :
	print('玩家获得了5个点。', end = '\n\n')
alien_color = 'green'
if alien_color == 'green' :
	print('玩家获得了5个点。', end = '\n\n')

# 5-4 外星人颜色
alien_color = 'red'
if alien_color == 'green' :
	print('玩家获得了5个点。')
else :
	print('玩家获得了10个点。')
alien_color = 'green'
if alien_color == 'green' :
	print('玩家获得了5个点。')
else :
	print('玩家获得了10个点。')
print()

# 5-5 外星人颜色
''' 函数
def color(alien_color):
	if alien_color == 'green' :
		print('玩家获得了5个点。')
	elif alien_color == 'yellow' :
		print('玩家获得了10个点。')
	elif alien_color == 'red' :
		print('玩家获得了15个点。')
'''
alien_color = 'red'
#color(alien_color)
if alien_color == 'green' :
	print('玩家获得了5个点。')
elif alien_color == 'yellow' :
	print('玩家获得了10个点。')
elif alien_color == 'red' :
	print('玩家获得了15个点。')
alien_color = 'yellow'
if alien_color == 'green' :
	print('玩家获得了5个点。')
elif alien_color == 'yellow' :
	print('玩家获得了10个点。')
elif alien_color == 'red' :
	print('玩家获得了15个点。')
alien_color = 'green'
if alien_color == 'green' :
	print('玩家获得了5个点。')
elif alien_color == 'yellow' :
	print('玩家获得了10个点。')
elif alien_color == 'red' :
	print('玩家获得了15个点。')
print()

# 5-6 人生不同的阶段
def phase(age):
	if age < 2:
		print('你是婴儿。')
	elif age >= 2 and age < 4:
		print('你正蹒跚学步。')
	elif age >= 4 and age < 13:
		print('你是儿童。')
	elif age >= 13 and age < 20:
		print('你是青少年。')
	elif age >= 20 and age < 65:
		print('你是成年人。')
	else:
		print('你是老年人。')
age = 5
phase(age)
age = 77
phase(age)
age = 64
phase(age)
age = 12
phase(age)
age = 22
phase(age)
print()

# 5-7 喜欢的水果
favorite_fruits = ['apple', 'mulberry', 'cantaloupe']
if 'banana' in favorite_fruits:
	print('You really like bananas!')
if 'apple' in favorite_fruits:
	print('You really like apples!')
if 'watermelon' in favorite_fruits:
	print('You really like watermelons!')
if 'cantaloupe' in favorite_fruits:
	print('You really like cantaloupes!')
if 'mulberry' in favorite_fruits:
	print('You really like mulberries!', end = '\n\n')

# 5-8 以特殊的方式跟管理员打招呼
users = ['admin', 'yangzai', 'xiao', 'he', 'wu']
for i in range(len(users)):
	if users[i] == 'admin':
		print('Hello admin, would you like to see a status report?')
	else:
		print('Hello ' + users[i].title() + ',thank you for logging in again.')
print()

# 5-9 处理没有用户的情形
users.clear()	#清空所有用户
if len(users) == 0:
	print('We need to find some users!')
else:
	for i in range(len(users)):
		if users[i] == 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print('Hello ' + users[i].title() + ',thank you for logging in again.')
print()

# 5-10 检查用户名
current_users = ['admin', 'yangzai', 'xiao', 'he', 'wu']
new_users = ['keng', 'Wu', 'yang', 'monkey', 'ADMIN']
flag = 0	#判断用户是否注册标志，0——未注册、1——已注册
# 例子1
for i in range(len(new_users)):
	for j in range(len(current_users)):
		if new_users[i].lower() == current_users[j].lower():
			flag = 1
		else:
			flag = 0
	if flag == 1:
		print('请重新输入别的用户名！')
	else:
		print(new_users[i] + '这个用户名未被使用。')
print()
# 例子2
for i in range(len(new_users)):
	for j in range(len(current_users)):
		if new_users[i].lower() == current_users[j].lower():
			flag = 1
	if flag == 1:
		print('请重新输入别的用户名！')
		flag = 0
	else:
		print(new_users[i] + '这个用户名未被使用。')
# 例子1和2在ADMIN上输出不同的原因是：例子1在第二个for循环里flag输出的是最后一个的比较结果
print()

# 5-11 序数
numbers = list(range(1,10))
print(numbers)
for i in numbers:
	if i == 1:
		print('1st、')
	elif i == 2:
		print('2nd、')
	elif i == 3:
		print('3rd、')
	elif i == len(numbers) and i > 3:
		print(str(i) + 'th')
	else:
		print(str(i) + 'th、')