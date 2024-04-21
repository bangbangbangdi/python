def CBD(name='xxx'): # 'xxx'里为default值，在引用函数时，如果输入了值便会被覆盖。
    print(__name__) # 当该文件作为程序的主入口执行时，会被赋值为__main__。这里的__name__和__main__是既定值。
    print(f'我叫{name}!')

# CBD('陈达邦')
if __name__ == '__main__':
    CBD('ddd')