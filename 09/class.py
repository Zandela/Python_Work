# coding=utf-8

# 日期：2020-03-10
# 作者：YangZai
# 功能：类的创建和使用

# 9-1 餐馆
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
#		初始化类属性
		self.restaurant_name = restaurant_name
		self.cuisine_type_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print(self.restaurant_name + '\t' + self.cuisine_type_type)
	
	def open_restaurant(self):
		print('Restaurant is opening!')
	
	def set_number_served(self, number):
		self.number_served = number
		
	def inscrement_number_served(self):
		while self.number_served < 80:
			self.number_served += 1
	
# 创建实体类
my_restaurant = Restaurant('YangZai', 'Noodle')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print()

# 9-2 三家餐馆
restaurant_1 = Restaurant('中华小当家', '中餐馆')
restaurant_2 = Restaurant('老新亨手工面', '中餐馆')
restaurant_3 = Restaurant('意大利牛排', '西餐厅')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
print()

# 9-3 用户
class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
# 描述用户信息
	def describe_user(self):
		print(self.first_name.title() + ' ' + self.last_name.title())
# 问候用户
	def greet_user(self):
		print('Hello,', end = ' ')
		self.describe_user()
# 登录次数+1
	def inscrement_login_attempts(self):
		self.login_attempts += 1
# 重置登录次数
	def reset_login_attempts(self):
		self.login_attempts = 0
		
# 创建用户实体类
me = User('zhan', 'shiyang')
me.describe_user()
me.greet_user()
print()

# 9-4 就餐人数，设置默认值属性
my_restaurant.set_number_served(40)
print('我的餐馆就餐人数：' + str(my_restaurant.number_served))
my_restaurant.inscrement_number_served()
print('增加后我的餐馆就餐人数：' + str(my_restaurant.number_served))
print()

# 9-5 尝试登录次数
me.inscrement_login_attempts()
print(me.first_name + '登录次数：' + str(me.login_attempts))
me.inscrement_login_attempts()
me.inscrement_login_attempts()
me.inscrement_login_attempts()
print(me.first_name + '登录次数：' + str(me.login_attempts))
me.reset_login_attempts()
print(me.first_name + '登录次数：' + str(me.login_attempts))
print()

# 9-6 冰淇淋小店，继承餐馆类
class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, restaurant_name, cuisine_type, flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def show_flavors(self):
		print('flavors:', end = ' ')
		for i in range(len(self.flavors)):
			print(self.flavors[i], end = '\t')
		print()

my_icecreamstand = IceCreamStand('冰淇淋小屋', '冷饮店', ['草莓味', '苹果味'])
my_icecreamstand.show_flavors()
my_icecreamstand.flavors.append('香橙味')
my_icecreamstand.show_flavors()
print()

# 9-7 管理员，继承用户类
class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name, privileges):
		super().__init__(first_name, last_name)
		self.privileges = privileges
		
	def show_privileges(self):
		print('privileges:', end = ' ')
		for i in range(len(self.privileges)):
			print(self.privileges[i], end = ',\t')
		print()

admin = Admin('Chen', 'Guangchuan', ['can add post', 'can delete post', 'can ban user'])
admin.describe_user()
admin.show_privileges()
print()

# 9-8 权限
class Privileges():
	"""docstring for Privileges"""
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']
		
	def show_privileges(self):
		print('privileges:', end = ' ')
		for i in range(len(self.privileges)):
			print(self.privileges[i], end = ',\t')
		print()

class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

wudi = Admin('WU', 'DI')
wudi.privileges.show_privileges()
print()

# 9-9 电瓶升级
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print('This car has ' + str(self.odometer_reading) + ' miles on it.')

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery():
	"""docstring for Battery"""
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size
	
	def describe_battery(self):
		print('This car has a ' + str(self.battery_size) + '-kWh battery.')

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = 'This car can go approximately ' + str(range)
		message += ' miles on a full charge.'
		print(message)

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85

class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

my_car = ElectricCar('tesla', 'model s', 2016)
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()