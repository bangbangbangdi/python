# -------------------------------- 转换为整型 --------------------------------
# str --> int
# a = '123'
# print(type(a))
# # 将字符串转换为整数
# b = int(a)
# print(type(b))

# float --> int
# a = 1.63
# print(type(a))
# 如果我们将float转为整数 那么会返回的是小数点前面的数据
# b = int(a)
# print(b)
# print(type(b))

# boolean --> int
# 强制类型转换为谁 就写什么方法
# True ---> 1   False ---> 0
# a = False
# print(type(a))
# b = int(a)
# print(b)
# print(type(b))


# 123.456 和 12ab 字符串，都包含非法字符，不能被转换成为整数，会报错
# 以下 如果字符串当中包含了非法的字符 则报错
# a = '1.23'
# print(type(a))
# b = int(a)
# print(b)

# a = '12ab'
# print(type(a))
# b = int(a)
# print(b)

# -------------------------------- 转换为浮点数 --------------------------------
# a = '12.34'
# print(type(a))
# 将字符串类型的数据转换为浮点数
# b = float(a)
# print(b)
# print(type(b))


a = 666
print(a)
print(type(a))

b = float(a)
print(b)
print(type(b))
# -------------------------------- 转换为字符串 --------------------------------
# 整数转换为字符串
# a = 80
# print(type(a))
# # 强制类型转换为字符串的方法是str()
# b = str(a)
# print(b)
# print(type(b))

# 浮点数转换为字符串
# a = 1.2
# print(type(a))
# b = str(a)
# print(b)
# print(type(b))

# 布尔类型转换为字符串
# a = True
# print(type(a))
# b = str(a)
# print(b)
# print(type(b))

# -------------------------------- 转换为布尔类型 --------------------------------
# 如果对非0的整数(int 包含正数和负数)进行bool类型的转换 那么就全都是True
# a = 1
# print(type(a))
# 将整数变成布尔类型的数据
# b = bool(a)
# print(b)
# print(type(b))

# a = -1
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = 0
# print(type(a))
# 在整数的范围内 0强制类型转换为bool类型的结果是false
# b = bool(a)
# print(b)
# print(type(b))

# 浮点数
# 将浮点数转换为bool类型的数据的时候  正的浮点数和负的浮点数的结果是true
# 如果是0.0 那么结果是false
# a = 1.0
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = -1.0
# # print(type(a))
# # b = bool(a)
# # print(b)
# # print(type(b))

# a = 0.0
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 字符串
# 只要字符串中有内容 那么在强制类型转换为bool的时候 那么就返回True
# a = '网红截聊天的图'
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = '     '
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = ''
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = ""
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 列表
# 只要列表中有数据 那么强制类型转换为bool的时候 就返回True
# a = ['鹿晗','张艺兴','黄子韬']
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 如果列表中什么数据都没有的情况下 那么返回的是False
# a = []
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 元组
# 只要元组中有数据 那么强制类型转换为bool的时候 就会返回True
# a = ('李逵','林冲','卢俊义','武松','潘金莲')
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 如果元组中没有数据的话 那么就返回False
# a = ()
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 字典
# 只要字典中有内容 那么在强制类型转换为bool的时候 就会返回True
# a = {'name':'武大郎'}
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 如果在字典中没有数据的话 那么返回的就是False
# a = {}
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 什么情况下是False
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
