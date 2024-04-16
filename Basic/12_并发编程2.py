# -------------------- 多进程编程 --------------------
# 问题描述:对于官方的python解释器而言,我们无法通过多线程的方式将CPU的使用率突破100%,
#   但是对于现在多核计算机而言CPU使用率100%仅仅意味着将一个CPU跑满,其他CPU都在摸鱼(一人干活,多人围观)
#   为了更加充分的使用CPU的计算能力,我们可以使用多进程
from multiprocessing import current_process, Process
from time import sleep


# -------------------- 创建进程 --------------------
def to_travel(character, locations):
    """
    输出谁去哪里旅行
    :param character: 旅人
    :param locations: 旅行的地点列表
    :return:
    """
    # current_process()能获取当前进程对象
    print(f'PID:{current_process().pid}')
    print(f'Name:{current_process().name}')
    sleep(1)
    while len(locations) != 0:
        print(f'{character} travels to the {locations[0]}')
        locations.pop(0)
        sleep(0.4)


def multi_process():
    """多进程的执行to_travel函数"""
    lis = ['クロニコのながぐつ', '人の痛みがわかる国', '多数決の国', '大人の国', '東亜重工']
    Process(target=to_travel, args=('kaiba', lis)).start()
    Process(target=to_travel, args=('kino', lis)).start()
    to_travel('kiri', lis)


def main():
    multi_process()
    pass


if __name__ == '__main__':
    main()
