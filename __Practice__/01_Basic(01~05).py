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
s_b1 = '12345'
s_b1 = bool(s_b1)
print(s_b1)
print(type(s_b1))
s_b2 = ''  #没有任何值时为fauls，只要有占位（即使是空格）也为ture
s_b2 = bool(s_b2)
print(s_b2)
print(type(s_b2))

# 列表
# 只要列表中有数据 那么强制类型转换为bool的时候 就返回True
l_b1 = ['吃饭','睡觉','打太极']
l_b1 = bool(l_b1)
print(l_b1)
print(type(l_b1))
# 如果列表中什么数据都没有的情况下 那么返回的是False
l_b2 = []
l_b2 = bool(l_b2)
print(l_b2)
print(type(l_b2))

# 只要元组中有数据 那么强制类型转换为bool的时候 就会返回True
y_b1 = ('吃饭','睡觉','打太极')
y_b1 = bool(l_b1)
print(y_b1)
print(type(y_b1))
# 如果元组中没有数据的话 那么就返回False
y_b2 = []
y_b2 = bool(y_b2)
print(y_b2)
print(type(y_b2))

# 字典，字典就是key和volum
# 只要字典中有内容 那么在强制类型转换为bool的时候 就会返回True
d_b1 = {'阿丁':'暴躁菠萝头',
        '阿邦':'开开心心坐大牢'}
print(d_b1)
d_b1 = bool(d_b1)
print(d_b1)
print(type(d_b1))

# 如果在字典中没有数据的话 那么返回的就是False

d_b2 = {}
print(d_b2)
d_b2 = bool(d_b2)
print(d_b2)
print(type(d_b2))

# 什么情况下是False
# print(bool(0))
# print(bool(0.0))
# print(bool(''))
# print(bool(""))
# print(bool([]))
# print(bool(()))
# print(bool({}))

# 05_运算符

a = 3
b = 4

# 加,减,乘,除,取整数，取余数
print(a+b,a-b,b-a,a*b,a/b,b/a,a//b,b//a,a%b,b%a)
# 指数
print(a ** b, b ** a)
# 优先级
print((a + b) * 2)

# 字符串的加法为拼接，并且要两边是字符串才可以相加
a = '春天正是读书天'
b = '夏日炎炎睡不着'
c = 123
d = 0.123
e = True
print(type(a),type(b),type(c),type(d),type(e))
print(a + b)
# print(a + c)
# print(a + d)
# print(a + e)
print(a + str(d)) # 以上全军覆没，这个OK
# 字符串的乘法是重复
print((a + b) * 3)

# -------------------------------- 赋值运算符 --------------------------------
a = 5
print(a)

# 会显示最终值
b = c = 10
print(b)
print(c)

# 多个变量赋值用逗号分开
d,e,f = '^',1,0.5
print(d,e,f)

# -------------------------------- 复合运算符 --------------------------------
a = 1
a = a + 3
print(a)
# +=运算：将值加算后带入
a += 1
print(a)
# *=运算：将值相乘后带入
a *= 2
print(a)
# -=运算：将值减去后带入
a -= 1
print(a)
# /=运算：将数除去后带入（除尽则保留.0，除不尽则保留小数点后16位
a /= 3
print(a) 
# //=运算：将数整除后带入（保留小数点前整数+.0）
a //= 1
print(a)
a //= 2
print(a)
# %=运算：将数除去后取余数
b = 7
b %= 5
print(b)
# *=运算：冥运算，求次冥后带入
c = 2
c **= 3
print(c)
# +=  -+  *=  /=  //=  %=  **=

# -------------------------------- 比较运算符 --------------------------------
# 比较符运算返回的都是boolean的数据

# ==恒等，判断==两边的变量是否一致
print(a == c)
# !=不等，判断!=两边的变量是否不一致
print(a != c)
# >大于，判断是否左边变量大于右边变量
print(a > b)
# >=大于等于，判断左边变量是否大于等于右边变量
print(a >= b)
print(b >= a)
# <小于，判断左边变量是否小于右边变量
print(a < c)
print(c < a)
# <=小于等于，判断左边变量是否小于等于右边变量
print(a <= c)
print(c <= a)

# 比较运算符  ==  !=  > >= < <=


# -------------------------------- 逻辑运算符 --------------------------------
# 与或非（and,or,not）

# and 与，条件需全部满足
# 所有的数据必须都是true，才会返回true。若某个数据为false，则全体判断为false。若所有数据为false，则全体判断为false。
print(5 > 2 and 2 > 1 and 0 < 1) # true
print(5 > 2 and 5 > 7 and 1 < 2) # false

# or 或，条件有一项满足
# 所有的数据，只要有一项为true，则整体判断为true。所有数据必须都是false，才会整体判断为false。
print(1 > 5 or 1 > 10 or 1 >= 1) # true
print(3 > 5 or 1 > 2 or 9 > 100 or 2 > 7) #false

# not 非，判断为相反结果，true为false，false为true
print(not True) # true => false
print(not False) # false => true
print(not (2 > 3)) # false => true
print(not (6 > 5)) # true => false

# not and 与非：有一项为false，则整体判断为true
print(not ('123' and 5 < 1 and 9 > 2)) # 有一项为false，and语句判别为true，所以not最终判别为true
print(not ( 1 == 1 and 6 >= 3 and 5 > 1 )) # 全为true，and语句判别为true，所以not最终判别为false

# not or 或非：有一项为true，则整体判断为false
print(not (10 > 1 or 2 < 3)) # 有一项为true，or语句判别为true，所以not最终判别为false
print(not (1 > 6 or 1 >5))  # 全为false，or语句判别为false，所以not最终判别为true