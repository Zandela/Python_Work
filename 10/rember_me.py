# coding=utf-8

# 日期：2020-03-11
# 作者：YangZai
# 功能：验证用户

# 10-13 验证用户
import json

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username = input('What is your name?')
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	username = get_stored_username()
	if username:
		flag = input(username + ', are you?(y/n):')
		if flag.lower() == 'n':
			get_new_username()
		else:
			print('Welcome back, ' + username + '!')
	else:
		username = get_new_username()
		print("We'll remeber you when you come back, " + username + '!')

greet_user()