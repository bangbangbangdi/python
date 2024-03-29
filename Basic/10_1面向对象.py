# -------------------------------- 定义类 --------------------------------
# 关键字：class
# class Student:
#
#     def study(self, course_name):
#         print(f'学生正在学习{course_name}.')
#
#     def play(self):
#         print(f'学生正在玩游戏.')


# -------------------------------- 通过类创建对象 --------------------------------
# stu1 = Student()
# stu2 = Student()
# print(stu1)
# print(stu2)
# # 上面输出的内容就是对象在内存中的地址
# print(id(stu1), id(stu2))
# print(hex(id(stu1)), hex(id(stu2)))

# -------------------------------- 调用对象中的方法 --------------------------------
# # 通过对象调用
# stu1.study('开摩托车')
# # 通过类调用
# Student.study(stu1, '使用枪械')

# -------------------------------- 初始化方法 --------------------------------
# 刚刚定义的Student类只有行为(方法),没有属性要添加属性我们可以添加一个名为__init__的方法
# __init__方法会在创建对象时自动执行，因此也通常被称作初始化方法
class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')
#
#
# # 由于初始化方法除了self之外还有两个参数
# # 所以调用Student类的构造器创建对象时要传入这两个参数
stu1 = Student('kino', 16)
stu2 = Student('erms', 0)
stu1.study('Python程序设计')
stu2.play()

# -------------------------------- 打印对象 --------------------------------
# 上面我们通过__init__方法在创建对象时为对象绑定了属性并赋予了初始值。
# 在Python中，以两个下划线__（读作“dunder”）开头和结尾的方法通常都是有特殊用途和意义的方法，我们一般称之为魔术方法或魔法方法。
# 如果我们在打印对象的时候不希望看到对象的地址而是看到我们自定义的信息
# 可以通过在类中放置__repr__魔术方法来做到，该方法返回的字符串就是用print函数打印对象的时候会显示的内容
# class Student:
#     """学生"""
#
#     def __init__(self, name, age):
#         """初始化方法"""
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         """学习"""
#         print(f'{self.name}正在学习{course_name}.')
#
#     def play(self):
#         """玩耍"""
#         print(f'{self.name}正在玩游戏.')
#
#     def __repr__(self):
#         return f'{self.name}: {self.age}'
#
#
# students = [Student('kino', 16), Student('erms', 0)]
# print(students)

# 可以预想到的是python中还有许多的魔术方法等着我们去了解，不过这里就暂时不做深入啦...留给以后在说~
