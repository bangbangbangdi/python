# -------------------- 模块和包 --------------------
# 两者的关系:一个包当中可以有多个模块

# -------------------- 引用模块1 --------------------
# import demo_module
#
# # 这种方式每次都要写模块名诶...能更简单一些嘛?
# # 当然可以,看下面的引用模块2
# demo_module.print_msg()
# print(demo_module.name)

# -------------------- 引用模块2 --------------------
from demo_module import print_msg, name

# 如果要引入模块中的所有内容的话,可以这样
# from demo_module import *
#
# print_msg()
# print(name)
# p1 = Person("kino", 17)
# print(p1)


# -------------------- 引用包:前言 --------------------
"""
如果说模块是将函数,全局变量等组合到一起供外界使用的话
那么包就是将多个模块组合到一起供外界使用

诶?话说从一开始,为什么非要把函数,全局变量等分到不同模块中呢?
答:因为方便管理,例如:有的模块专门做文本相关的操作,有的模块专门做数值运算的操作等等
"""
# -------------------- 引用包 --------------------
# 引入my_package包下的kino模块
# from my_package.kino import *
#
# print(name)
# print_kino_msg()

# -------------------- 拓展(一笔带过就好) --------------------
"""
在创建包的时候,会发现包下会多出一个空白的__init__.py文件
这是个什么东西?
答:该文件可以看作是package的初始化文件.
嗯...,所以具体有什么用呢?
答: 1.批量化导入 2.__all__ (具体看下面的栗子)
"""
# ---在探究它的具体作用之前,先搞清楚__init__文件在干嘛?---
# 我们在my_package包下的__init__文件中写了一行print()语句
# import my_package
# 可以发现,在导入my_package包时发现print()语句被执行了,也就是__init__文件会在我们导入对应的包时会被调用
# 这也就不难理解为什么该文件的名叫做__init__了(初始化).

# ---1.批量化导入---
from my_package import *

# 如果没有__init__文件的话,上述的import语句就要像下面这样写多行
# from my_package.kino import *
# from my_package.lain import *

# print_kino_msg()
# print_lain_msg()
# print(name)

# ---2.__all__---
# 虽然上面我们用import * 用的很开心,但是实际的开发中这种写法是不推荐的
# 原因在于,这种全部导入的写法很容易污染当前的命名空间
# 那有没有什么办法可以限制全部导入这种行为呢? __all__就可以

# 在__init__文件中通过__all__对暴露的接口做出了限制

# __all__中没有print_kino_msg因此下面会报错
# print_kino_msg()
# print_lain_msg()
# print(name)

# --3.一点额外的小问题--
# 上述代码在输出name 的时候总是lain,不过我们的kino模块也定义了name全局变量啊;这是为什么?
# 因为在引入相同命名的对象时,后面的内容会覆盖前面的
# 要规避这一点可以在引入时给他们取别名 (在__init__文件中)
print(kino_name)
print(lain_name)

