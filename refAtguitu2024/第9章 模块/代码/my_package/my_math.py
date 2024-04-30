author = 'mia'

def add(a,b):
    return a+b

def total(*args):
    '''
    参数args:接收一个列表
    return：a列表中每个元素的平方和
    '''
    result = 0
    for i in args:
        result = result + i**2
    return result

