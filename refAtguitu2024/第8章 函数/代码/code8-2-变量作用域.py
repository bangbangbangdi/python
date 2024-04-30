# 全局变量
num1 = 10  # 不可变数据类型
list1 = [1,2,3,4,5]   # 可变数据类型

def f():
    global num1  # 声明在f中使用的num1是全局变量num1
    num2 = 20  # 局部变量
    num1 = 20
    list1[2] = 8
    print('在函数f中打印num1的值',num1)
    print('在函数f中打印list1的值',list1)
    print('num2的值',num2)



f()
# print('在函数f外打印变量num2的值',num2) # 局部变量不能在函数外使用
print('在函数f执行后打印num1的值',num1)
print('在函数f执行后打印list1的值',list1)