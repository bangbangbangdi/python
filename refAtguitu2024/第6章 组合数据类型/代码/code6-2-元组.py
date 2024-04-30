# 元组的创建
tuple1 = (1, 2, 3, True, 'hello')
print(tuple1)
print(type(tuple1))
list1 = [1]
print(list1)
tuple2 = (1, )   # 元组里只有一个元素时，加一个逗号
print(tuple2)
print(type(tuple2))
tuple3 = tuple()  # tuple():类型转换
print(tuple3)
print(type(tuple3))
tuple4 = ()
print(tuple4)
print(type(tuple4))

# 类型转换
tuple5 = tuple('hello') # str-->tuple
print(tuple5)
tuple6 = tuple([1,2,3,4]) # list-->tuple
print(tuple6)
list1 = list(tuple6)  # tuple-->list
print(list1)
str1 = str(tuple6)  # tuple-->str
print(str1)
print(type(str1))
print(str1[2])

# 序列的通用操作
print('-'*30)
# 索引
print(tuple1[-1])
# 切片
print(tuple1[::-1])
# len
print(len(tuple1))
print(max(tuple6),min(tuple6))
# del
del tuple5
# print(tuple5)
# +
print(tuple1+tuple6)
# *
print(tuple1*3)
# in
print(1 in tuple1)


# 元组的常用方法
a = tuple1.count('hellwwwo')
print(a)
print(tuple1)
a = tuple1.index(2)
print(a)

# 元组的遍历
print('-'*30)
for i in tuple1:
    print(i)

for index,value in enumerate(tuple1):
    print(index,value)

for i in range(len(tuple1)):
    print(i,tuple1[i])