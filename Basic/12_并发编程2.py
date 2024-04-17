# -------------------- 多进程编程 --------------------
# 问题描述:对于官方的python解释器而言,我们无法通过多线程的方式将CPU的使用率突破100%,
#   但是对于现在多核计算机而言CPU使用率100%仅仅意味着将一个CPU跑满,其他CPU都在摸鱼(一人干活,多人围观)
#   为了更加充分的使用CPU的计算能力,我们可以使用多进程
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import current_process, Process
from time import sleep


# -------------------- 单进程和多进程的区别 --------------------
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


def single_process():
    """单进程的执行to_travel函数"""
    lis = ['クロニコのながぐつ', '人の痛みがわかる国', '多数決の国', '大人の国', '東亜重工']
    to_travel('kaiba', lis)
    to_travel('kino', lis)
    to_travel('kiri', lis)


def multi_process():
    """多进程的执行to_travel函数"""
    lis = ['クロニコのながぐつ', '人の痛みがわかる国', '多数決の国', '大人の国', '東亜重工']
    Process(target=to_travel, args=('kaiba', lis)).start()
    Process(target=to_travel, args=('kino', lis)).start()
    to_travel('kiri', lis)


"""对比上述单进程和多进程的执行结果,可以更好的感受到他们之间的区别"""

# -------------------- 多进程和多线程的区别 --------------------
PRIMES = [
             1116281,
             1297337,
             104395303,
             472882027,
             533000389,
             817504243,
             982451653,
             112272535095293,
             112582705942171,
             112272535095293,
             115280095190773,
             115797848077099,
             1099726899285419
         ] * 5


def is_prime(num):
    """判断素数(了解一下就好了,涉及到一些数论...原理我也搞不太清楚...;重点在于通过这个栗子,体会多进程和多线程的区别)"""
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def multi_thread_prime():
    """多线程版本(注意我们用的是ThreadPool-线程池)"""
    with ThreadPoolExecutor(max_workers=16) as executor:
        """下面这种写法可能会有点陌生,可以参照下面的补充解释"""
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is prime: {prime}')


def multi_process_prime():
    """多进程版本(注意我们用的是ProcessPool-进程池)"""
    with ProcessPoolExecutor(max_workers=16) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'number: {number} is prime: {prime}')


def main():
    # single_process()
    # multi_process()
    """使用time python 12_并发编程2.py 执行;
    观察最后的输出结果中cpu使用率,对比多线程和多进程
    (是不是有点晕~hhh,放轻松,目前有个概念就好啦~) """

    """通过观察可以发现,多线程情况下cpu使用率只能逼近100%,没有榨干多核cpu的性能"""
    # multi_thread_prime()

    """通过观察可以发现,多进程情况下cpu使用率能简单的突破100%(具体多少与CPU核心数相关,m1是660%),相比多线程能更好榨干cpu性能"""
    multi_process_prime()

    pass


if __name__ == '__main__':
    main()
