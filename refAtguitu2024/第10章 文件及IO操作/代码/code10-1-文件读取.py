import os
# 打开文件
# f = open('test.txt')  # 相对路径
path = os.getcwd()
filename = path + '/test.txt'
f = open(filename, mode='r', encoding='utf-8')  # 绝对路径
# # 读取文件
# context = f.read(5)
# print(context)
# context = f.readline()
# print(context)
context = f.readlines()
print(context)
# # 关闭文件
f.close()