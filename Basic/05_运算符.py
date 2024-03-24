# -------------------------------- 算数运算符 --------------------------------
a = 3
b = 2

# print(a + b)
#
# print(a - b)
#
# print(a * b)
#
# print(a / b)
# # 取整
# print(a // b)
# # 取余
# print(a % b)
# # 指数  幂
# print(a ** b)
#
# print((5 + 1) * 2)

# 扩展
# 字符串的加法 是进行拼接的
# a = '123'
# b = '456'
# print(a + b)

# 在python中 +两端都是字符串才可以进行加法运算
# a = '123'
# b = 456
# # print(a + b)
# print(a + str(b))

# 字符串的乘法 是将字符串重复多少次
# a = '人类的本质就是复读机 '
# print(a * 3)

# -------------------------------- 赋值运算符 --------------------------------
# a = 10
# print(a)
#
#
# b = c = 20
# print(b)
# print(c)
#
# # 多个变量赋值(使用逗号分隔)
d,e,f = 1,2,3
# print(d)
# print(e)
# print(f)

# -------------------------------- 复合运算符 --------------------------------
a = 1
# a加上一个2 打印结果
# a = a + 2
# print(a)

a += 2   # a = a + 2
print(a)

b = 1
# b 乘以一个3 打印结果
# b = b * 3
# print(b)

b *= 3  # b = b * 3
print(b)

c = 2
# c 减去一个1 打印结果
# c = c - 1
# print(c)

c -= 1  # c = c - 1
print(c)


d = 3

# d 除以一个2 打印结果
# d = d / 2
# print(d)

d /= 2 # d = d / 2
print(d)

e = 3

# e 整除一个2 打印结果
# e = e // 2
# print(e)

e //= 2  # e = e // 2
print(e)

# %  取余  取模  模余
f = 3
# f 对5来取余数 打印结果
# f = f % 5
# print(f)

f %= 5 # f = f % 5
print(f)

g = 5

# 求一下5的3次幂
# g = g ** 3
# print(g)

g **= 3   # g = g ** 3
print(g)

# +=  -+  *=  /=  //=  %=  **=

# -------------------------------- 比较运算符 --------------------------------
# 比较运算符返回的都是boolean类型的数据

# == 恒等   判断==两边的变量是否是一致
# a = 10
# b = 10
# print(a == b)

# != 不等  判断！=两边的变量是否不一致
# a = 10
# b = 10
# print(a != b)
# 扩展：<>  python2版本使用 python3 遗弃
# print(10 <> 20)

# > 大于
print(10 > 20)
print(10 > 5)

# >= 大于等于
print(10 >= 10)
print(10 >= 5)
print(10 >= 20)

# < 小于
print(10 < 20)
print(10 < 5)

# <= 小于等于
print(10 <= 10)
print(10 <= 20)


# 比较运算符  ==  !=  > >= < <=

# -------------------------------- 逻辑运算符 --------------------------------
# 逻辑运算符  and 与  or 或  not 非

# and 与
# and两边的数据 必须全部都是true的时候 才会返回true 只要有一端返回的是false 那么就返回false
# and两端都是false的时候 返回的是false
print(10 > 20 and 10 > 11)
# and一端是true 一端是false 返回的是false
print(10 > 5 and 10 >11)
# and一端返回的是false 一端返回的是true  返回的是false
print(10 > 11 and 10 > 5)
# and 两端返回的都是true则返回的是的true
print(10 > 5 and 10 > 6)

# or 或者
# or的两端只要有一端是true 那么结果就是true
# or的两端都是false 则返回的是false
print(10 > 20 or 10 > 21)
# or的两端前面的是true  后面的是false 那么返回的是true
print(10 > 5 or 10 > 20)
# or的两端 前面的是false 后面的是true  那么返回的是true
print(10 > 20 or 10 > 5)
# or的两端都是true  那么返回的是true
print(10 > 5 or 10 > 6)

# not  非  取反
print(not True)
print(not False)
print(not (10 > 20))

print('-------')

var = 10 < 5 and '大于' and 10 > 5
var = 10 < 5 or '' or 'xxx'

print(var)
print('-------')
