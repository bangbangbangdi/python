try:
    pwd = input('请输入你的密码：')
    if len(pwd)<8:
        raise Exception('密码的长度不够，请输入一个8位以上的密码')
except Exception as e:
    print(e)
