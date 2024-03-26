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
    # 可以用open函数打开一个文件
    # 常用参数：
    # file = 文件名 ('./Sample.txt')
    # mode = 操作模式 ('r') 常见的操作模式:'r'-read读取  'w'-write写入(会清空原有文件) 'a'-append追加(将内容写到文件末尾)
    # encoding = 字符编码 ('utf-8') 为什么这个在传参的时候要指明参数呢？
    file = open('testFile/Sample.txt', 'r', encoding='utf-8')
    # 打开一个文件后我们就可以从中读取数据啦~
    print(file.read())
    # 在使用完以后记得要close释放资源
    # 如果不释放会怎么样？1.系统资源的浪费 2.某些操作系统下文件打开状态会将文件锁定(其他程序无法访问或者修改该文件)
    # 但是每次都需要close不会很麻烦嘛...能不能在使用完后自动帮我close呢?能! with登场!
    file.close()


def read_file():
    # 以后我们操作文件基本都用with关键字帮我们调用对象的close方法
    with open('testFile/Sample.txt', 'r', encoding='utf-8') as file:
        # 其实file也是一个可遍历的对象,我们可以按行读取其中的数据
        for line in file:
            print(line)


# -------------------- 写入文件 --------------------
def write_file():
    # 通过观察可以发现 w 模式会覆盖我们原有的内容
    # with open('./Sample.txt', 'w', encoding='utf-8') as file:
    #     file.write('通过write方法写入')
    # 如果我们需要追加某些内容,我们可以使用 'a'-追加操作模式
    with open('testFile/Sample.txt', 'a', encoding='utf-8') as file:
        file.write('通过write方法写入')


# -------------------- Practices1 --------------------
# 读取FightClub.txt中的内容,并输出到控制台上


# -------------------- Practices2 --------------------
# 在FightClub.txt后追加任意内容


# -------------------- main --------------------
def main():
    # read_file()
    # write_file()
    # read_file()
    pass


if __name__ == '__main__':
    main()
