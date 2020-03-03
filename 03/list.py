# 日期：2020-02-25
# 作者：YangZai
# 功能：列表的修改、删除和添加

# 3-1 列表
names = ['Chenweisheng', 'Xuzeshan', 'Feason', 'Wenzhicong']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

# 3-2 添加问候语
message = ",long time no see!"
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)
print(names[-1] + message)

# 3-3 通勤方式
commute = ['motorcycle.', 'car.', 'bicycle.', 'aircraft.']
declaration = 'I would like to own a Honda '
print(declaration + commute[0])
print(declaration + commute[1])
print(declaration + commute[2])
print(declaration + commute[-1])

# 3-4 嘉宾名单
guests = ['Chenweisheng', 'Xuzeshan', 'Feason', 'Wenzhicong']
invitation = ',invite you to dinner with me.'
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[-1] + invitation)

# 3-5 修改嘉宾名单
print(guests[-2] + " can't make an appointment!")
guests[1] = 'Xumanqi'
print(guests[1] + invitation)

# 3-6 添加嘉宾
print('I found a bigger table!')
guests.insert(0, 'Jiangwanting')
print(guests)
guests.insert(2, 'Wife')
print(guests)
guests.append('Zhengbingchun')
print(guests)
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[3] + invitation)
print(guests[4] + invitation)
print(guests[5] + invitation)
print(guests[-1] + invitation)

# 3-7 缩减名单
# pop()方法从末尾开始删除
print('Sorry, because the newly purchased table cannot be delivered in time, I can only invite two guests for dinner.')
guest = guests.pop()
print(guest + ",sorry i can't have dinner with you!")
guest = guests.pop()
print(guest + ",sorry i can't have dinner with you!")
guest = 'Chenweisheng'
guests.remove(guest)
print(guest + ",sorry i can't have dinner with you!")
guest = guests.pop(3)
print(guest + ",sorry i can't have dinner with you!")
guest = guests.pop(0)
print(guest + ",sorry i can't have dinner with you!")

print(guests[0] + ',you are still invited!')
print(guests[1] + ',you are still invited!')

del guests[0]
del guests[0]
print(guests)

# 3-8 组织列表
places = ['yueyanglou', 'qinghaihu', 'gugong', 'changcheng', 'qianmenlouzi']
print(places)
# sorted()对列表按字母顺序进行临时排序
print(sorted(places))
print(places)
# sorted()对列表按字母逆序进行临时排序
print(sorted(places, reverse = True))
print(places)
# reverse()反转列表
places.reverse()
print(places)
# 再反转列表
places.reverse()
print(places)
# sort()对列表按字母顺序进行永久排序
places.sort()
print(places)
# sort()对列表按字母逆序进行永久排序
places.sort(reverse = True)
print(places)

# len()指出嘉宾人数
print(len(guests))