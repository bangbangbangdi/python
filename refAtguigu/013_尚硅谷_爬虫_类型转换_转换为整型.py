# 转换为整型
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
