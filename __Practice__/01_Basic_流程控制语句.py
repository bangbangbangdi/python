# -------------------------------- if --------------------------------
# if判断语句结构
# if 判断条件:
#         代码（如果判断条件为true的时候执行if下面的内容）

if 1 < 2 :
    print('正确')

# false则不输出内容
if 1 > 2 :
    print('正确')

kino = True
if kino:
    print('她的摩托车叫艾尔梅斯')
l
# if-else的语法
# if 判断条件:
#       判断条件为true的时候执行的代码
# else:
#       判断条件为false的时候执行的代码

# password = input('Enter your PW')
# if password == '2024':
#     print('Login Success!')
# else:
#     print('You are not allow to access')

# -------------------------------- for --------------------------------
# for循环：遍历，挨个输出。
# for 变量  in 要遍历的数据:
#   方法体

# 字符串循环
s = 'tokyo'
for i in s: # “i”可以是任意英文与“_”。数字和特殊字符会报错。
    print(i)

# -------------------------------- range --------------------------------
# range：一个遍历的方法。生成对象供for遍历
range(6)
for i in range(6):
    print(i)