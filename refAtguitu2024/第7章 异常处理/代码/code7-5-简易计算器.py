while True:
    try:
        op = input('请输入一个四则运算算式（例如1+2）：')
        if '+' in op:#加法 14+256
            a = op.split('+')
            result = int(a[0]) + int(a[1])
            print(result)
        elif '-' in op:
            a = op.split('-')
            result = int(a[0]) - int(a[1])
            print(result)
        elif '*' in op:
            a = op.split('*')
            result = int(a[0]) * int(a[1])
            print(result)
        elif '/' in op:
            a = op.split('/')
            result = int(a[0]) / int(a[1])
            print(result)
        elif op=='C':
            print('感谢您使用本计算器！')
            break
        else:
            raise Exception('请按1+2这个格式输入算式！')
    except ZeroDivisionError:
        print('注意除法运算，除数不能为0！')
    except Exception as e:
        print(e)