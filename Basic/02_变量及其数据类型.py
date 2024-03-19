# -------------------------------- 变量 --------------------------------
# 重复的值 书写/修改起来都很麻烦

# 在不使用变量的情况下
print('天気が良いから、散歩しましょう')
print('天気が良いから、散歩しましょう')
print('天気が良いから、散歩しましょう')
print('天気が良いから、散歩しましょう')
# 上述情况如果我们不想再散步了,就要修改四处地方;超级麻烦

# 在使用变量的情况下
# 变量的格式： 变量的名字 = 变量的值

sentence = 'もう2度と散歩したくない...'

print(sentence)
print(sentence)
print(sentence)
print(sentence)

# -------------------------------- 数据类型 --------------------------------
# Number     数值
#      int
#      float
# boolean    布尔
# string     字符串

# 变量类型的基本使用
# Number     数值
#      int
money = 5000
#      float
money1 = 1.2

# boolean    布尔
# 流程控制语句
# 性别的变量
# 性别在实际的企业级开发中 使用的单词是sex  gender
# 男  True
sex = True
gender = False

# string     字符串
# 字符串 使用的是单引号 或者双引号
s = '苍茫的大海上有一只海燕 你可长点心吧'
s1 = "嘀嗒嘀嗒嘀"
# 不允许一单一双 屌丝写法
# s2 = '哈哈哈"
# s3 = "呵呵呵'

# 单引号和双引号的嵌套
# s4 = '"嘿嘿嘿"'
# print(s4)
# s5 = "'嘿嘿'"
# print(s5)

# 单引号套单引号  双引号套双引号
s6 = ''行还是不行呢''
s7 = ""行还是不行呢""

# -------------------------------- 查看数据类型 --------------------------------
# 变量没有类型,数据才有类型
# int
# float
# boolean
# string
# type方法判断变量的数据类型
# 格式：type（变量）
# int
a = 1
print(a)
# <class 'int'>
print(type(a))

# float
b = 1.2
print(b)
# <class 'float'>
print(type(b))

# boolean
c = True
print(c)
# <class 'bool'>
print(type(c))


# string
d = '中国'
print(d)
# <class 'str'>
print(type(d))
