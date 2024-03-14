

# fp = open('test.txt','w')
# # 默认情况我们只能将字符串写入到文件中
# fp.write('hello world')
#
# fp.close()


# fp = open('test.txt','w')
# # 默认情况下 对象是无法写入到文件中  如果想写入到文件 那么必须使用序列化操作
# name_list = ['zhangsan','lisi']
#
# fp.write(name_list)


# 序列化的2种方式
# dumps()
# （1）创建一个文件
# fp = open('test.txt','w')
#
# # （2）定义一个列表
# name_list = ['zs','ls']
#
# # 导入json模块到该文件中
# import json
# # 序列化
# # 将python对象 变成 json字符串
# # 我们在使用scrapy框架的时候  该框架会返回一个对象 我们要将对象写入到文件中 就要使用json.dumps
# names = json.dumps(name_list)
#
# # 将names写入到文件中
# fp.write(names)
# fp.close()





# dump
# 在将对象转换为字符串的同时，指定一个文件的对象 然后把转换后的字符串写入到这个文件里


# fp = open('text.txt','w')
# #
# # name_list = ['zs','ls']
# #
# # import json
# # # 相当于names = json.dumps(name_list) 和 fp.write(names)
# # json.dump(name_list,fp)
# #
# # fp.close()



# 反序列化
# 将json的字符串变成一个python对象

# fp = open('text.txt','r')
#
# content = fp.read()
#
# # 读取之后 是字符串类型的
# print(content)
# print(type(content))
#
# # loads
# import json
# # 将json字符串变成python对象
# result = json.loads(content)
# # 转换之后
# print(result)
# print(type(result))



# load

fp = open('text.txt','r')

import json

result = json.load(fp)

print(result)
print(type(result))

fp.close()