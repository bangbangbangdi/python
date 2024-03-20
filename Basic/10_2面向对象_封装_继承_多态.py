# -------------------------------- 前言 --------------------------------
# 封装、继承、多态这些都是编程思想,对他们的理解需要在往后的学习、工作中慢慢深化,此处仅仅做一个抛砖引玉的介绍

# -------------------------------- 封装 --------------------------------
# 描述:隐藏实现细节,对外暴露简单的调用接口
# 函数本身就是封装思想的体现
"""打印最大值为max的size个随机数"""
import random


def print_random_list(max, size):
    for _ in range(size):
        print(random.randint(0, max), end=',')


# print_random_list(10, 10)
# 调用者并不需要知道函数内部是怎么实现的,仅仅只需要知道怎么用就够了~ 即:隐藏实现细节,对外暴露简单的调用接口


# -------------------------------- 继承 --------------------------------
"""让我们看看下面的代码有什么问题"""

"""声明一个教师类"""
# class Teacher:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def teach(self, course_name):
#         print(f'{self.name} is teaching {course_name}')


"""声明一个学生类"""
# class Student:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def study(self, course_name):
#         print(f'{self.name} is learning {course_name}')
#
# kirii = Teacher('Kirii',18,'male')
# kuroniko = Student('Kuroniko',13,'female')
#
# kirii.teach('shot')
# kuroniko.study('blowing bubbles')

"""可以发现对于上述两个类来说,初始化部分的代码是重复的
如果想要消除这部分代码,可以声明Person类,让Student和Teacher继承Person;如下"""

"""声明一个Person类"""
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def sleep(self):
#         print(f'{self.name} is sleeping')
#
#     def eat(self):
#         print(f'{self.name} is eating')


"""声明一个Teacher类,并继承自Person类"""
# class Teacher(Person):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age, gender)
#
#     def teach(self, course_name):
#         print(f'{self.name} is teaching {course_name}')


"""声明一个Student类,并继承自Person类"""
# class Student(Person):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age, gender)
#
#     def study(self, course_name):
#         print(f'{self.name} is learning {course_name}')
#
#
# kirii = Teacher('Kirii', 18, 'male')
# kuroniko = Student('Kuroniko', 13, 'female')
#
# kirii.teach('shot')
# kuroniko.study('blowing bubbles')

# PS:实际上我们会发现,很多技术诞生的目的都是为了解决代码复用的问题(我们真的非常非常讨厌重复的东西啦..)

# -------------------------------- 多态 --------------------------------
# 描述:子类通过“重写”父类的方法,从而实现调用相同的方法却做不同的事情
# 看不懂没关系,我们直接来看代码~

"""声明一个Person类"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def sleep(self):
        print(f'{self.name} is sleeping')

    def eat(self):
        print(f'{self.name} is eating')


"""声明一个Teacher类,并继承自Person类"""
class Teacher(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def teach(self, course_name):
        print(f'{self.name} is teaching {course_name}')

    """重写父类的eat方法"""
    def eat(self):
        print(f'{self.name} is eating energy bar')



"""声明一个Student类,并继承自Person类"""
class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def study(self, course_name):
        print(f'{self.name} is learning {course_name}')

    """重写父类的eat方法"""
    def eat(self):
        print(f'{self.name} is eating candy floss')

kirii = Teacher('Kirii', 18, 'male')
kuroniko = Student('Kuroniko', 13, 'female')

"""因为Teacher和Student都各自重写了eat方法,因此表现为“调用相同的方法,但不同的行为” 即多态"""
kirii.eat()
kuroniko.eat()

"""因为sleep方法没有重写,因此用的是Person类中的实现"""
kirii.sleep()
kuroniko.sleep()

