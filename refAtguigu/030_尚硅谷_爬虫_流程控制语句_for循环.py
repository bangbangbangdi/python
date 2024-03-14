# 循环字符串
# range(5)
# range(1,6)
# range(1,10,3)
# 循环一个列表


# 一个一个的输出 叫做循环 也叫做遍历
# for
# 格式：  for 变量  in 要遍历的数据:
#             方法体


# 循环字符串
# s = 'china'
# i是字符串中一个又一个的字符的变量
# s是代表的是要遍历的数据
# for i in s:
#     print(i)


# range(5)
# range方法的结果 一个可以遍历的对象
# range（5）  0~4  左闭右开区间(0,5)
# for i in range(5):
#     print(i)


# range(1,6)
# range（起始值，结束值）
# 左闭右开区间
# for i in range(1,6):
#     print(i)


# range(1,10,3)
# range（起始值，结束值，步长）
# 1  4  7  10
# 左闭右开区间
# for i in range(1,11,3):
#     print(i)


# 应用场景  会爬取一个列表返回给我们
# 循环一个列表
a_list = ['周杰伦','林俊杰','陶喆','庞龙']

# 遍历列表中的元素
# for i in a_list:
#     print(i)

# 遍历列表中的下标

# 判断列表中的元素的个数
# print(len(a_list))
# 0 1 2
for i in  range(len(a_list)):
    print(i)
