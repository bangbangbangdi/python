# 1.位置参数(普通参数)
def param(name, age, gender, height, weight):
    print(name, age, gender, height, weight)


param('Kino', 16, 'female', 160, 110)


# 现在请阿T同学实现这样一个add()函数,需求如下
# 1.接受四个参数
# 2.将这四个参数相加的结果打印出来
# 例如 add(1,2,3,4) -> 打印 10


# 现在需求调整为了如下:
# 1.接受最多四个参数
# 2.将这四个参数相加的结果打印出来
# 例如 add2() -> 打印0 ; add2(1,2) -> 打印 3; add2(1,2,3) -> 打印 6; add2(1,2,3,4) -> 打印 10


# 需求又调整啦:
# 1.接受任意多个参数
# 2.将这四个参数相加的结果打印出来
# 例如 add3(1,2,3,4,5,6,7,8) -> 打印 36


# 想想一下有下面这样的函数
def param3(name=None, age=None, gender=None, height=None, weight=None, favorite=None, partner=None):
    print(name, age, gender, height, weight, favorite, partner)


# 现在我只知道该要打印的信息有 名字叫kino 年龄16岁 伙伴是erms;
