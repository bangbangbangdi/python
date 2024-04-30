class Player(object):
    numbers = 0   # 类属性
    def __init__(self,name,age,city):  # 初始化函数（构造函数）
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1

mia = Player('mia',24,'上海')
print(mia.__dict__)
print('欢迎荣耀王者的第 %d 个玩家注册！' % Player.numbers)
tom = Player('tom',32,'重庆')
print('欢迎荣耀王者的第 %d 个玩家注册！' % Player.numbers)

class weapon(object):
    numbers = 0
    max_damage = 10000
    levels = ['青铜','白银','黄金','钻石','王者']
    def __init__(self,name,damage,level):
        self.name = name
        self.damage = damage
        self.level = level
        weapon.numbers += 1
        if damage>weapon.max_damage:
            raise Exception('最大的伤害值是10000，请重试！')
        if level not in weapon.levels:
            raise Exception('段位设置错误！')
try:
    gun = weapon('magic',10000,'王者')
    print(weapon.numbers)
    arrow = weapon('arrow',450,'青铜')
    print(weapon.numbers)
except Exception as e:
    print(e)