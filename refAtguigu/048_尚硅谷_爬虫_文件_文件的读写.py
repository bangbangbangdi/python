

# 写数据
# write方法

# fp = open('test.txt','a')
#
# fp.write('hello world,i am here\n' * 5)
#
# fp.close()

# 如果我再次来运行这段代码  会打印10次还是打印5呢？
# 如果文件存在 会先情况原来的数据 然后再写
# 我想在每一次执行之后都要追加数据
# 如果模式变为了a 那么就会执行追加的操作


# 读数据
fp = open('test.txt','r')
# 默认情况下 read是一字节一字节的读 效率比较低
# content = fp.read()
# print(content)

# readline是一行一行的读取  但是只能读取一行
# content = fp.readline()
# print(content)


# readlines可以按照行来读取  但是会将所有的数据都读取到 并且以一个列表的形式返回
# 而列表的元素 是一行一行的数据
content = fp.readlines()
print(content)