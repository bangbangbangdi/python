# -------------------- 绝对路径 --------------------
# 描述:从根盘符开始,到目标文件的完整路径
# 例如: /Users/chendabang/PycharmProjects/python/Sample.txt
# 现实中的栗子:阿丁在哪里? 日本/东京都/xx区/xx丁目/xx咖啡厅/xx桌
import os
import time


# -------------------- 相对路径 --------------------
# 描述:是从当前文件开始,到目标文件的路径
# 例如: ./Sample.txt (./表示当前文件夹)
# 现实中的栗子:阿丁在哪里? 在我旁边


# -------------------- 读取文件 --------------------
def read_file1():
    file = open('./Sample.txt', 'r', encoding='utf-8')
    print(file.read())
    file.close()


def read_file():
    with open('./Sample.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)


# -------------------- 写入文件 --------------------
def write_file():
    # 通过观察可以发现 w 模式会覆盖我们原有的内容
    with open('./Sample.txt', 'w', encoding='utf-8') as file:
        file.write('通过write方法写入')
    # 如果我们需要追加某些内容,我们
    with open('./Sample.txt', 'w', encoding='utf-8') as file:
        file.write('通过write方法写入')

# -------------------- main --------------------
def main():
    read_file()
    write_file()
    read_file()


if __name__ == '__main__':
    main()
