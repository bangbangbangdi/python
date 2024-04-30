class User(object):
    def __init__(self,name):  # 构造函数
        print('__init__被调用')
        self.name = name

    def __str__(self):
        return '我的名字是%s'%self.name

    def __add__(self, other):
        return self.name + other.name

    def __eq__(self, other):
        return self.name == other.name


mia = User('mia')
print(str(mia))
print(mia)
print(1+3)
print('hi '+'mia')
jack = User('mia')
print(mia+jack)
print(6==7)
print(mia==jack)
