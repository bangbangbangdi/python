# -------------------------------- 字符串 --------------------------------
# - 获取长度:len                     len函数可以获取字符串的长度。
# - 查找内容:find                    查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次出现的开始位置索引值，如果不存在，则返回-1.
# - 判断:startswith,endswith        判断字符串是不是以谁谁谁开头/结尾
# - 计算出现次数:count                返回 str在start和end之间 在 mystr里面出现的次数
# - 替换内容:replace                 替换字符串中指定的内容，如果指定次数count，则替换不会超过count次。
# - 切割字符串:split                  通过参数的内容切割字符串
# - 修改大小写:upper,lower           将字符串中的大小写互换
# -  空格处理:strip                   去空格
# - 字符串拼接:join                   字符串拼接

# len  length的缩写  长度
s = 'china'
print(len(s))

s1 = 'china'
print(s1.find('a'))

s2 = 'china'
print(s2.startswith('h'))
print(s2.endswith('n'))

s3 = 'aaabb'
print(s3.count('b'))

s4 = 'cccdd'
print(s4.replace('c', 'd'))

s5 = '1#2#3#4'
print(s5.split('#'))

s6 = 'china'
print(s6.upper())

s7 = 'CHINA'
print(s7.lower())

s8 = '   a   '
print(len(s8))

print(len(s8.strip()))

s9 = 'a'
print(s9.join('hello'))
# -------------------------------- 列表 --------------------------------
# -------- 增 ---------
# append  追加   在列表的最后来添加一个对象/数据
food_list = ['铁锅炖大鹅', '酸菜五花肉']
print(food_list)

food_list.append('小鸡炖蘑菇')
print(food_list)

# insert  插入
char_list = ['a', 'c', 'd']
print(char_list)
# index的值就是你想插入数据的那个下标
char_list.insert(1, 'b')
print(char_list)

# extend 合并两个列表
num_list = [1, 2, 3]
num1_list = [4, 5, 6]

num1_list.extend(num_list)
num_list.extend(num1_list)
print(num_list)
print(num1_list)

# -------- 删 ---------
# a_list = [1,2,3,4,5]
#
# print(a_list)

# 根据下标来删除列表中的元素
# 爬取的数据中 有个别的数据 是我们不想要的 那么我们就可以通过下标的方式来删除
# del a_list[2]
# print(a_list)


# b_list = [1,2,3,4,5]
# print(b_list)
# pop是删除列表中的最后一个元素
# b_list.pop()
#
# print(b_list)


c_list = [1, 2, 3, 3, 4, 5]
print(c_list)

# 根据元素来删除列表中的数据
c_list.remove(3)
print(c_list)

# -------- 改 ---------
city_list = ['北京', '上海', '深圳', '武汉', '西安']

print(city_list)

# 将列表中的元素的值修改
# 可以通过下标来修改，注意列表中的下标是从0开始的
city_list[4] = '大连'
print(city_list)

# -------- 查 ---------
# in 是判断某一个元素是否在某一个列表中
# food_list = ['锅包肉','汆白肉','东北乱炖']

# 判断一下在控制台输入的那个数据 是否在列表中
# food = input('请输入您想吃的食物')
#
# if food in food_list:
#     print('在')
# else:
#     print('不在，一边拉去')


# not in

ball_list = ['篮球', '台球']

# 在控制台上输入你喜欢的球类 然后判断是否不在这个列表中
ball = input('请输入您喜欢的球类')

if ball not in ball_list:
    print('不在')
else:
    print('在')

# -------------------------------- 元组 --------------------------------
# a_tuple = (1,2,3,4)
#
# print(a_tuple[0])
# print(a_tuple[1])

# 元组是不可以修改里面的内容的
# a_tuple[3] = 5
# print(a_tuple)

# a_list = [1,2,3,4]
#
# print(a_list[0])
#
# a_list[3] = 5
# print(a_list)
# 列表中的元素是可以修改的 而元组中的元素是不可以被修改


a_tuple = (5)

print(type(a_tuple))

# 当元组中只要一个元素的时候  那么他是整型数据
# 定义只有一个元素的元组，需要在唯一的元素后写一个逗号
b_tuple = (5,)
print(type(b_tuple))
# -------------------------------- 切片 --------------------------------
s = 'hello world'

# 在切片中直接写一个下标
print(s[0])

# 左闭右开区间   包含坐标的数据 不包含右边的数据
print(s[0:4])

# 是从起始的值开始  一直到末尾
print(s[1:])

# 是下标为0的索引的元素开始 一直到第二参数为止   遵循左闭右开区间
print(s[:4])

# hello  world
# 从下标为0的位置开始 到下标为6的位置结束  每次增长2个长度
print(s[0:6:2])

# -------------------------------- 字典 --------------------------------
# -------- 增 ---------
person = {'name': '老马'}

print(person)

# 给字典添加一个新的key value
# 如果使用变量名字['键'] = 数据时  这个键如果在字典中不存在  那么就会变成新增元素
person['age'] = 18

# 如果这个键在字典中存在 那么就会变成这个元素
person['name'] = '阿马'

print(person)

# -------- 删 ---------
# (1) 删除字典中指定的某一个元素
person = {'name': '老马', 'age': 18}

# 删除之前
# print(person)
#
# del person['age']
#
# # 删除之后
# print(person)

# （2）删除整个字典
# 删除之前
# print(person)
#
# del person
#
# 删除之后
# print(person)


# clear
#   （3） 清空字典 但是保留字典对象
print(person)

# 清空指的是将字典中所有的数据 都删除掉  而保留字典的结构
person.clear()

print(person)

# -------- 改 ---------
person = {'name': '张三', 'age': 18}

# 修改之前的字典
print(person)

# 修改name的值为法外狂徒
person['name'] = '法外狂徒'

# 修改之后的字典
print(person)

# -------- 查 ---------
# 定义一个字典
person = {'name': 'kino', 'age': 16}

# 访问person的name
# print(person['name'])
# print(person['age'])

# 使用[]的方式，获取字典中不存在的key的时候  会发生异常   keyerror
print(person['gender'])

# 不能使用.的方式来访问字典的数据
# print(person.name)


# print(person.get('name'))
# print(person.get('age'))

# 使用.的方式，获取字典中不存在的key的时候  会返回None值 或者指定的默认值
print(person.get('gender', '未知'))


# -------- 遍历字典 ---------
# 遍历--》就是数据一个一个的输出

person = {'name':'阿马','age':18,'sex':'男'}

# (1) 遍历字典的key
# 字典.keys() 方法 获取的字典中所有的key值  key是一个变量的名字 我们可以随便起
# for key in person.keys():
#     print(key)

# (2) 遍历字典的value
# 字典.values()方法  获取字典中所有的value值   value也是一个变量 我们可以随便命名
# for value in person.values():
#     print(value)

# (3) 遍历字典的key和value
# for key,value in person.items():
#     print(key,value)


# (4) 遍历字典的项/元素
for item in person.items():
    print(item)
