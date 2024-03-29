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
print(ai, bi)
print(ai, bi)
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
print(f'{daf}n\{type(daf)}')  # 成了！

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
a12 = 12
print(type(a12))
print(a12)
a12 = float(a12)
print(type(a12))
print(a12)
print('=========================')

# str --> float
b12 = '678'
b13 = '12ba'
# print(type(b12,b13)) # 写法错误，报错
# print(type(b12)(b13)) # 不报错，但是只显示b13的值
print(type(b12))
print(type(b13))
print(f'{b12}\n{b13}')
b12 = float(b12)
# b13 = float(b13) # 数字+字母非法了，转换不了
print(type(b12))
# print(type(b13)) # 非法，报错
print(f'{b12}\n{b13}')
print(type(b12))
print(type(b13))  # 没转换上，还是str

# boolean -->float
# 仍旧可以直接转换
a23 = False
a23 = float(a23)
print(type(a23))
print(a23)

# -------------------------------- 转换为字符串 --------------------------------
# int --> str
b12 = 996996
b12 = str(b12)
print(type(b12))
print(b12)

print('====================')

# float --> str
b11 = 1.12321
b11 = str(b11)
print(type(b11))
print(b11)

# boolean -->str
# 直接把Faslse和True转换为str，输出也为文字内容
b23 = True
b23 = str(b23)
print(type(b23))
print(b23)

# -------------------------------- 转换为布尔类型 --------------------------------
# 如果对非0的整数(int 包含正数和负数)进行bool类型的转换 那么就全都是True
# 在整数的范围内 0强制类型转换为bool类型的结果是false
i_b1 = 133
i_b2 = -2
i_b3 = 0
int_list = [i_b1, i_b2, i_b3]  # 企图偷懒但失败，留作日后课题
index = 0
for i in int_list:
    i = bool(i)
    print(i)
    print(type(i))
    int_list[index] = i
    index += 1

for i in int_list:
    print(type(i))

print('----------------')
# print(int_list)
# print(type(int_list))
print(type(i_b1), type(i_b2), type(i_b3))

print(i_b1, i_b2, i_b3)
# i_b1, i_b2, i_b3 = bool(i_b1,i_b2,i_b3) # NO
i_b1, i_b2, i_b3 = bool(i_b1), bool(i_b2), bool(i_b3)
print(type(i_b1), type(i_b2), type(i_b3))
print(i_b1, i_b2, i_b3)

# 浮点数
# 将浮点数转换为bool类型的数据的时候  正的浮点数和负的浮点数的结果是true
# 如果是0.0 那么结果是false
f_b1 = 1.25
f_b2 = 0.654
f_b3 = -1.56
f_b4 = -0.789
f_b5 = 0.0

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
