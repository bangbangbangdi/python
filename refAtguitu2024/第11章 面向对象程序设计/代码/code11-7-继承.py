# 面向对象特点：继承、多态、封装
class Player(object): # 父类
    numbers = 0   # 类属性
    levels = ['青铜', '白银', '黄金', '钻石', '王者']
    def __init__(self,name,age,city,level):  # 初始化函数（构造函数）
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        if level not in Player.levels:
            raise Exception('段位设置错误！')
        else:
            self.level = level
        Player.numbers += 1

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

class VIP(Player): # 子类

    # 构造函数重写
    def __init__(self,name,age,city,level,coin):
        # 调用父类的构造函数
        super().__init__(name,age,city,level)
        self.coin = coin

    # 实例方法重写
    def show(self):  # 实例的方法
        print('我是荣耀王者的第%d个玩家，我的名字是%s，我来自 %s，我的段位是%s，我的余额是%d' % (Player.numbers,self.name,self.city,self.level,self.coin))




mia = VIP('mia',24,'哈尔滨','黄金',100)
mia.show()
