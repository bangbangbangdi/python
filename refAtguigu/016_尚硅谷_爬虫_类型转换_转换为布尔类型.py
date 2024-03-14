
# 如果对非0的整数(int 包含正数和负数)进行bool类型的转换 那么就全都是True
# a = 1
# print(type(a))
# 将整数变成布尔类型的数据
# b = bool(a)
# print(b)
# print(type(b))

# a = 2
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = -1
# print(type(a))
#
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
# a = ['吴亦凡','鹿晗','张艺兴','黄子韬']
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