def write_txt():
    date = input('请输入今天的日期：')
    text = input('请输入日记内容：')
    filename = '日记本.txt'
    with open(filename,mode='a',encoding='utf-8') as f:
        f.write( 'pyrjb\n')
        f.write(date+'\n')
        f.write(text+'\n')
    return True
def read_txt(day='-1'):
    filename = '日记本.txt'
    with open(filename,mode='r',encoding='utf-8') as f:
        context = f.read()

    if day!='-1':
        lista = context.split('pyrjb\n')
        for i in lista:
            if i[:10] == day:
                print(i)
                return True
        return False
    else:
        context = context.replace('pyrjb\n','')
        print(context)

    return True
def menu():
    print('*'*30)
    print('''欢迎使用python日记本系统
    1：记日记
    2：阅读日记
    3：退出系统''')
    print('*'*30)

def quit():
    print('欢迎下次使用！再见！')

def main():
    menu()
    while True:
        op = input('请输入你的选择：')
        if op == '1':
            if write_txt():
                print('日记保存成功！')
        elif op == '2':
            day = input('请输入你查询的日期(查询全部请输入-1):')
            if read_txt(day):
                print('日记已加载完毕！')
            else:
                print('未查询到日记信息，请重试！')
        elif op == '3':
            quit()
            break
        else:
            print('请重新选择')