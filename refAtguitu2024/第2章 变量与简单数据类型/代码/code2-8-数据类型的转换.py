# 转换为整数int
# 字符串str-->整数int
# 纯数字的字符串
s = '2024'
n = int(s)
print(type(s), type(n))
# 浮点数float-->整数int
s1 = 2.23
print(int(s1))
# 布尔bool-->整数int
s2, s3 = True, False
print(int(s2),int(s3))


# 转换为浮点数float
# str-->float
s = '324.6' # 有没有小数点都可以
print(float(s))
# int-->float
n = 2024
print(float(n))
# bool-->float
print(float(s2), float(s3))



# 转换为布尔bool
# str-->bool
s = '0'
print(bool(s))
s1 = ''  # 空串
print('*'*20)
print(bool(s1))
# int-->bool
n=0
print(bool(n))
# float-->bool
f=0.0
print(bool(f))



# 转换为字符串str
# int-->str
n = 5
print(str(n))
print(type(str(n)))
# float -->str
f = 5.3
print(str(f))
print(type(str(f)))
# bool --> str
a = True
print(type(a))
print(type(str(a)))

# 进制的转换
s = '1a'
print(int(s, 16))