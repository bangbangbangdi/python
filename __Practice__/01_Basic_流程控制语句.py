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

# ------------------------------- if-else --------------------------------

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

# #while和if的联合使用（以密码登陆为例）
# # 正确的密码
# correct_password = "123"

# # 用于计数密码尝试次数
# attempt_count = 0

# while attempt_count < 3:
#     # 用户输入密码
#     password = input("请输入密码：")
    
#     # 检查密码是否正确
#     if password == correct_password:
#         print("您已经成功登陆！")
#         break
#     else:
#         print("密码错误！")
#         attempt_count += 1  # 增加尝试次数

#     # 检查尝试次数是否达到3次
#     if attempt_count == 3:
#         print("密码输错3次，程序即将退出。")


# # 用户名和密码的字典
# user_credentials = {
#     "dyx": "123",
#     "cdb": "321"
# }

# # 用于计数密码尝试次数
# attempt_count = 0

# while attempt_count < 3:
#     # 用户输入用户名
#     username = input("请输入用户名：")
#     # 用户输入密码
#     password = input("请输入密码：")

#     # 检查用户名是否存在且密码是否正确
#     if username in user_credentials and user_credentials[username] == password:
#         print("您已经成功登陆！")
#         break
#     else:
#         print("用户名或密码错误！")
#         attempt_count += 1  # 增加尝试次数
#         if attempt_count == 3:
#             print("登陆失败次数过多，程序即将退出。")

# -------------------------------- if-elif --------------------------------


# -------------------------------- for --------------------------------
# for循环：遍历，挨个输出。
# for 变量  in 要遍历的数据:
#   方法体

# 字符串循环
s = 'tokyo'
for i in s: # “i”可以是任意英文与“_”。数字和特殊字符会报错。
    print(i)

# # -------------------------------- range --------------------------------
# range：一个遍历的方法。生成对象供for遍历
range(6)
for i in range(6):
    print(i)

print('================')

# range(起始值, 结束值, 步长)
# 左闭右开区间，如（1, 10, 3)指1～9，没隔3个数取值，取的值为1，4，7
a = range(2, 15, 3)
for i in a:
    print(i)

# range应用：爬取列表
# 循环列表
teacher_name = ['mitsui', 'iwanami', 'iida', 'takegawa']
for i in teacher_name:
    print(i)

# -------------------------------- practice1 --------------------------------
# 在控制台上输入您的成绩分数
# 如果你考了90以上  成绩为优秀
# 如果你考了80以上  成绩为良好
# 如果你考了70以上  成绩为中等
# 如果你考了60以上  成绩为合格
# 如果你考了0以上   成绩为不合格
# 否则            你在逗我..


# score = int(input('Please enter your score:')) # 注意这里一定要将输入的str转换为int，不然会报错！
# # 需要限制分数小于的区间，不然天文数字也会显示为优秀
# if score >= 90 and score <= 100:
#     print('Perfect!')
# elif score >= 80 and score < 90:
#     print('Great!')
# elif score >= 70 and score < 80:
#     print('Great.')
# elif score >= 60 and score < 70:
#     print('OK.')
# elif score >= 0 and score < 60:
#     print('No OK.')
# else:
#     print('Are you kidding me?')

# -------------------------------- practice2 --------------------------------
# 寻找水仙花数。
# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身
# 例如： 153=1^3+5^3+3^3 。
a = range(100, 10000)
for i in a:
    if i == (i // 100)**3 + (i // 10 % 10)**3 + (i % 10)**3 :
        print(i)
# 具体
# for i in a:
#     a1 = i // 100
#     b1 = i // 10 % 10
#     c1 = i % 10
#     if i == a1**3 + b1**3 + c1**3 :
#         print(a1**3, b1**3, c1**3)
#         print(i)


# -------------------------------- practice3 --------------------------------
# 百钱百鸡问题
# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？


# -------------------------------- practice4 --------------------------------
# 斐波那契数列。
# 斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和
# 按照这个规律，斐波那契数列的前10个数是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# 输出斐波那契数列前20个数


# -------------------------------- practice5 --------------------------------
# 打印100以内的素数。
# 素数指的是只能被1和自身整除的正整数（不包括1）。