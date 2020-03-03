# 日期：2020-02-25
# 作者：YangZai

# 2-3 合并（拼接）字符串
name = 'Eric'
message = 'Hello ' + name + ',would you like to learn some Python today?'
print(message)

# 2-4 修改字符串大小写
name = 'Zhan tianyou'
# 首字母大写
print(name.title())
# 字母全部大写
print(name.upper())
# 字母全部小写
print(name.lower())

# 2-5 输出引号
message = 'Albert Einstein once said,"A person who never made a mistake never tried anyting new"'
print(message)

# 2-6 合并（拼接）字符串
famous_person = 'Albert Einstein'
saying = 'A person who never made a mistake never tried anyting new'
message = name + ' once said,"' + saying + '"'
print(message)

# 2-7 删除空白
name = "\n\tYangZai\t\n"
print(name)
print(name.strip())		# 两端空白
print(name.rstrip())	# 开头空白
print(name.lstrip())	# 末尾空白

# 2-8 数字8
print(3 + 5)
print(18 - 10)
print(2 * 4)
print(2 ** 3)
print(16 / 2)

# 2-9 数值转化为字符串
number = 7
message = 'My love number is ' + str(number)
print(message)

# Python之禅
import this