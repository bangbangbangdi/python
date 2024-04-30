cards = [{'name': 'mia', 'phone': '213', 'qq': '3546', 'email': '123'},
{'name': 'jack', 'phone': '124235', 'qq': '23423434', 'email': '3465'},
         {'name': 'tom', 'phone': '234', 'qq': '234', 'email': '09877'}]
def menu():
    print('*'*30)
    print('''欢迎使用【名片管理系统】
    1.新建名片
    2.显示全部
    3.查询名片
    0.退出系统''')
    print('*'*30)
def new_card(name,phone,qq,email):
    user = {
        'name':name,
        'phone':phone,
        'qq':qq,
        'email':email
    }
    cards.append(user)
    return True

def modify_card():
    pass

def del_card():
    pass

def show_card():
    for card in cards:
        print(card)

def query_card(kw):
    for card in cards:
        for k,v in card.items():
            if kw == v:
                return card
    return False

def quit():
    print('欢迎下次使用【名片管理系统】')


def main():
    menu()
    while True:
        op = input('请输入你要操作的序号：')
        if op=='1':
            name = input('请输入你的姓名：')
            phone = input('请输入你的电话：')
            qq = input('请输入你的qq号：')
            email = input('请输入你的电子邮箱：')
            result = new_card(name,phone,qq,email)
            if result:
                print('成功新建名片')
            else:
                print('请重试')
        elif op=='2':
            show_card()
        elif op=='3':
            kw = input('请输入查询的关键字：')
            result = query_card(kw)
            if result:
                print(result)
                op2 = input('输入4修改名片，输入5删除名片：')
                if op2 =='4':
                    modify_card()
                if op2=='5':
                    del_card()

            else:
                print('没有查到相关信息')
        elif op=='0':
            quit()
            break
        else:
            print('请重试')