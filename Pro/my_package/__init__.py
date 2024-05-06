# -------------------- __init__文件的作用--------------------
# __init__文件在干嘛?
# print("Hello~这里是__init__文件")

# ---1.批量化导入---
# 在__init__文件中导入需要的模块

# ---2.__all__---
# 通过__all__可以控制,对外暴露的接口(即函数、全局变量等),这里我们只对外暴露了print_lain_msg和name两个内容
# __all__ = ['print_lain_msg', 'name']

# from Pro.my_package.kino import *
# from Pro.my_package.lain import *

# ---3.一点点小问题---
# 可以给引入的重名变量起别名规避同名覆盖
from Pro.my_package.kino import print_kino_msg, name as kino_name
from Pro.my_package.lain import print_lain_msg, name as lain_name
