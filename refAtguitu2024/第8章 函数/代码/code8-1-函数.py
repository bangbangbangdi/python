def sum_2(a,b): # 形式参数
    return a+b


result = sum_2(9,8)  # 实际参数
# a = len('get')
# print(a)
# print(result)

def power(x, n=2): #  n：默认参数，缺省参数
    return x**n

a = power(4,3)
b = power(5,3)
c = power(6)
print(c)
print(b)
print(a)
a = int('16', 8)
print(a)

def infos(name,age=24,gender='女'):
    return '大家好，我叫%s ，我今年%d岁，我是一名%s生'%(name,age,gender)
s = infos('mia',24,'女')
lily = infos('lily')
jack = infos('jack',gender='男')
print(jack)
print(lily)

# 可变参数

def total(*args): # 可变参数
    print(args)
    result = 0
    for i in args:
        result += i*i
    return result

result = total(1,4,5,6,7,8,3)

print(result)
result = total(3,4,5)
a = [1,2,3,4,5]
result = total(*a)
print(result)


def f(**kwargs): # 可变参数，接收字典
    for k,v in kwargs.items():
        print(k,v)

d = {'name':'xiaoming','age':18}
f(**d)

