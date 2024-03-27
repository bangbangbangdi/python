# 单行注释
# 多行注释
"""
123
123
"""

'''
weqwe
'''

# 02_数据类型
# 变量
a = 'Hello World!'
a = 'Hello, world.'
b = "hello world."
print(a)
print(b)
# -------------------------------- 数据类型 --------------------------------
# Number     数值
#      int
ai = 123
bi = 12311.123
print(ai,bi)
print(ai,   bi)
print(ai,
      bi)
# print函数内换行 /n
print(f"{ai}\n{bi}")

#      float
af = 1.23
print(af)

# boolean    布尔
# 首字母大写！！！
ab = True
bb = False
print(f'{ab}\n{bb}')

# string     字符串
# 字符串 使用的是单引号 或者双引号
# 不允许一单一双 屌丝写法
ast = 'as不能用，好像是个函数'
bst = "吃好喝好，长生不老"
print(ast)
print(bst)
# 单引号和双引号的嵌套，内测的引号会被自动识别成字符串
cst = '"早睡早起身体好"'
dst = "'可惜暂时做不到'"
print(cst), print(dst)
# 单引号套单引号  双引号套双引号
# 不可行，报错了
# est = ''看什么看''
# fst = ""NO!""
# print(est), print(fst)


# -------------------------------- 查看数据类型 --------------------------------
# 变量没有类型,数据才有类型
# type方法判断变量的数据类型
# 格式：type（变量）
# int
dai = 9090
print(dai)
print(type(dai))

# float
daf = 0.141392
print(f'{daf}n\{type(daf)}') #成了！

# boolean
dab = ab
dbb = bb
print(dab)
print(type(dab))
print(dbb)
print(type(dbb))

# string
print(type(ast))


# 1. 标识符由字母、下划线和数字组成，且数字不能开头。
# 2. 严格区分大小写。
# 3. 不能使用关键字。


# -------------------------------- 转换为整型 --------------------------------
# str --> int
str1 = '999'
si1 = int(str1)
print(si1)
print(type(si1))


# float --> int
flo1 = 0.1191
flo1 = int(flo1)
print(flo1)
print(type(flo1))

# boolean --> int
print(type(ab))
ab = int(ab)
print(type(ab))
print(ab)

aaa = False
print(type(aaa))
aaa = int(aaa)
print(type(aaa))
print(aaa)

# 123.456 和 12ab 字符串，都包含非法字符，不能被转换成为整数，会报错

# -------------------------------- 转换为浮点数 --------------------------------
# int --> float
# str --> float
# boolean -->float


# -------------------------------- 转换为字符串 --------------------------------
# int --> str
# float --> str
# boolean -->str

# -------------------------------- 转换为布尔类型 --------------------------------
# 如果对非0的整数(int 包含正数和负数)进行bool类型的转换 那么就全都是True
# 在整数的范围内 0强制类型转换为bool类型的结果是false
# 浮点数
# 将浮点数转换为bool类型的数据的时候  正的浮点数和负的浮点数的结果是true
# 如果是0.0 那么结果是false
# 字符串
# 只要字符串中有内容 那么在强制类型转换为bool的时候 那么就返回True
# 列表
# 只要列表中有数据 那么强制类型转换为bool的时候 就返回True
# 如果列表中什么数据都没有的情况下 那么返回的是False
# 只要元组中有数据 那么强制类型转换为bool的时候 就会返回True
# 如果元组中没有数据的话 那么就返回False
# 字典
# 只要字典中有内容 那么在强制类型转换为bool的时候 就会返回True
# 如果在字典中没有数据的话 那么返回的就是False
# 什么情况下是False
# print(bool(0))
# print(bool(0.0))
# print(bool(''))
# print(bool(""))
# print(bool([]))
# print(bool(()))
# print(bool({}))