# 1.位置参数(普通参数)
def param(name, age, gender, height, weight):
    print(name, age, gender, height, weight)


param('Kino', 16, 'female', 160, 110)


# 现在请阿T同学实现这样一个add()函数,需求如下
# 1.接受四个参数
# 2.将这四个参数相加的结果打印出来
# 例如 add(1,2,3,4) -> 打印 10


# 现在需求调整为了如下:
# 1.接受最多四个参数
# 2.将这四个参数相加的结果打印出来
# 例如 add2() -> 打印0 ; add2(1,2) -> 打印 3; add2(1,2,3) -> 打印 6; add2(1,2,3,4) -> 打印 10


# 需求又调整啦:
# 1.接受任意多个参数
# 2.将这四个参数相加的结果打印出来
# 例如 add3(1,2,3,4,5,6,7,8) -> 打印 36

def add3(*args):
    print(type(args))
    print(*args)

    print(args)


add3(1, 2, 3, 4, 5, 6, 7, 8, 9)


# 想想一下有下面这样的函数
def param3(name=None, age=None, gender=None, height=None, weight=None, favorite=None, partner=None):
    print(name, age, gender, height, weight, favorite, partner)


# 现在我只知道该要打印的信息有 名字叫kino 年龄16岁 伙伴是erms;
param3('Kino', 16, partner='erms')


def param(*args):
    print(args)


param(10, 20, 35)


def param2(**kwargs):
    print(type(kwargs))
    print(kwargs['name'])
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs)


param2(name='Kino', age=16)


class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):

    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id

    def show(self):
        print(self.id, self.name, self.age, self.gender)


stu = Student(123, 'Kino', 16, gender='female')


# stu.show()

def param3(*args, **kwargs):
    print(*args)
    print(args)
    # print(**kwargs)
    print(kwargs)


param3(1, 2, 3, 4, a=5, b=6, c=7)
