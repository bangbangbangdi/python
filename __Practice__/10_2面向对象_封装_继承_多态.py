import random


def print_random_list(max, size):
    for i in range(size):
        print(random.randint(0, max), end=',')


# 教师类声明


class Teacher:
    def __init__(self, name, age, gender, subject):
        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject

    def eat(self):
        print(f'{self.name} eating cake')

    def teach(self, course_name):
        print(f'{self.name} is teaching {course_name}')


# 声明一个学生类


class Student:
    def __init__(self, name, age, gender, homework):
        self.name = name
        self.age = age
        self.gender = gender
        self.homework = homework

    def eat(self):
        print(f'{self.name} eating gum')

    def study(self, course_name):
        print(f'{self.name} is learning {course_name}')


Bang = Teacher('Abang', 27, 'male', 'coding')
Tin = Student('Tin', 6, 'femal', 'coding')

Tin.eat()
Tin.study('python')
Bang.eat()
Bang.teach('python')

# 继承重复的部分以使你的代码更加简洁

print('================')


# 声明一个共通的“Person”类

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def sleep(self):
        print(f'{self.name} is sleeping')
        print(f'{self.gender} is sleeping for {self.age} years')

    def eat(self):
        print(f'{self.name} is eating,{self.gender} is eating Pizza')


# 声明一个Teacher类，并让它继承Person类


class Teacher(Person):
    def __init__(self, name, age, gender, school):
        super().__init__(name, age, gender)
        # super().__init__('Tin', '28', 'femal') '''也可以固定下来，这样不会受外部调用的影响'''
        self.school = school

    def teach(self, course_name):
        print(f'{self.name} is at {self.school} teaching {course_name}')

    def metting(self, student_name):
        print(f"{self.name} is having a meeting with {student_name}'s parent")


class Student(Person):
    def __init__(self, name, age, gender, homework):
        super().__init__(name, age, gender, )
        self.homework = homework

    def self_studying(self, test):
        print(f'{self.name} is learning for {test}')


Bang = Teacher('Abang', 27, 'he', 'ToDai')
Tin = Student('Tin', 13, 'she', 'coding')

Bang.eat()
Bang.teach('coding')
Bang.metting('Tin')
Tin.self_studying('python')

# -------------------------多态--------------------------
# 子类通过“重写”父类的方法，从而实现调用相同的方法却做不同的事情

'''声明一个Person类'''


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def sleep(self):
        print(f'{self.name} is sleeping')

    def eat(self):
        print(f'{self.name} is eating,{self.gender} is eating Pizza')


print('声明一个Student类,并继承自Preson类')


class Teacher(Person):
    def __init__(self, name, age, gender, ):
        super().__init__(name, age, gender)

    def teach(self, course_name):
        print(f'{self.name} is teaching {course_name}')

    '''重写父类eat方法'''

    def eat(self):
        print(f'{self.name} is full,so {self.gender} is not eating now.')


class Student(Person):
    def __init__(self, name, age, gender, homework):
        super().__init__(name, age, gender)
        self.homework = homework

    def coding(self):
        print(f'{self.name} is {self.homework}')

    def sleep(self):
        print(f'{self.name} is awake')


Abang = Teacher('Abang', 27, 'he')
Tin = Student('Tin', 6, 'she', 'coding Python')

'''尽管在Student的类里没有声明eat这个方法，但因为继承的父类里面有，所以即使不声明也可以执行'''
Tin.eat()
'''在父类里没有的coding方法，通过在子类里追加定义而实现执行（且引用了父类里没有homework）'''
Tin.coding()
'''通过覆盖的方式重新定义了从父类继承过来的sleep方法'''
Tin.sleep()

Abang.sleep()
Abang.eat()
'''此处{course_name}没有在任何地方被定义，所以需要手动记入'''
Abang.teach('Java')
