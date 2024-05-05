# -------------------- 模块 --------------------
# 类比:模块就好比是工具包,想要使用这个工具包中的工具,就需要导入import这个模块
# 描述:每一个以扩展名py结尾的python源代码文件都是一个模块
# 作用:在模块中定义的全局变量、函数等都是模块能够提供给外界直接使用的工具
# PS:实际上我们之前写的所有.py文件,都是一个模块
# 全局变量
name = 'Tyler'


# 函数
def print_msg():
    print("I shouldn't just abandon money and property and knowledge.")


# 类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.age}'
