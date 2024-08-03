# -------------------------------- 函数 --------------------------------
# 下面代码又什么问题捏?
import time
from random import randint


# schedules = ['睡个懒觉', '吃顿好的', '看书', '练字', '学习']
# print("早上要干什么呢?")
# rand = randint(0, len(schedules) - 1)
# for _ in range(3):
#     print('让我想想...')
#     time.sleep(1)
# schedule = schedules[rand]
# print('早上要%s' % schedule)
#
# print("下午要干什么呢?")
# rand = randint(0, len(schedules) - 1)
# for _ in range(3):
#     print('让我想想...')
#     time.sleep(1)
# schedule = schedules[rand]
# print('下午要%s' % schedule)
#
# print("晚上要干什么呢?")
# rand = randint(0, len(schedules) - 1)
# for _ in range(3):
#     print('让我想想...')
#     time.sleep(1)
# schedule = schedules[rand]
# print('晚上要%s' % schedule)


# --------------------------- 函数的定义和调用 -------------------------------------
# 不难发现其中for循环的部分总是重复的
# 这种情况下我们就可以将这部分代码封装到函数中,解决代码重复的问题
# def consider():
#     for _ in range(3):
#         print('让我想想...')
#         time.sleep(1)
#
#
# schedules = ['睡个懒觉', '吃顿好的', '看书', '练字', '学习']
# print("早上要干什么呢?")
# rand = randint(0, len(schedules) - 1)
# consider()
# schedule = schedules[rand]
# print('早上要%s' % schedule)
#
# print("下午要干什么呢?")
# rand = randint(0, len(schedules) - 1)
# consider()
# schedule = schedules[rand]
# print('下午要%s' % schedule)
#
# print("晚上要干什么呢?")
# rand = randint(0, len(schedules) - 1)
# consider()
# schedule = schedules[rand]
# print('晚上要%s' % schedule)

# ----------------------------- 函数返回值 -----------------------------------
# 虽然上面的代码可以吧for部分的重复解决了
# 不过获取日程的部分还是会重复的,能不能直接告诉我日程是什么呢?
# def consider():
#     schedules = ['睡个懒觉', '吃顿好的', '看书', '练字', '学习']
#     rand = randint(0, len(schedules) - 1)
#     for _ in range(3):
#         print('让我想想...')
#         time.sleep(1)
#     program = schedules[rand]
#     return program
#
#
# print("早上要干什么呢?")
# schedule = consider()
# print('早上要%s' % schedule)
#
# print("下午要干什么呢?")
# schedule = consider()
# print('下午要%s' % schedule)
#
# print("晚上要干什么呢?")
# schedule = consider()
# print('晚上要%s' % schedule)

# ----------------------------- 函数参数 -----------------------------------
# 有些时候我早上、下午、晚上的活动不一样啦...,能不能根据我的需求改变schedules的内容呢?
# def consider(schedules):
#     rand = randint(0, len(schedules) - 1)
#     for _ in range(3):
#         print('让我想想...')
#         time.sleep(1)
#     program = schedules[rand]
#     return program
#
#
# morn_sche = ['睡个懒觉', '练字', '学习']
# print("早上要干什么呢?")
# schedule = consider(morn_sche)
# print('早上要%s' % schedule)
#
# after_sche = ['看书', '健身', '学习']
# print("下午要干什么呢?")
# schedule = consider(after_sche )
# print('下午要%s' % schedule)
#
# night_sche = ['吃顿好的', '看电影', '看漫画']
# print("晚上要干什么呢?")
# schedule = consider(night_sche)
# print('晚上要%s' % schedule)

# ----------------------------- 函数内调用函数 -----------------------------------
# 嗯....那几个print()也好碍眼啊...,能不能吧那部分代码也封住也封装一下呢?
# def consider(schedules):
#     rand = randint(0, len(schedules) - 1)
#     for _ in range(3):
#         print('让我想想...')
#         time.sleep(1)
#     program = schedules[rand]
#     return program
#
#
# def decide_sche(times, morn_sche, after_sche, night_sche):
#     all_events = [morn_sche, after_sche, night_sche]
#     for i in range(len(times)):
#         print("%s要干什么呢?" % times[i])
#         # 这里我们调用了另一个我们自定义的函数
#         schedule = consider(all_events[i])
#         print("%s要%s" % (times[i], schedule))
#
#
# periods = ['早上', '下午', '晚上']
# morn_event = ['睡个懒觉', '练字', '学习']
# after_event = ['看书', '健身', '学习']
# night_event = ['吃顿好的', '看电影', '看漫画']
#
#
# decide_sche(periods, morn_event, after_event, night_event)


# 嗯...其实上面这个写的也不够好啦...,肯定还有更好的解决方案;不过那就交给以后的我们吧~

# ----------------------------- 局部变量 -----------------------------------
# 描述:在函数内部定义的变量,其作用范围尽在函数内部
# def test():
#     local_var = '我是局部变量哒'
#     print('我在函数内因此能访问到', local_var)
#
#     print('xxx')
#     return local_var
#
#
# print('在函数外还能访问到嘛?', test())

# ----------------------------- 全局变量 -----------------------------------
# global_var = '我是全局变量哒'


# def test2():
# global global_var
# global_var = 'change'
#     print('我能访问到全局变量嘛?', global_var)
#
#
# test2()
# print('在函数外还能访问到嘛?', global_var)


# ----------------------------- 20240803 -----------------------------------
# ----------------------------- 函数参数 -----------------------------------

# 1.位置参数(普通参数)
def param(name, age, gender, height, weight):
    print(name, age, gender, height, weight)


param('Kino', 16, 'female', 160, 110)


# 2.*args参数
# - *args:允许函数接受任意数量的位置参数
# - 这些参数会存储在一个元祖中.(简单回忆一下元祖)
# - 在函数内部,可以像处理元组一样处理*args
# - 如果不确定调用者会传递多少个位置参数,可以使用*args
def param2(*args):
    print(args)
    # print(type(args))


param2('Kino', 16, 'female', 160, 110)


# 3.**kwargs参数
# - **kwargs:允许函数接受任意数量的关键字参数,并将这些参数存储在一个字典中.(简单回忆一下字典)
#  - 在函数内部,可以像处理字典一样处理**kwargs
#  - 如果不确定调用者会传递多少个位置参数,可以使用**kwargs
def param3(**kwargs):
    print(kwargs)
    print(kwargs['name'])


param3(name='Kino', age=20, gender='male')


# 一起使用时的顺序
#  1. 位置参数
#  2. *args
#  3. **kwargs
def param4(name, age, *args, **kwargs):
    print(name, age)
    print(args)
    print(kwargs)


# 一个栗子
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id


s = Student(123, 'kino', 10, gender='female')
print(s.name, s.age, s.gender)
