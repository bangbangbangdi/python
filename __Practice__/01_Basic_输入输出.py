# -------------------------------- 输出 --------------------------------
# 输出
print('学车倒计时')
print(2)
print(1.2)
print(1 > 2)
print(2 > 1)

# 格式化输出(带入变量？)
mbti = 'enfp'
name = 'Tin'
num = 10086

# %s 代表的是字符串，%d 代表的是整数数值
# *中间需要%来承上启下，后面括号里跟着各自想带入的变量
default = '我是%s,我的mbti是%s,我的电话号码是%d。' % (name,mbti,num)
print(default)


mbti_bbb = 'intj'
name_bbb = 'Bang'
fs = 27.5
# %f float型，默认取小数点后6位。
Bang = '俺是%s，我的mbti是%s，我穿%fcm的鞋子。' % (name_bbb,mbti_bbb,fs)
print(Bang)

# %f float型，控制小数点后的数字量可用%.1f。这里的“1”代表只取后一位。
Bang = '俺是%s，我的mbti是%s，我穿%.1fcm的鞋子。' % (name_bbb,mbti_bbb,fs)
print(Bang)

# -------------------------------- 输入 --------------------------------
'''
name = input('哈喽，你是谁？')
mbti = input('你是什么mbti？')
age = input('你多大了？')
size = input('你穿多大的鞋子？')

print('我的名字是%s,我是%s,我%d岁了,我穿%.1fcm的鞋子。') % (name,mbti,age,size) # 错误
print('我的名字是%s,我是%s,我%d岁了,我穿%.1fcm的鞋子。' % name,mbti,age,size) # 错误
print('我的名字是%s,' % name, 我是%s, % mbti, 我%d岁了,我穿%.1fcm的鞋子。' % name,mbti,age,size) # 错误

*失败,input 函数默认返回字符串类型，但在格式化字符串时，有 age 使用 %d （整数格式化）和 size 使用 %.1f （浮点数格式化）。这需要将这些输入转换为相应的数据类型。

print('我的名字是%s,我是%s,我%s岁了,我穿%scm的鞋子。') % (name,mbti,age,size) # 错误
print('我的名字是%s,我是%s,我%s岁了,我穿%scm的鞋子。' % (name,mbti,age,size))  #错误
'''
name = input('哈喽，你是谁？')
mbti = input('你是什么mbti？')
age = int(input('你多大了？'))
size = float(input('你穿多大的鞋子？'))

# print('我的名字是%s,我是%s,我%d岁了,我穿%.1fcm的鞋子。') % (name,mbti,age,size) # 错误，print 语句中的格式化操作符 % 现在被包含在 print 函数的括号内，这样整个格式化字符串和其对应的变量都作为 print 的参数处理。
print('我的名字是%s,我是%s,我%d岁了,我穿%.1fcm的鞋子。' % (name,mbti,age,size))

name = input('哈喽，你是谁？')
mbti = input('你是什么mbti？')
age = str(input('你多大了？'))  # 这里的str()可以省掉,原因就像上面说的那样,input()函数返回的本身就是字符串
size = str(input('你穿多大的鞋子？'))  # 同上~

# 暴力而简便的方法：把所有类型都先强制转换为str
print('我的名字是%s,我是%s,我%s岁了,我穿%scm的鞋子。' % (name,mbti,age,size))

'''
总结：
1.用“input”输入时，需要先确定数据类型。(也可以全部转换为str后用%s代入)
2.格式化操作符“%”需要包含在print括号内部。
'''