# # 封装
# class User(object):
#     def __init__(self,name,age):
#         self._name = name   # 受保护的变量
#         self.__age = age  # 私有变量
#
#     '''把函数当做变量去使用：
#     @property
#     def 变量名() #获取变量
#     @age.setter
#     def 变量名() #修改变量
#     '''
#
#     @property  # 获取变量
#     def age(self):
#         return self.__age
#
#     @age.setter   # 变量的修改器
#     def age(self,age):
#         if isinstance(age,int):
#             self.__age = age
#         else:
#             raise Exception('年龄只能是整数')
#
#     def show_infos(self):
#         print('大家好，我是%s,我今年%d' %(self._name,self.__age))
#
#
# mia = User('mia',24)
# # print(mia.get_age())
# # mia.set_age('二十五')
# # print(mia.get_age())
# '''
# print(mia.age)
# mia.age=25
# print(mia.age)
# '''
# print(mia.age)
# mia.age = '二十五'
# print(mia.age)



class Player(object): # 父类
    numbers = 0   # 类属性
    levels = ['青铜', '白银', '黄金', '钻石', '王者']
    def __init__(self,name,age,city,level):  # 初始化函数（构造函数）
        self._name = name  # 实例属性
        self._age = age
        self._city = city
        if level not in Player.levels:
            raise Exception('段位设置错误！')
        else:
            self.level = level
        Player.numbers += 1

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self,city):
        if len(city)>10 or len(city)<2:
            raise Exception('城市名称有误，请检查！')
        self._city = city


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if not isinstance(age,int):
            raise Exception('年龄必须是整数')
        if age<0 or age>100:
            raise Exception('年龄必须在0到100之间')
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if name == self.name:
            raise Exception('修改的名字与现在的名字相同，请重新修改')
        else:
            self._name = name


    def show(self):  # 实例的方法
        print('我是荣耀王者的第%d个玩家，我的名字是%s，我来自 %s，我的段位是%s' % (Player.numbers,self.name,self.city,self.level))

    def level_up(self):
        index1 = Player.levels.index(self.level)
        if index1<len(Player.levels)-1:
            self.level = Player.levels[index1+1]

    def get_weapon(self,weapon):
        self.weapon = weapon

    def show_weapon(self):
        return self.weapon.show_weapon()

    @classmethod
    def get_players(cls):  # 类方法
        print('荣耀王者的用户数量已经达到了%d人'%cls.numbers)

    @staticmethod
    def isvalid(**kwargs):
        if kwargs['age']>18:
            return True
        else:
            return False

mia = Player('mia',26,'山东','王者')
mia.name = 'tom'
print(mia.name)
mia.age = 22
print(mia.age)
mia.city = '苏州'
print(mia.city)
print(mia.__dict__)
