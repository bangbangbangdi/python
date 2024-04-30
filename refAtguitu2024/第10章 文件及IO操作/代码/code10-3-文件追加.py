# 打开文件
f = open('test3.txt',mode='a',encoding='utf-8')
# 写入文件
f.write('hello\n')
a=['a','vb\n','c\n']
f.writelines(a)
# 关闭文件
f.close()