
#while和if的联合使用（以密码登陆为例）
# 正确的密码
correct_password = "123"

# 用于计数密码尝试次数
attempt_count = 0

while attempt_count < 3:
    # 用户输入密码
    password = input("请输入密码：")
    
    # 检查密码是否正确
    if password == correct_password:
        print("您已经成功登陆！")
        break
    else:
        print("密码错误！")
        attempt_count += 1  # 增加尝试次数

    # 检查尝试次数是否达到3次
    if attempt_count == 3:
        print("密码输错3次，程序即将退出。")


# 用户名和密码的字典
user_credentials = {
    "dyx": "123",
    "cdb": "321"
}

# 用于计数密码尝试次数
attempt_count = 0

while attempt_count < 3:
    # 用户输入用户名
    username = input("请输入用户名：")
    # 用户输入密码
    password = input("请输入密码：")

    # 检查用户名是否存在且密码是否正确
    if username in user_credentials and user_credentials[username] == password:
        print("您已经成功登陆！")
        break
    else:
        print("用户名或密码错误！")
        attempt_count += 1  # 增加尝试次数
        if attempt_count == 3:
            print("登陆失败次数过多，程序即将退出。")