

# 创建一个test.txt文件
# open(文件的路径,模式)
# 模式:  w 可写
#       r 可读
# open('test.txt','w')


# 打开文件
# fp = open('test.txt','w')
# fp.write('hello world')

# 文件夹是不可以创建的  暂时需要手动创建
# fp = open('demo/text.txt','w')
# fp.write('hello shangguigu')

# 文件的关闭
fp = open('a.txt','w')
fp.write('hello')
fp.close()