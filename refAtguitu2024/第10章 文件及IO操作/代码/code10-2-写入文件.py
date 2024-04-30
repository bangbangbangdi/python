# 打开文件
f = open('test2.txt',mode='w',encoding='utf-8')
# 写入文件内容
f.write('你好，我是mia\n')
f.write('你是谁\n')
context = ['你好，我是mia','你是谁']
for i in context:
    f.write(i+'\n')
# 关闭文件
f.close()



f = open('test2.txt',mode='r', encoding='utf-8')  # 相对路径
context = f.read()
print(context)
f.close()