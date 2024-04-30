x = 'heidsio'
match x:
    case 'hello':
        print('正确')
    case 'helo':
        print('少写了一个l')
    case 'heiio':
        print('字母l拼错了')
    case _:
        print('拼写不正确，请仔细检查')
